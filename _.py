# a=[]
# for i in range(0,100+1,7):
#     if i % 5 !=0:
#         print(i,end=' ')



# for i in range(100,1000):
#     if i == (i//100)**3 + (i//10-(i//100)*10)**3 + (i//1-(i//10)*10)**3:
#         print(i)


# 632  6     632//100     
# 632  63    632//10-(632//100)*10     
# 632  632   632-(632//10)*10     


# def aa(n,i,count,x):
#     count=count+1
#     if count>n-1:
#         return i//(10**(n-1))
#     x1=i//(10**(n-1-count))-x*10
#     x1_i=x1**n
#     x=i//(10**(n-1-count))
#     return x1_i+aa(n,i,count,x)
# n=int(input("数字位数："))
# for i in range(10**(n-1),10**n):
#     a=aa(n,i,0,i//(10**(n-1)))
#     if i==int(a):
#         print(i)

# n=3
# i=153
# print(aa(3,153,0,1))

# a=[1,2,3,4,5,6]
# b=a[:]
# b[1]="A"
# a[0]="B"
# c=a.count(6)
# print(a,b,c)




# a=[]
# b=[1,2,3]
# for i in range (3):
#     for j in b:
#         a.append(j)
# b=a.count(a[1])
# print("____")
# print(b)
# a.reverse()
# print(a)


# x=[1,2,3,4]
# y=["A","B","C","D"]

# a=dict(zip(x,y))
# print(*a)


# # a=dict()
# # a.update({1:2})
# print(a)


# a="QWERTYUIOPQWERTYUIOP"
# print(a.find("R"),a.rfind("R"),a.index("R"),a.rindex("R"),a.count("R"))
# print(a.find("1"),a.rfind("1"))
# print(a.split("R"),a.rsplit("R"),a.partition("RT"),a.rpartition("RT"),sep="\n")
# print(a.replace("Q","122",1232))
# s = "! @#$% ^&*"
# table = str.maketrans("*$^%@#&!", "TKCELIAI")
# trans_s = s.translate(table)
# print(trans_s)
# # 输出： I LIKE CAT




# test = 'hello world! I like python. this is a nice day. right?'
#
# import re
#
# def format_english(text):
#     text = ' '.join(text.split())
#     text = re.sub(r'(?<=[.!?])\s+([a-z])', lambda m: ' ' + m.group(1).upper(), text)
#     text = text[0].upper() + text[1:]
#     return text
# formatted_text = format_english(test)
# print("1. 正常英文格式：")
# print(formatted_text)
# print()
#
# words = test.split()
# word_count = len(words)
# print("2. 单词个数：")
# print(word_count)
# print()
#
# def caesar_encrypt(text, k):
#     k = k % 26
#     lower = 'abcdefghijklmnopqrstuvwxyz'
#     upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     trans_table = str.maketrans(
#         lower + upper,
#         lower[k:] + lower[:k] + upper[k:] + upper[:k]
#     )
#     return text.translate(trans_table)
#
# k = 3
# encrypted_text = caesar_encrypt(test, k)
# print(f"3. 加密结果（k={k}）：")
# print(encrypted_text)

# import string,random;
# a='01234567890'
# b='ABCDEFGHIJKMNOPQLSTUVWSYZ'
# print(''.join([random.choice(a+b) for i in range(6)]))

# import random
# a=[str(random.randint(1,10000))+'\n' for i in range(50)]
# b=[]
# b_=[]
# with open ('a.txt','w') as f0:
#     f0.writelines(a)
#     print('数据创建成功保存在a.txt')
#
# with open ('a.txt','r') as f1:
#     s=f1.readlines()
#     for i in s:
#         b.append(int(i))
#
#
# with open ('b.txt','w') as f2:
#     b.sort()
#     for i in b[::-1]:
#         b_.append(str(i)+'\n')
#     print(b_)
#     f2.writelines(b_)
#     print('数据排序成功保存在b.txt')

# import os
# a=os.getcwd()
# b=os.listdir(os.getcwd())
# for i in os.listdir(os.getcwd()):
#     print("是否文件",os.path.isfile(i))
#     print('是否是.py',i.endswith('.py'))
#     print()
# print(a,b,sep='\n')

