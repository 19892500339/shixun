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
    um.add_user("张三", "zhangsan@example.com")
    um.add_user("李四", "lisi@example.com")
    um.get_user_by_id(1)
    um.update_user_email(1, "zhangsan_new@example.com")
    um.get_user_by_id(1)
    um.delete_user(2)
    um.show_table()

    # 4. 数据还原 + 断开连接
    um.reset_table(sample_users)
    um.disconnect()