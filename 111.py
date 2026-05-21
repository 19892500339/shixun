
'''学生管理系统
		1. 获取学生信息(姓名 分数)
		2. 平均分、最高分、最低分
		3. 把所有学生分级
			90 - 100 ： "A"
			80 - 90  ： "B"
			70 - 80  ： "C"
			60 - 70  ： "D"
			0  - 60  ： "E"
		4. 请把前三个要求以函数的形式实现'''
def aa(student):
    lines=[]
    with open(student, 'r') as file: 
        line = file.readline() 
        while line: 
            lines.append(line)
            line = file.readline()
    return lines

def bb(chengjis):
    _pin=sum(chengjis)/50
    _max=max(chengjis)
    _min=min(chengjis)
    print(f"平均分: {_pin}  最高分: {_max}  最低分: {_min}")

def cc(chengji):
    ji=""
    if chengji<60:
        ji="E"
    elif 60<=chengji<70:
        ji="D"
    elif 70<=chengji<80:
        ji="C"
    elif 80<=chengji<90:
        ji="B"
    elif 90<=chengji<=100:
        ji="A"
    return ji




chengjis=[]
lines=aa("student.txt")
for I in lines:
    if I not in "\n":
        xv=I.index("成绩：")
        chengji=int(I[xv+3:])
        chengjis.append(chengji)
        print(I+" 级别："+cc(chengji))

bb(chengjis)