# 遍历目录（生成器）
# print(os.listdir('.'))  # 当前目录所有文件和子目录

# 遍历目录（生成器）
# for root, dirs, files in os.walk("shixv"):
#     print(f"当前目录: {root}")
#     print(f"子目录: {dirs}")
#     print(f"文件: {files}")
#     for i in dirs:
#         print(root + '\\' + i )
#         print(os.path.join(root,i))
#     for j in files:
#         print(root + '\\' + j )
#         print(os.path.join(root,j))

# totalSize,fileNum,dirNum=0,0,0
# for root, dirs, files in os.walk("shixv"):
#     print(f"当前目录: {root}")
#     print(f"子目录: {dirs}")
#     print(f"文件: {files}")
#     # totalSize=totalSize+len(dirs)+len(files)
#     for i in files:
#         totalSize+=(os.stat(os.path.join(root,i))).st_size
#     fileNum+=len(files)
#     dirNum+=len(dirs)
#
#
# print()
# print(f"文件夹大小：{totalSize}字节,文件数量：{fileNum},子文件夹数量：{dirNum}")


# class ShortInputException(Exception):
#     def __init__(self, length, atleast):
#         Exception.__init__(self)
#         self.length = length
#         self.atleast = atleast


# try:
#     s = "1111"
#     if len(s) < 3:
#         raise ShortInputException(len(s), 3)
# except EOFError:
#     print('你输入了一个结束标记EOF')
# except ShortInputException as x:
#     print('ShortInputException: 长度是 %d, 至少应是 %d' % (x.length, x.atleast))
# else:
#     print('没有异常发生.')


# class sb(Exception):
#     pass

# a=input()
# if a .isdigit():
#     print(a)
# else:
#     raise sb("出错")
# 123

# from __ import aa
# print(aa(input()))

# from datetime import datetime
# while(1):
#     now=datetime.now()
#     time=now.strftime('%Y年-%m月-%d日  %H时-%M分-%S秒')
#     # print('\r',now, end='')
#     print(now)
#     print(time, end='')




# import json
# a={
# "company": "Alibab",
# "employees": [{"name": "Alice", "position": "Engineer", "salary": 10000},
#               {"name": "Bob", "position": "Manager", "salary": 15000}],
# "location": "Hangzhou"}
# print(a)
# print(json.dumps(a,indent=4))


# import requests


# dicts={
#     "name":"张三",
#     "age":18,
#     "sex":"男"
# }
# requests = requests.get('https://httpbin.org/get',dicts,timeout=1)
# print("状态码：",requests.status_code)
# # print("响应头：",requests.headers)
# # print("响应内容：",requests.text)
# print("最终url：",requests.url)
# print("响应内容：",requests.json())
# print("超时时间：",requests.elapsed.total_seconds())


# import requests
# import json

# API_KEY = "2d281b9a960c62d33574b51d88344123"
# city = "新余"  # 城市 adcode，110000 = 北京

# url = "https://restapi.amap.com/v3/weather/weatherInfo" # 天气查询接口
# params = {"key": API_KEY, "city": city, "extensions": "all"}
# res = requests.get(url, params=params)
# print(json.dumps(res.json(),indent=4))
# res=res.json()

# def get_weather(key, city):
#     url = "https://restapi.amap.com/v3/weather/weatherInfo"

#     # 实况天气
#     params = {"key": key, "city": city, "extensions": "base"}
#     res = requests.get(url, params=params).json()
#     if res["status"] == "1":
#         live = res["lives"][0]
#         print(f"实况: {live['weather']}, {live['temperature']}°C, {live['winddirection']}风{live['windpower']}级, 湿度{live['humidity']}%")
#     else:
#         print(f"实况请求失败: {res['info']}")

#     # 天气预报（4天）
#     params["extensions"] = "all"
#     res = requests.get(url, params=params)
#     res=res.json()
  
#     if res["status"] == "1":
#         print("\n预报:")
#         for day in res["forecasts"][0]["casts"]:
#             print(f"  {day['date']}: {day['dayweather']}, {day['nighttemp']}°C ~ {day['daytemp']}°C")
#     else:
#         print(f"预报请求失败: {res['info']}")

