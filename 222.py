def aa(x):
    a= "A" if 90<=x<=100 else ("B" if 60<=x<90 else ("C" if 0<=x<60 else "错误"))
    return a

def bb(x):
    for  i in x:
        if i not in "0123456789":
            return 0
    return 1

c=dict()
ku=[["学生","成绩"]]
yonghu=input("""
        0-退出
        1-输入学生姓名和成绩
        2-评级所有学生成绩
        请选择0/1/2：""")
while(yonghu):
    if yonghu=="0":
        break
    elif yonghu=="1":
        xingming=input("请输入学生姓名：")
        chengji=input("请输入学生成绩：")
        while(chengji):
            if bb(chengji) :
                break
            chengji=input("输入非法,请重新输入学生成绩：")
        chengji=int(chengji)
        ku.append([xingming,chengji])
        print("添加成功！")
    elif yonghu=="2":
        print(ku[0][0],ku[0][1])
        for i in range(1,len(ku)):
            print(ku[i][0],ku[i][1],aa(ku[i][1]))

    else:
        print("输入不合法，请重新输入")
    yonghu=input("""
        0-退出
        1-输入学生姓名和成绩
        2-评级所有学生成绩
        请选择0/1/2：""")

print("退出完毕！")


