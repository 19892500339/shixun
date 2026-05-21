"""
作业1：定义图书类（Book）
- 属性：书名、作者、价格
- 方法：show_info() 格式化输出图书完整信息
"""

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def show_info(self):
        print("=" * 30)
        print(f"书名：《{self.title}》")
        print(f"作者：{self.author}")
        print(f"价格：¥{self.price:.2f}")
        print("=" * 30)


# ============================================================

"""
作业2：完善银行账户系统
- 在账户类基础上添加计算利息的方法
- 年利率 1.5%，实现简单利息计算
"""

class BankAccount:
    def __init__(self, account_id, name, balance=0.0):
        self.account_id = account_id
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"存款 ¥{amount:.2f} 成功，当前余额：¥{self.balance:.2f}")
        else:
            print("存款金额必须大于0")

    def withdraw(self, amount):
        if amount > self.balance:
            print("余额不足，取款失败")
        elif amount > 0:
            self.balance -= amount
            print(f"取款 ¥{amount:.2f} 成功，当前余额：¥{self.balance:.2f}")
        else:
            print("取款金额必须大于0")

    def calculate_interest(self, years):
        """
        计算简单利息
        公式：利息 = 本金 × 年利率 × 年数
        """
        rate = 0.015  # 年利率 1.5%
        interest = self.balance * rate * years
        print(f"本金 ¥{self.balance:.2f}，存 {years} 年，年利率 {rate*100}%")
        print(f"简单利息为：¥{interest:.2f}")
        print(f"{years} 年后本息合计：¥{self.balance + interest:.2f}")
        return interest

    def show_info(self):
        print("=" * 30)
        print(f"账户：{self.account_id}")
        print(f"户主：{self.name}")
        print(f"余额：¥{self.balance:.2f}")
        print("=" * 30)


# ============================================================

"""
作业3（思考题）：面向对象的优势
对比面向过程编程，面向对象编程（OOP）在大型软件开发中的核心优势：

1. 封装性 —— 将数据和操作封装在类中，对外隐藏实现细节，降低耦合
2. 继承性 —— 通过继承复用已有代码，减少重复，提高开发效率
3. 多态性 —— 同一接口不同实现，便于扩展和维护，符合开闭原则
4. 可维护性 —— 代码模块化，结构清晰，修改一处不影响全局
5. 可扩展性 —— 新增功能只需添加新类，无需修改现有代码
6. 团队协作 —— 各模块可独立开发，并行工作
"""

# ============================================================
# 测试代码
# ============================================================

def test_book():
    print("\n===== 测试 Book 类 =====")
    book1 = Book("三体", "刘慈欣", 68.00)
    book2 = Book("Python编程从入门到实践", "Eric Matthes", 89.00)
    book1.show_info()
    book2.show_info()

def test_bank():
    print("\n===== 测试 BankAccount 类 =====")
    acc = BankAccount("10086", "张三", 10000.0)
    acc.show_info()
    acc.deposit(5000)
    acc.withdraw(3000)
    acc.calculate_interest(3)  # 3年定期

if __name__ == "__main__":
    test_book()
    test_bank()