# get_weather(API_KEY, city)


# class Student:

#     def aa(self, name, age, score):
#         self.name = name
#         self.age = age
#         self.score = score
#         duanhaoyu=100

# s=Student()
# s.aa("张三",18,90)
# print(s.name)
# # print(s.duanhaoyu)


# class Car:
#     color='白色'
#     def run (self):
#         print(f"一辆{self.color}的汽车在跑")

# c=Car()
# c.run()
# c.color='红色'
# c.run()



# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def get_area(self):
#         return self.width * self.height
    
#     def get_perimeter(self):
#         return 2 * (self.width + self.height)
    
#     @classmethod
#     def create_square(cls, side_length):
#         return cls(side_length, side_length)
    
# r=Rectangle(5,3)
# print("面积：",r.get_area(),"周长：",r.get_perimeter())

# r2=Rectangle.create_square(4)
# print("面积：",r2.get_area(),"周长：",r2.get_perimeter())   
        


# class Shape ():
#     def get_area(self):
#         return 0
    
#     def aa(self):
#         return print("测试成功！")

# class Square (Shape):
#     def __init__(self, side_length):
#         self.side_length = side_length

#     def get_area(self):
#         return self.side_length * self.side_length

# class Circle (Shape):

#     def __init__(self, radius):

#         self.radius = radius
    
#     def get_area(self):
#         return 3.14 * self.radius * self.radius
    
# s1=Square(5)
# s2=Circle(3)
# print(s1.get_area())
# print(s2.get_area())
# print(s1.get_area()+s2.get_area())
# s1.aa()
# s2.aa()


# class Attributes ():
#     def __init__(self,account_id,name):
#         self.account_id=account_id
#         self.name=name
#
#     def kaihu(self,account_id,password,name,balance):
#         self.account_id=account_id
#         self.__password=password
#         self.name=name
#         self.__balance=balance
#         return print('开户成功')
#
#
#     def cha(self,password):
#         if self.__password==password :
#             return print('金额为:',self.__balance)
#         else:
#             return print('密码错误')
#
#     def cun(self,password,balance):
#         if self.__password==password:
#             self.__balance+=balance
#             return print('存款成功，现在金额为:',self.__balance)
#         else:
#             return print('存款失败')
#
#     def qv(self,password,balance):
#         if self.__password==password:
#             self.__balance-=balance
#             return print('取款成功，现在金额为:',self.__balance)
#         else:
#             return print('取款失败')
#
#     def xiou(self,password,newpassword):
#         if self.__password==password:
#             self.__password=newpassword
#             return print('修改成功')
#         else:
#             return print('修改失败')
#
# while(1):
#     a=input("1.开户，2.查询，3.存款，4.取款，5.修改密码，6.退出")
#     if a=='1':
#         account_id=input('请输入账号:')
#         password=input('请输入密码:')
#         name=input('请输入姓名:')
#         balance=int(input('请输入金额:'))
#         b=Attributes(account_id,name)
#         b.kaihu(account_id,password,name,balance)
#
#
#     elif a=='2':
#         password=input('请输入密码:')
#         b.cha(password)
#
#     elif a=='3':
#         password=input('请输入密码:')
#         balance=int(input('请输入金额:'))
#         b.cun(password,balance)
#
#     elif a=='4':
#         password=input('请输入密码:')
#         balance=int(input('请输入金额:'))
#         b.qv(password,balance)
#
#     elif a=='5':
#         password=input('请输入密码:')
#         newpassword=input('请输入新密码:')
#         b.xiou(password,newpassword)
#
#     elif a=='6' :
#         print("已退出")
#         break
#
#     else:
#         print("无效选项,请重新输入")


# -- CREATE TABLE employees (
# --     emp_id INT PRIMARY KEY AUTO_INCREMENT COMMENT '员工编号',
# --     name VARCHAR(20) NOT NULL COMMENT '员工姓名',
# --     salary DECIMAL(10,2) COMMENT '薪水',
# --     position VARCHAR(20) COMMENT '职位',
# --     department VARCHAR(20) COMMENT '部门',
# --     entry_date DATE COMMENT '入职日期',
# --     gender CHAR(1) COMMENT '性别'
# -- ) COMMENT='员工信息表';

