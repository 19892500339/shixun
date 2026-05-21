# ====================================================================
# 文件总说明：
# 这是一个 Python 学习笔记文件，记录了从基础语法到高级应用（数据库编程）
# 的完整学习过程。每段代码都代表一个独立的学习实验或练习，
# 大部分代码已被注释以保留学习记录，最后一个模块（DBHelper + UserManager）
# 是运行中的数据库操作实践。
#
# 代码结构（按学习阶段）：
#   阶段1: Python 基础语法（循环、分支、列表、字典、字符串、正则、加密、随机）
#   阶段2: Python 高级内置功能（文件IO、os模块、异常、日期、JSON）
#   阶段3: Python 网络编程（requests、API调用）
#   阶段4: Python 面向对象编程（类、封装、继承、多态）
#   阶段5: Python 数据库编程（pymysql、CRUD）
# ====================================================================


# ====================================================================
# 阶段1：Python 基础语法
# 
# 【学了什么】
#   1. for循环与range()函数：掌握循环控制变量遍历数字序列
#   2. 整除//和取余%运算：用于提取数字的每一位（百位/十位/个位）
#   3. 水仙花数（阿姆斯特朗数）：每位数字的n次幂之和等于自身的数
#   4. 递归函数：函数自己调用自己，配合终止条件使用
#   5. 列表操作：copy()、count()、reverse()、append()、切片复制
#   6. 字典创建：dict()构造、zip()合并两个列表、update()更新
#   7. 字符串方法：find/rfind/index/rindex/count、split/rsplit、
#      partition/rpartition、replace、translate/maketrans
#   8. 正则表达式(re模块)：sub()替换、句子格式化、首字母大写
#   9. 凯撒密码加密：基于字母移位（偏移k位）的古典加密算法
#  10. random模块：choice()随机选择字符，生成随机验证码
# ====================================================================

# ----------------------------------------------------
# 练习1：输出 0~100 中能被 7 整除但不能被 5 整除的数
# 使用 range(start, end+1, step) 直接生成步长为 7 的序列
# ----------------------------------------------------
# a=[]
# for i in range(0,100+1,7):
#     if i % 5 !=0:
#         print(i,end=' ')


# ----------------------------------------------------
# 练习2：找出所有三位水仙花数（循环方式）
# 例如 153 = 1³ + 5³ + 3³
# 用整除 // 和取余 % 分别提取百位、十位、个位
# ----------------------------------------------------
# for i in range(100,1000):
#     if i == (i//100)**3 + (i//10-(i//100)*10)**3 + (i//1-(i//10)*10)**3:
#         print(i)


# ----------------------------------------------------
# 练习3：水仙花数——递归函数实现（通用版，支持任意位数）
# aa(n,i,count,x) 递归提取数字的每一位并计算 n 次幂之和
# n 是位数，i 是当前数字，count 是已处理的位数，x 是当前高位值
# ----------------------------------------------------
# # 632  6     632//100
# # 632  63    632//10-(632//100)*10
# # 632  632   632-(632//10)*10
#
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


# ----------------------------------------------------
# 练习4：列表的浅拷贝与操作方法
# a[:] 是浅拷贝，修改 b 不影响 a（但如果嵌套可变对象则会影响）
# .count() 统计元素出现次数
# ----------------------------------------------------
# a=[1,2,3,4,5,6]
# b=a[:]
# b[1]="A"
# a[0]="B"
# c=a.count(6)
# print(a,b,c)


# ----------------------------------------------------
# 练习5：列表的 append() 和 reverse() 操作
# count() 统计 a[1] 在 a 中出现的次数（a[1]=2，结果为 3）
# reverse() 原地反转列表
# ----------------------------------------------------
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


# ----------------------------------------------------
# 练习6：使用 zip() 将两个列表合并为字典
# zip(x, y) 返回一个迭代器，dict() 将其转为字典
# *a 解包字典，输出所有键
# ----------------------------------------------------
# x=[1,2,3,4]
# y=["A","B","C","D"]
# a=dict(zip(x,y))
# print(*a)
# # a=dict()
# # a.update({1:2})
# print(a)


