import pymysql
import time

# book管理核心类
class BookManager:
    # 初始化数据库连接
    def __init__(self):
        try:
            self.conn = pymysql.connect(
                host="localhost",
                user="root",          # 改为自己的MySQL账号
                password="123456",    # 改为自己的MySQL密码
                database="book_db",
                charset="utf8mb4",
                autocommit=False
            )
            self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
            print("✅ 数据库连接成功")
        except Exception as e:
            print("❌ 数据库连接失败：", e)

    # 日志记录工具
    def write_log(self, msg):
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        with open("book_log.txt", "a", encoding="utf-8") as f:
            f.write(f"[{now}] {msg}\n")

    #用户注册
    def register(self,user,password):
        try:
            sql = "INSERT INTO user(user,passwords,priority) VALUES(%s,%s,2)"
            self.cursor.execute(sql, (user,password))
            self.conn.commit()
            print("✅ 注册成功")
            self.write_log(f"新用户注册：{user}")
        except Exception as e:
            self.conn.rollback()
            print("❌ 注册失败：", e)
    
    def new_password(self,user,password,new__password):
        try:
            sql1="select passwords from user where user=%s"
            self.cursor.execute(sql1,user)
            res=self.cursor.fetchone()["passwords"]
            print(res,type(res))
            if password==res:
                sql2="update user set passwords=%s where user=%s"
                self.cursor.execute(sql2,(new__password,user))
                self.conn.commit()
                print("密码修改成功！")
        except Exception as e:
            self.conn.rollback()
            print("❌ 密码修改失败：", e)

    #用户登入
    def user(self,user,password):
        try:
            sql = """
            SELECT priority
            FROM user
            where user=%s and passwords=%s
            """
            self.cursor.execute(sql,(user,password))
            res = self.cursor.fetchall()
            return res
        except Exception as e:
            print("账号或密码错误 ",e)  
            return 0

    # 1. 添加book信息
    def add_book(self, book_name,author,classify):
        try:
            #先判断插入book是否重复
            sql1 ="select * from book where book_name=%s and author=%s"
            self.cursor.execute(sql1, (book_name,author))
            res = self.cursor.fetchone()
            # 插入book基础信息
            if not res:
                sql_book = "INSERT INTO book(book_name,author,classify,state) VALUES(%s,%s,%s,1)"
                self.cursor.execute(sql_book, (book_name,author,classify))

                self.conn.commit()
                print("✅ 图书信息及成绩添加成功")
                self.write_log(f"新增图书：书名:{book_name}--作者:{author}")
            else:
                print("图书重复！")
        except Exception as e:
            self.conn.rollback()
            print("❌ 添加失败！图书重复或数据格式错误")

    # 2. 查看所有book
    def show_all_book(self):
        sql = """
        SELECT *
        FROM book
        """
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        # print(res,type(res))

        print("\n========== book完整信息列表 ==========")
        for item in res:
            a='可借阅' if item['state']==1 else '已借出'
            if item['state']:
                print(f"图书编号：{item['book_id']}, 书名：{item['book_name']}， 作者：{item['author']}， 状态：{a}")

    # 3. 按条件精准查询图书信息
    def search_book(self, out,sta):
        sql=f'select * from book where {sta} like \"%{out}%\"'
        # print(sql)
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        # print(res)
        if type(res)== list :
            for item in res :
                if item['state']:
                    a='可借阅' if item['state']==1 else '已借出'
                    print(f"图书编号：{item['book_id']}, 书名：{item['book_name']}， 作者：{item['author']}， 状态：{a}")
        elif type(res) == dict:
            if res['state']:
                a='可借阅' if res['state']==1 else '已借出'
                print(f"图书编号：{res['book_id']}, 书名：{res['book_name']}， 作者：{res['author']}， 状态：{a}")
        else:
            print("未找到该图书")


    # 4. 修改book基础信息
    def update_book(self,book_id,new_name,new_author,new_classify):
        try:
            sql = "UPDATE book SET book_name=%s, author=%s, classify=%s WHERE book_id=%s"
            self.cursor.execute(sql, (new_name,new_author,new_classify,book_id))
            self.conn.commit()

            if self.cursor.rowcount > 0:
                print("✅ 图书基础信息修改成功")
                self.write_log(f"修改图书基础信息：编号：{book_id}")
            else:
                print("❌ 未找到该图书")
        except:
            self.conn.rollback()
            print("❌ 修改失败")

    # 5. 删除book信息
    def delete_book(self, book_id):
        try:
            # 只需删除学生表数据，成绩表会自动级联删除
            sql = "UPDATE book SET state=0 WHERE book_id=%s"
            self.cursor.execute(sql, book_id)
            self.conn.commit()

            if self.cursor.rowcount > 0:
                print("✅ 对应图书已删除")
                self.write_log(f"删除图书数据：编号：{book_id}")
            else:
                print("❌ 未找到图书")
        except:
            self.conn.rollback()
            print("❌ 删除失败")

    def show_delete(self):
        sql="select * from book where state=0"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        print("\n========== 已删除的book信息列表 ==========")
        for item in res:
            print(f"图书编号：{item['book_id']}, 书名：{item['book_name']}， 作者：{item['author']}")

    #6. 借书与还书
    def bore_book(self,book_id,user):
        try:
            sql="select * from book where book_id=%s"
            self.cursor.execute(sql,book_id)
            res=self.cursor.fetchone()      #获取借阅状态

            sql1="select * from borrower where book_id=%s and user=%s"
            self.cursor.execute(sql1,(book_id,user))
            res1=self.cursor.fetchone()     #获取用户是否借了这本书
            print(res1)

            if res['state']==1:
                sql3="SELECT COUNT(*) FROM borrower WHERE user = %s;"
                self.cursor.execute(sql3,user)
                count = self.cursor.fetchone()['COUNT(*)']

                print(f"当前借了{count}本书",type(count))
                print(book_id,type(book_id),user,type(user))

                # 插入借阅记录和期限(不能借超过3本书)
                if count<3:
                    #book表状态更新
                    sql1="update book set state=2 where book_id=%s"
                    self.cursor.execute(sql1,book_id)
                    self.conn.commit()
                    print("✅ 借阅成功")
                    self.write_log(f"编号 {book_id} 的图书已借出")

                    #borrower表数据更新
                    sql2="insert into borrower(book_id,user,kai,jie) values(%s,%s, CURDATE(), CURDATE() + INTERVAL 7 DAY)"
                    self.cursor.execute(sql2,(book_id,user))
                    self.conn.commit()

                else:

                    print("❌ 借阅失败，已超过借阅次数")

            elif res['state']==2:

                if res1:
                    sql1="update book set state=1 where book_id=%s"
                    self.cursor.execute(sql1,book_id)
                    self.conn.commit()
                    print("✅ 还书成功")    
                    self.write_log(f"编号 {book_id} 的图书已还进")

                    # 插入还书记录和期限
                    sql2="delete from borrower where book_id=%s"
                    self.cursor.execute(sql2,book_id)
                    self.conn.commit()
                else:
                    print("你没借这本书！")

            else:
                print("❌ 该书已借出")
        except:
            self.conn.rollback()
            print("❌ 借阅失败")

    #7.借阅用户数据
    def show_borrower(self,user):
        print(f"====={user}用户您好=====")
        sql="select * from borrower join book on borrower.book_id=book.book_id where user=%s"
        self.cursor.execute(sql, user)
        results = self.cursor.fetchall()
        for row in results:
            print(f"书名：{row['book_name']}， 作者：{row['author']}， 借阅日期：{row['kai']}， 还书日期：{row['jie']}，借阅用户：{row['user']}")

    #8.查看指定用户数据
    def show_all_borrower(self,user):
        print(f"====={user}管理员您好=====")
        sql="select * from borrower join book on borrower.book_id=book.book_id"
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        for row in results:
            print(f"书名：{row['book_name']}， 作者：{row['author']}， 借阅日期：{row['kai']}， 还书日期：{row['jie']}，借阅用户：{row['user']}")

    # 关闭数据库连接
    def close(self):
        self.cursor.close()
        self.conn.close()
        print("✅ 数据库连接已关闭")

    