# mysql> use gs
# Database changed
# mysql> desc employees;
# +----------+---------------+------+-----+---------+----------------+
# | Field    | Type          | Null | Key | Default | Extra          |
# +----------+---------------+------+-----+---------+----------------+
# | emp_id   | int           | NO   | PRI | NULL    | auto_increment |
# | emp_name | varchar(20)   | YES  |     | NULL    |                |
# | salary   | decimal(10,2) | YES  |     | NULL    |                |
# | dept_id  | int           | YES  |     | NULL    |                |
# +----------+---------------+------+-----+---------+----------------+
# mysql> select * from employees;
# +--------+----------+----------+---------+
# | emp_id | emp_name | salary   | dept_id |
# +--------+----------+----------+---------+
# |      1 | 小明     |  8000.00 |       1 |
# |      2 | 小红     |  9000.00 |       1 |
# |      3 | 小刚     | 12000.00 |       2 |
# |      4 | 小丽     |  7500.00 |    NULL |
# |      5 | 小强     | 11000.00 |      99 |
# +--------+----------+----------+---------+


import pymysql


# ============================================================
# DBHelper 数据库操作基类
# ============================================================
class DBHelper:
    """数据库操作基类，封装 pymysql 连接与基础操作"""

    def __init__(self, host="127.0.0.1", port=3306, user="root",
                 password="123456", database="gs"):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
        self.cursor = None

    def connect(self):
        """建立数据库连接并获取游标"""
        self.conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.conn.cursor()
        return self.cursor

    def close(self):
        """关闭游标和连接"""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def execute(self, sql, params=None):
        """执行增删改 SQL，返回受影响行数"""
        if params:
            rows = self.cursor.execute(sql, params)
        else:
            rows = self.cursor.execute(sql)
        self.conn.commit()
        return rows

    def query(self, sql, params=None):
        """执行查询 SQL，返回全部结果"""
        if params:
            self.cursor.execute(sql, params)
        else:
            self.cursor.execute(sql)
        return self.cursor.fetchall()

    def query_one(self, sql, params=None):
        """执行查询 SQL，返回单条结果"""
        if params:
            self.cursor.execute(sql, params)
        else:
            self.cursor.execute(sql)
        return self.cursor.fetchone()