# ----------------------------------------------------
# 练习7：字符串查找与分割方法大全
# find() 找不到返回 -1，index() 找不到抛出异常
# rfind/rindex 从右侧开始查找（返回索引位置不变）
# count() 统计出现次数
# split/rsplit 分割，partition/rpartition 分割为三元组
# replace() 替换所有匹配项
# ----------------------------------------------------
# a="QWERTYUIOPQWERTYUIOP"
# print(a.find("R"),a.rfind("R"),a.index("R"),a.rindex("R"),a.count("R"))
# print(a.find("1"),a.rfind("1"))  # 找不到返回 -1
# print(a.split("R"),a.rsplit("R"),a.partition("RT"),a.rpartition("RT"),sep="\n")
# print(a.replace("Q","122",1232))  # 第三参数为最大替换次数


# ----------------------------------------------------
# 练习8：字符串 translate() 和 maketrans() 字符映射转换
# str.maketrans(a, b) 建立从 a 中字符到 b 中字符的映射表
# translate(table) 按照映射表替换字符
# 示例效果：把乱码字符映射为 "I LIKE CAT"
# ----------------------------------------------------
# s = "! @#$% ^&*"
# table = str.maketrans("*$^%@#&!", "TKCELIAI")
# trans_s = s.translate(table)
# print(trans_s)
# # 输出： I LIKE CAT


# ----------------------------------------------------
# 练习9：正则表达式（re模块）——英文文本格式化
# 功能：移除多余空格、句子首字母大写、段落首字母大写
# re.sub(r'(?<=[.!?])\s+([a-z])', ...)  匹配句子结束符后的小写字母并转为大写
# .upper() + [1:]  整个段落首字母大写
# ----------------------------------------------------
# test = 'hello world! I like python. this is a nice day. right?'
#
# import re
#
# def format_english(text):
#     text = ' '.join(text.split())  # 移除多余空格
#     text = re.sub(r'(?<=[.!?])\s+([a-z])', lambda m: ' ' + m.group(1).upper(), text)
#     text = text[0].upper() + text[1:]  # 段落首字母大写
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
#
# ----------------------------------------------------
# 练习10：凯撒密码加密算法
# 原理：将每个字母按字母表顺序向后偏移 k 位（循环）
# maketrans() 构建位移后的字母映射表，translate() 执行转换
# k % 26 确保偏移量在合理范围内
# ----------------------------------------------------
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


# ----------------------------------------------------
# 练习11：random模块——生成随机6位验证码
# random.choice() 从给定序列中随机选取一个元素
# 列表推导式：循环6次，每次选一个随机字符，用 join 拼接为字符串
# ----------------------------------------------------
# import string,random;
# a='01234567890'
# b='ABCDEFGHIJKMNOPQLSTUVWSYZ'
# print(''.join([random.choice(a+b) for i in range(6)]))


# ====================================================================
# 阶段2：Python 高级内置功能
#
# 【学了什么】
#   1. 文件IO操作：open()读写模式、readlines()、writelines()
#   2. 数据排序处理：读取文件→类型转换→排序→写入新文件
#   3. os模块：getcwd()、listdir()、path.isfile()、path.join()
#   4. os.walk()：递归遍历目录树，统计文件数量和大小
#   5. os.stat()：获取文件元信息（大小、修改时间等）
#   6. 自定义异常类：继承Exception，自定义属性（如length、atleast）
#   7. try/except/else：完整异常处理流程（捕获、处理、无异常时执行）
#   8. raise关键字：主动抛出异常
#   9. datetime模块：获取当前时间、strftime()格式化时间字符串
#  10. JSON模块：dumps()序列化为JSON格式字符串，indent参数美化输出
# ====================================================================

# ----------------------------------------------------
# 练习1：文件IO——随机生成50个数字写入文件，排序后写入另一个文件
# 流程：生成随机数 → 写入 a.txt → 读取并排序 → 降序写入 b.txt
# writelines() 接收字符串列表；readlines() 返回每行字符串列表（含\n）
# ----------------------------------------------------
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
# with open ('b.txt','w') as f2:
#     b.sort()
#     for i in b[::-1]:          # 倒序 = 降序
#         b_.append(str(i)+'\n')
#     print(b_)
#     f2.writelines(b_)
#     print('数据排序成功保存在b.txt')