# 主菜单函数
def main():
    sm = BookManager()
    users=input("请输入用户名：")
    passwords=input("请输入密码：")
    while True:
        try:
            a=sm.user(users,passwords)
            nn=a[0]['priority']
            print('登录成功:',users)
            break
        except:
            print("错误!")
            exit()
    if nn==1:
        while True:
            print("\n======= 图书信息管理系统【root版】=======")
            print("1. 添加图书信息")
            print("2. 查看所有图书完整信息")
            print("3. 按条件查询图书")
            print("4. 修改图书基础信息")
            print("5. 删除图书信息")
            print("6. 借阅图书")
            print("7. 查看借阅用户借书数据")
            print("8. 查看指定用户借书数据")
            print("9. 查看已删除的图书信息")
            print("10.修改密码")
            print("0. 退出系统")
            print("==========================================")

            choice = input("请输入功能编号：")

            if choice == "1":
                book_name = input("请输入书名：")
                author = input("请输入作者：")
                classify = input("请输入分类：")
                sm.add_book(book_name,author,classify)

            elif choice == "2":
                sm.show_all_book()

            elif choice == "3":
                sta=input("1.图书编号查询\n2.书名查询\n3.作者查询\n4.分类查询\n请选择查询功能：")
                if sta=='1':
                    out=input("输入图书编号：")
                    sm.search_book(out,"book_id")
                elif sta=='2':
                    out=input("输入书名：")
                    sm.search_book(out,"book_name")
                elif sta=='3':
                    out=input("输入作者：")
                    sm.search_book(out,"author")
                elif sta=='4':
                    out=input("输入分类：")
                    sm.search_book(out,"classify")
                else:
                    print('选择无效！')

            elif choice == "4":
                book_id = input("请输入要修改的图书编号：")
                new_name = input("请输入新书名：")
                new_author = input("请输入新作者：")
                new_classify = input("请输入新分类：")
                sm.update_book(book_id,new_name,new_author,new_classify)

            elif choice == "5":
                sid = input("请输入要删除的图书编号：")

                i=input("确认吗? y/n")
                if i=='y':
                    sm.delete_book(sid)
                elif i=='n':
                    print("取消删除")

                else:
                    print("输入无效")

            elif choice == "6":

                sid = input("请输入要借阅or交还的图书编号：")
                sm.bore_book(sid,users)

            elif choice == "7":
                sm.show_all_borrower(users)

            elif choice == "8":

                user=input("请输入用户名：")
                sm.show_borrower(user)
            
            elif choice == "9":
                sm.show_delete()

            elif choice == '10':
                password=input("输入账号密码：")
                new_password=input("输入新密码：")
                sm.new_password(users,password,new_password)

            elif choice == "0":
                sm.close()
                print("👋 系统退出成功，再见！")
                break

            else:
                print("❌ 输入无效，请输入0-9的数字！")
    elif nn==2:
        while True:
            print("\n======= 图书信息管理系统【用户版】=======")
            print("1. 查看所有图书完整信息")
            print("2. 按条件查询图书")
            print("3. 借阅图书")
            print("4.查看个人借阅信息")
            print("5.修改密码")
            print("0. 退出系统")
            print("==========================================")

            choice = input("请输入功能编号：")
            if choice == "1":
                sm.show_all_book()

            elif choice == "2":
                sta=input("1.图书编号查询\n2.书名查询\n3.作者查询\n4.分类查询\n请选择查询功能：")
                if sta=='1':
                    out=input("输入图书编号：")
                    sm.search_book(out,"book_id")
                elif sta=='2':
                    out=input("输入书名：")
                    sm.search_book(out,"book_name")
                elif sta=='3':
                    out=input("输入作者：")
                    sm.search_book(out,"author")
                elif sta=='4':
                    out=input("输入分类：")
                    sm.search_book(out,"classify")
                else:
                    print('选择无效！')

            elif choice == "3":
                book_id = input("请输入要借阅or交还的图书编号：")
                sm.bore_book(int(book_id),users)

            elif choice == '4':
                password=input("输入账号密码：")
                new_password=input("输入新密码：")
                sm.new_password(users,password,new_password)

            elif choice == "0":
                sm.close()
                print("👋 系统退出成功，再见！")
                break
            else:
                print("❌ 输入无效，请输入0-3的数字！")
                
    else:
        print("没有访问权限！")
            


if __name__ == "__main__":
    while 1:
        print("================图书管理系统================")
        n=input("注册or登入1/2: ")
        if n=='1':
            m=BookManager()
            username=input("请输入用户名：")
            password=input("请输入密码：")
            m.register(username, password)
        elif n=='2':
            main()