# ============================================================
# UserManager 用户管理类（依赖 DBHelper）
# ============================================================
class UserManager:
    """用户数据表 CRUD 操作，依赖注入 DBHelper 实例"""

    def __init__(self, db_helper):
        """
        构造方法，接收 DBHelper 实例作为依赖
        :param db_helper: DBHelper 实例
        """
        self.db = db_helper
        self.db.connect()
        self._ensure_table()

    def _ensure_table(self):
        """确保 users 表存在"""
        sql = """
        CREATE TABLE IF NOT EXISTS users (
            id INT PRIMARY KEY AUTO_INCREMENT COMMENT '用户编号',
            name VARCHAR(50) NOT NULL COMMENT '用户名',
            email VARCHAR(100) COMMENT '邮箱'
        ) COMMENT='用户信息表'
        """
        self.db.execute(sql)

    # ---- CRUD 操作 ----

    def add_user(self, name, email):
        """新增用户"""
        sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
        self.db.execute(sql, (name, email))
        print(f"新增用户成功：{name}，邮箱：{email}")

    def batch_add_users(self, user_list):
        """批量新增用户
        :param user_list: [(name, email), ...] 列表
        """
        sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
        rows = self.db.cursor.executemany(sql, user_list)
        self.db.conn.commit()
        print(f"批量新增 {rows} 条用户数据成功")
        return rows

    def get_user_by_id(self, user_id):
        """根据 ID 查询用户"""
        sql = "SELECT * FROM users WHERE id = %s"
        result = self.db.query_one(sql, (user_id,))
        if result:
            print(f"查询结果：ID={result[0]}, 姓名={result[1]}, 邮箱={result[2]}")
        else:
            print(f"未找到 ID={user_id} 的用户")
        return result

    def update_user_email(self, user_id, new_email):
        """更新用户邮箱"""
        sql = "UPDATE users SET email = %s WHERE id = %s"
        rows = self.db.execute(sql, (new_email, user_id))
        if rows:
            print(f"用户 ID={user_id} 邮箱已更新为：{new_email}")
        else:
            print(f"更新失败：未找到 ID={user_id} 的用户")

    def delete_user(self, user_id):
        """删除用户"""
        sql = "DELETE FROM users WHERE id = %s"
        rows = self.db.execute(sql, (user_id,))
        if rows:
            print(f"用户 ID={user_id} 已删除")
        else:
            print(f"删除失败：未找到 ID={user_id} 的用户")

    def list_all(self):
        """列出所有用户"""
        sql = "SELECT * FROM users"
        results = self.db.query(sql)
        if results:
            print("\n===== 用户列表 =====")
            for row in results:
                print(f"ID={row[0]}, 姓名={row[1]}, 邮箱={row[2]}")
        else:
            print("用户表为空")
        return results

    def show_table(self):
        """以 MySQL 命令行格式可视化当前数据表"""
        sql = "SELECT * FROM users"
        self.db.cursor.execute(sql)
        results = self.db.cursor.fetchall()
        col_names = [desc[0] for desc in self.db.cursor.description]

        if not results:
            print("Empty set")
            return

        # 计算各列最大宽度
        col_widths = []
        for i, name in enumerate(col_names):
            max_w = len(name)
            for row in results:
                max_w = max(max_w, len(str(row[i])))
            col_widths.append(max_w)

        # 分隔线
        sep = "+" + "+".join("-" * (w + 2) for w in col_widths) + "+"

        # 表头
        print(sep)
        header = "|" + "|".join(
            f" {col_names[i]:{col_widths[i]}} " for i in range(len(col_names))
        ) + "|"
        print(header)
        print(sep)

        # 数据行
        for row in results:
            line = "|" + "|".join(
                f" {str(row[i]):{col_widths[i]}} " for i in range(len(row))
            ) + "|"
            print(line)

        print(sep)
        print(f"{len(results)} row(s) in set\n")

    def reset_table(self, backup_data):
        """还原表内数据：清空表并重新插入备份数据
        :param backup_data: [(name, email), ...] 原始数据列表
        """
        self.db.execute("DELETE FROM users")
        self.db.execute("ALTER TABLE users AUTO_INCREMENT = 1")
        if backup_data:
            self.batch_add_users(backup_data)
        print("数据表已还原")

    def disconnect(self):
        """主动断开数据库连接"""
        self.db.close()
        print("数据库连接已关闭")


# ============================================================
# 测试代码
# ============================================================
if __name__ == "__main__":
    # 1. 创建 DBHelper 实例
    db = DBHelper(host="127.0.0.1", port=3306, user="root",
                  password="123456", database="gs")

    # 2. 依赖注入到 UserManager
    um = UserManager(db)

    # 3. 批量添加 12 条测试数据
    sample_users = [
        ("张三", "zhangsan@example.com"),
        ("李四", "lisi@example.com"),
        ("王五", "wangwu@example.com"),
        ("赵六", "zhaoliu@example.com"),
        ("孙七", "sunqi@example.com"),
        ("周八", "zhouba@example.com"),
        ("吴九", "wujiu@example.com"),
        ("郑十", "zhengshi@example.com"),
        ("小明", "xiaoming@example.com"),
        ("小红", "xiaohong@example.com"),
        ("小刚", "xiaogang@example.com"),
        ("小丽", "xiaoli@example.com"),
    ]
    um.batch_add_users(sample_users)

    um.show_table()

    # 4. 数据还原 + 断开连接
    um.reset_table(sample_users)

    um.show_table()
    um.add_user("张三", "zhangsan@example.com")
    um.add_user("李四", "lisi@example.com")
    um.show_table()
    um.get_user_by_id(1)
    um.update_user_email(1, "zhangsan_new@example.com")
    um.get_user_by_id(1)
    um.delete_user(2)

    um.disconnect()