# ----------------------------------------------------
# 练习2：os模块——查看当前目录下的文件和子目录信息
# getcwd() 获取当前工作目录
# listdir() 列出当前目录所有文件和文件夹名
# path.isfile() 判断是否为文件
# .endswith('.py') 判断文件扩展名
# ----------------------------------------------------
# import os
# a=os.getcwd()
# b=os.listdir(os.getcwd())
# for i in os.listdir(os.getcwd()):
#     print("是否文件",os.path.isfile(i))
#     print('是否是.py',i.endswith('.py'))
#     print()
# print(a,b,sep='\n')


# ----------------------------------------------------
# 练习3：os.walk()——递归遍历目录树
# os.walk() 是一个生成器，每次返回 (root, dirs, files) 三元组
# root 是当前目录路径，dirs 是子目录列表，files 是文件列表
# os.path.join(root, name) 拼接完整路径
# ----------------------------------------------------
# import os
# print(os.listdir('.'))  # 当前目录所有文件和子目录
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


# ----------------------------------------------------
# 练习4：os.walk() + os.stat()——统计文件夹大小和文件/文件夹数量
# os.stat(file_path).st_size 获取文件大小（字节）
# 统计指标：totalSize（总大小）、fileNum（文件数）、dirNum（子文件夹数）
# ----------------------------------------------------
# totalSize,fileNum,dirNum=0,0,0
# for root, dirs, files in os.walk("shixv"):
#     print(f"当前目录: {root}")
#     print(f"子目录: {dirs}")
#     print(f"文件: {files}")
#     for i in files:
#         totalSize+=(os.stat(os.path.join(root,i))).st_size
#     fileNum+=len(files)
#     dirNum+=len(dirs)
# print()
# print(f"文件夹大小：{totalSize}字节,文件数量：{fileNum},子文件夹数量：{dirNum}")


# ----------------------------------------------------
# 练习5：自定义异常类——ShortInputException
# 继承 Exception，在 __init__ 中添加自定义属性 length 和 atleast
# raise 主动抛出异常，except xxx as e 捕获并使用 e.length/e.atleast
# ----------------------------------------------------
# class ShortInputException(Exception):
#     def __init__(self, length, atleast):
#         Exception.__init__(self)
#         self.length = length
#         self.atleast = atleast
#
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


# ----------------------------------------------------
# 练习6：自定义异常——简单的输入校验
# isdigit() 判断字符串是否全为数字
# raise 自定义异常输出错误提示
# ----------------------------------------------------
# class sb(Exception):
#     pass
#
# a=input()
# if a .isdigit():
#     print(a)
# else:
#     raise sb("出错")


# ----------------------------------------------------
# 练习7：datetime模块——实时显示当前时间
# datetime.now() 获取当前日期时间
# strftime() 自定义格式化：%Y年 %m月 %d日 %H时 %M分 %S秒
# ----------------------------------------------------
# from datetime import datetime
# while(1):
#     now=datetime.now()
#     time=now.strftime('%Y年-%m月-%d日  %H时-%M分-%S秒')
#     # print('\r',now, end='')
#     print(now)
#     print(time, end='')


# ----------------------------------------------------
# 练习8：JSON模块——Python字典序列化为JSON格式字符串
# json.dumps() 将Python对象转为JSON字符串
# indent=4 参数缩进4空格，提高可读性
# ----------------------------------------------------
# import json
# a={
# "company": "Alibab",
# "employees": [{"name": "Alice", "position": "Engineer", "salary": 10000},
#               {"name": "Bob", "position": "Manager", "salary": 15000}],
# "location": "Hangzhou"}
# print(a)
# print(json.dumps(a,indent=4))


# ====================================================================
# 阶段3：Python 网络编程
#
# 【学了什么】
#   1. requests库：第三方HTTP请求库，简化网络请求操作
#   2. GET请求：requests.get(url, params) 发送带参数的GET请求
#   3. 响应处理：status_code（状态码）、headers（响应头）、url（最终URL）、
#      json()（解析JSON响应体）、elapsed.total_seconds()（请求耗时）
#   4. API调用实践：调用高德地图天气API获取实时天气和天气预报
#   5. API参数构造：key（API密钥）、city（城市名/adcode）、extensions（base/all）
#   6. JSON数据提取：从多层嵌套的JSON中提取天气预报数据
# ====================================================================

# ----------------------------------------------------
# 练习1：requests库基础——发送带参数的GET请求
# 访问 httpbin.org/get 测试 API（httpbin 是 HTTP 测试服务）
# requests.get(url, params=dict) 将字典转为URL查询参数
# .json() 直接将响应体解析为Python字典
# .elapsed.total_seconds() 获取请求耗时（秒）
# ----------------------------------------------------
# import requests
#
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


# ----------------------------------------------------
# 练习2：高德地图天气API——获取实时天气 + 4天预报
# extensions="base" 只获取实况天气
# extensions="all"  获取实况天气 + 4天预报
# 从 res["forecasts"][0]["casts"] 提取每日天气预报数据
# ----------------------------------------------------
# import requests
# import json
#
# API_KEY = "2d281b9a960c62d33574b51d88344123"
# city = "新余"  # 城市 adcode，110000 = 北京
#
# url = "https://restapi.amap.com/v3/weather/weatherInfo" # 天气查询接口
# params = {"key": API_KEY, "city": city, "extensions": "all"}
# res = requests.get(url, params=params)
# print(json.dumps(res.json(),indent=4))
# res=res.json()
#
# def get_weather(key, city):
#     url = "https://restapi.amap.com/v3/weather/weatherInfo"
#
#     # 实况天气
#     params = {"key": key, "city": city, "extensions": "base"}
#     res = requests.get(url, params=params).json()
#     if res["status"] == "1":
#         live = res["lives"][0]
#         print(f"实况: {live['weather']}, {live['temperature']}°C, {live['winddirection']}风{live['windpower']}级, 湿度{live['humidity']}%")
#     else:
#         print(f"实况请求失败: {res['info']}")
#
#     # 天气预报（4天）
#     params["extensions"] = "all"
#     res = requests.get(url, params=params)
#     res=res.json()
#
#     if res["status"] == "1":
#         print("\n预报:")
#         for day in res["forecasts"][0]["casts"]:
#             print(f"  {day['date']}: {day['dayweather']}, {day['nighttemp']}°C ~ {day['daytemp']}°C")
#     else:
#         print(f"预报请求失败: {res['info']}")
#
# get_weather(API_KEY, city)


# ====================================================================
# 阶段4：Python 面向对象编程（OOP）
#
# 【学了什么】
#   1. 类的定义与实例化：class 关键字定义类，通过 类名() 创建实例
#   2. self参数：代表实例自身，在方法定义中必须作为第一个参数
#   3. __init__()构造方法：创建对象时自动调用，用于初始化实例属性
#   4. 类属性 vs 实例属性：类属性所有实例共享，实例属性各自独立
#   5. @classmethod类方法：第一个参数是 cls（类本身），可通过类名调用
#   6. 继承（Inheritance）：子类继承父类的属性和方法
#   7. 方法重写（Override/多态）：子类重新定义父类的方法
#   8. 封装（Encapsulation）：以 __ 开头的属性变为私有，外部无法直接访问
#   9. 综合实践：银行账户管理系统（开户、查余额、存款、取款、改密码）
# ====================================================================

# ----------------------------------------------------
# 练习1：类的最基本定义——Student类
# 定义一个方法 aa()，用 self.name/self.age/self.score 设置实例属性
# 注意：duanhaoyu 是局部变量，不是实例属性，外部无法通过 s.duanhaoyu 访问
# ----------------------------------------------------
# class Student:
#     def aa(self, name, age, score):
#         self.name = name
#         self.age = age
#         self.score = score
#         duanhaoyu=100
#
# s=Student()
# s.aa("张三",18,90)
# print(s.name)
# # print(s.duanhaoyu)  # 会报错，因为是局部变量


# ----------------------------------------------------
# 练习2：类属性 vs 实例属性——Car类
# color='白色' 是类属性，所有实例共享默认值
# c.color='红色' 是给实例 c 添加/覆盖实例属性（不影响类属性）
# ----------------------------------------------------
# class Car:
#     color='白色'
#     def run (self):
#         print(f"一辆{self.color}的汽车在跑")
#
# c=Car()
# c.run()           # 输出：一辆白色的汽车在跑
# c.color='红色'
# c.run()           # 输出：一辆红色的汽车在跑


# ----------------------------------------------------
# 练习3：__init__()构造方法 + @classmethod类方法——Rectangle类
# __init__() 在创建对象时自动调用，初始化 width 和 height
# @classmethod create_square()：类方法接收 cls（类本身），
#   返回 cls(side, side) 创建正方形实例（宽=高）
# ----------------------------------------------------
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_area(self):
#         return self.width * self.height
#
#     def get_perimeter(self):
#         return 2 * (self.width + self.height)
#
#     @classmethod
#     def create_square(cls, side_length):
#         return cls(side_length, side_length)
#
# r=Rectangle(5,3)
# print("面积：",r.get_area(),"周长：",r.get_perimeter())
#
# r2=Rectangle.create_square(4)
# print("面积：",r2.get_area(),"周长：",r2.get_perimeter())


# ----------------------------------------------------
# 练习4：继承与多态——Shape基类 + Square/Circle子类
# Shape 定义通用接口 get_area() 和 aa() 测试方法
# Square 和 Circle 继承 Shape，并各自重写 get_area()
# 多态：同一方法名在不同子类中有不同实现
# 子类自动继承父类中未重写的方法（如 aa()）
# ----------------------------------------------------
# class Shape ():
#     def get_area(self):
#         return 0
#
#     def aa(self):
#         return print("测试成功！")
#
# class Square (Shape):
#     def __init__(self, side_length):
#         self.side_length = side_length
#
#     def get_area(self):
#         return self.side_length * self.side_length
#
# class Circle (Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def get_area(self):
#         return 3.14 * self.radius * self.radius
#
# s1=Square(5)
# s2=Circle(3)
# print(s1.get_area())      # 25
# print(s2.get_area())      # 28.26
# print(s1.get_area()+s2.get_area())
# s1.aa()  # 继承自 Shape
# s2.aa()


# ----------------------------------------------------
# 练习5：封装——银行账户系统 Attributes类
# 以 __ 开头的属性（__password, __balance）变为私有属性
# 外部无法直接访问，必须通过类方法 查/存/取/改密码 来操作
# 封装优势：保护敏感数据，通过方法控制访问逻辑（如密码验证）
# ----------------------------------------------------
# class Attributes ():
#     def __init__(self,account_id,name):
#         self.account_id=account_id
#         self.name=name
#
#     def kaihu(self,account_id,password,name,balance):
#         self.account_id=account_id
#         self.__password=password          # 私有属性：密码
#         self.name=name
#         self.__balance=balance            # 私有属性：余额
#         return print('开户成功')
#
#     def cha(self,password):               # 查余额：需验证密码
#         if self.__password==password :
#             return print('金额为:',self.__balance)
#         else:
#             return print('密码错误')
#
#     def cun(self,password,balance):        # 存款：需验证密码
#         if self.__password==password:
#             self.__balance+=balance
#             return print('存款成功，现在金额为:',self.__balance)
#         else:
#             return print('存款失败')
#
#     def qv(self,password,balance):         # 取款：需验证密码
#         if self.__password==password:
#             self.__balance-=balance
#             return print('取款成功，现在金额为:',self.__balance)
#         else:
#             return print('取款失败')
#
#     def xiou(self,password,newpassword):   # 修改密码：需先验证旧密码
#         if self.__password==password:
#             self.__password=newpassword
#             return print('修改成功')
#         else:
#             return print('修改失败')

# ----------------------------------------------------
# 银行账户系统——命令行交互主循环
# while(1) 无限循环直到用户选择 "6.退出"
# 菜单驱动：根据用户输入调用对应的银行操作
# ----------------------------------------------------
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


# ====================================================================
# 阶段5：Python 数据库编程（pymysql + MySQL）
#
# 【学了什么】
#   1. SQL语句编写：CREATE TABLE建表、INSERT插入、SELECT查询、
#      UPDATE更新、DELETE删除
#   2. 数据类型：INT PRIMARY KEY AUTO_INCREMENT、VARCHAR、DECIMAL
#   3. pymysql基本操作：connect()连接、cursor()获取游标、execute()执行
#   4. 事务控制：commit()提交、隐式事务
#   5. 参数化查询：%s 占位符防止SQL注入
#   6. 批量操作：executemany() 一次执行多条INSERT
#   7. 数据库封装：DBHelper 基类封装连接/游标/执行/查询方法
#   8. 业务封装：UserManager 业务类封装CRUD操作（增删改查）
#   9. 依赖注入：UserManager 接收 DBHelper 实例，实现解耦
#  10. 数据可视化：show_table() 以 MySQL 命令行格式展示数据表
#  11. 数据还原：reset_table() 清空表并重新插入备份数据
# ====================================================================

# ----------------------------------------------------
# SQL 建表语句（参考，在 MySQL 命令行中执行）
# employees 表：包含员工编号、姓名、薪水、职位、部门、入职日期、性别
# ----------------------------------------------------
# -- CREATE TABLE employees (
# --     emp_id INT PRIMARY KEY AUTO_INCREMENT COMMENT '员工编号',
# --     name VARCHAR(20) NOT NULL COMMENT '员工姓名',
# --     salary DECIMAL(10,2) COMMENT '薪水',
# --     position VARCHAR(20) COMMENT '职位',
# --     department VARCHAR(20) COMMENT '部门',
# --     entry_date DATE COMMENT '入职日期',
# --     gender CHAR(1) COMMENT '性别'
# -- ) COMMENT='员工信息表';
#
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
# 功能：封装 pymysql 的底层连接、游标和基础操作
# 方法：
#   connect()    — 建立数据库连接并获取游标
#   close()      — 关闭游标和连接
#   execute()    — 执行增删改 SQL，自动 commit
#   query()      — 执行查询 SQL，返回全部结果
#   query_one()  — 执行查询 SQL，返回单条结果
# ============================================================
class DBHelper:
    """数据库操作基类，封装 pymysql 连接与基础操作"""

    def __init__(self, host="127.0.0.1", port=3306, user="root",
                 password="123456", database="gs"):
        """初始化数据库连接参数，不立即连接"""
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
        """关闭游标和连接（释放资源）"""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def execute(self, sql, params=None):
        """执行增删改 SQL，自动 commit 提交事务，返回受影响行数"""
        if params:
            rows = self.cursor.execute(sql, params)
        else:
            rows = self.cursor.execute(sql)
        self.conn.commit()
        return rows

    def query(self, sql, params=None):
        """执行查询 SQL，返回 fetchall() 全部结果"""
        if params:
            self.cursor.execute(sql, params)
        else:
            self.cursor.execute(sql)
        return self.cursor.fetchall()

    def query_one(self, sql, params=None):
        """执行查询 SQL，返回 fetchone() 单条结果"""
        if params:
            self.cursor.execute(sql, params)
        else:
            self.cursor.execute(sql)
        return self.cursor.fetchone()


# ============================================================
# UserManager 用户管理类（依赖 DBHelper）
# 功能：封装用户表 users 的 CRUD 操作
# 方法：
#   add_user(name, email)       — 新增单个用户
#   batch_add_users(user_list)  — 批量新增用户
#   get_user_by_id(user_id)     — 根据 ID 查询用户
#   update_user_email(id, email)— 更新用户邮箱
#   delete_user(user_id)        — 删除用户
#   list_all()                  — 列出所有用户
#   show_table()                — MySQL命令行格式可视化展示
#   reset_table(backup_data)    — 还原表数据（清空+重新插入）
#   disconnect()                — 断开数据库连接
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
        self._ensure_table()  # 确保 users 表存在

    def _ensure_table(self):
        """私有方法：确保 users 表存在，不存在则创建"""
        sql = """
        CREATE TABLE IF NOT EXISTS users (
            id INT PRIMARY KEY AUTO_INCREMENT COMMENT '用户编号',
            name VARCHAR(50) NOT NULL COMMENT '用户名',
            email VARCHAR(100) COMMENT '邮箱'
        ) COMMENT='用户信息表'
        """
        self.db.execute(sql)

    # ---- CRUD（增删改查）操作 ----

    def add_user(self, name, email):
        """
        新增单个用户
        %s 占位符传递参数，防止 SQL 注入
        """
        sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
        self.db.execute(sql, (name, email))
        print(f"新增用户成功：{name}，邮箱：{email}")

    def batch_add_users(self, user_list):
        """
        批量新增用户
        executemany() 一次执行多条数据，效率远高于循环单条插入
        :param user_list: [(name, email), ...] 元组列表
        """
        sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
        rows = self.db.cursor.executemany(sql, user_list)
        self.db.conn.commit()
        print(f"批量新增 {rows} 条用户数据成功")
        return rows

    def get_user_by_id(self, user_id):
        """根据 ID 查询单个用户，使用 query_one 返回单条记录"""
        sql = "SELECT * FROM users WHERE id = %s"
        result = self.db.query_one(sql, (user_id,))
        if result:
            print(f"查询结果：ID={result[0]}, 姓名={result[1]}, 邮箱={result[2]}")
        else:
            print(f"未找到 ID={user_id} 的用户")
        return result

    def update_user_email(self, user_id, new_email):
        """更新用户邮箱，返回受影响行数判断是否成功"""
        sql = "UPDATE users SET email = %s WHERE id = %s"
        rows = self.db.execute(sql, (new_email, user_id))
        if rows:
            print(f"用户 ID={user_id} 邮箱已更新为：{new_email}")
        else:
            print(f"更新失败：未找到 ID={user_id} 的用户")

    def delete_user(self, user_id):
        """删除指定 ID 的用户"""
        sql = "DELETE FROM users WHERE id = %s"
        rows = self.db.execute(sql, (user_id,))
        if rows:
            print(f"用户 ID={user_id} 已删除")
        else:
            print(f"删除失败：未找到 ID={user_id} 的用户")

    def list_all(self):
        """查询并打印所有用户"""
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
        """
        以 MySQL 命令行表格格式可视化展示数据
        实现原理：
          1. 获取列名（cursor.description）
          2. 计算每列最大宽度（动态列宽）
          3. 用 +---+ 绘制分隔线
          4. 用 | data | 绘制数据行
        """
        sql = "SELECT * FROM users"
        self.db.cursor.execute(sql)
        results = self.db.cursor.fetchall()
        col_names = [desc[0] for desc in self.db.cursor.description]

        if not results:
            print("Empty set")
            return

        # 计算各列最大宽度（取列名和数据两者中的较大值）
        col_widths = []
        for i, name in enumerate(col_names):
            max_w = len(name)
            for row in results:
                max_w = max(max_w, len(str(row[i])))
            col_widths.append(max_w)

        # 分隔线：+------+------+------+
        sep = "+" + "+".join("-" * (w + 2) for w in col_widths) + "+"

        # 表头行：| id | name | email |
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
        """
        还原表内数据：清空表、重置自增ID、重新插入备份数据
        :param backup_data: [(name, email), ...] 原始数据列表
        """
        self.db.execute("DELETE FROM users")
        self.db.execute("ALTER TABLE users AUTO_INCREMENT = 1")
        if backup_data:
            self.batch_add_users(backup_data)
        print("数据表已还原")

    def disconnect(self):
        """主动断开数据库连接，释放资源"""
        self.db.close()
        print("数据库连接已关闭")


# ============================================================
# 测试代码 —— 演示 DBHelper + UserManager 的完整使用流程
# 执行流程：
#   1. 创建 DBHelper → 2. 依赖注入到 UserManager → 3. 批量插入12条数据
#   4. 可视化展示 → 5. 数据还原 → 6. 单条增删改查测试 → 7. 断开连接
# ============================================================
if __name__ == "__main__":
    # 1. 创建 DBHelper 实例（连接 MySQL 数据库）
    db = DBHelper(host="127.0.0.1", port=3306, user="root",
                  password="123456", database="gs")

    # 2. 依赖注入：将 DBHelper 实例传给 UserManager
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

    # 4. 数据还原（清空表并重新插入），验证 reset_table() 功能
    um.reset_table(sample_users)
    um.show_table()

    # 5. 测试单条增删改查
    um.add_user("张三", "zhangsan@example.com")
    um.add_user("李四", "lisi@example.com")
    um.show_table()

    um.get_user_by_id(1)                          # 查用户1
    um.update_user_email(1, "zhangsan_new@example.com")  # 改邮箱
    um.get_user_by_id(1)                          # 再次查询验证修改
    um.delete_user(2)                             # 删用户2

    # 6. 断开数据库连接
    um.disconnect()
