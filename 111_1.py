import random


def ss():
    lines = ['Line 1\n', 'Line 2\n', 'Line 3\n'] 
    xing=['赵','钱','孙','李','周','吴','郑','王',
        '冯','陈','褚','卫','蒋','沈','韩','杨',
        '朱','秦','尤','许','何','吕','施','张',
        '孔','曹','严','华','金','魏','陶','姜']
    xing_n=len(xing)

    ming=['伟','芳','娜','敏','静','强',
        '磊','军','洋','勇','艳','杰',
        '涛','明','超','秀','霞','平',
        '刚','莉','丽','浩','鑫','波',
        '婷','雷','鹏','欣','宇','晨',
        '悦','佳','豪','博','雯','琪',
        '宁','彤','轩','然','雨桐 ','子涵 ',
        '浩然','一诺 ','欣怡','梓涵 ','俊宇',
        '雨泽','诗涵 ','语桐','思睿 ','佳琪',
        '梦瑶','晨曦 ','子轩','博文 ','雨萱',
        '俊豪','若曦 ','沐辰','嘉怡 ','泽宇',
        '婉婷','思琪 ','奕辰','依诺 ','雨欣',
        '子墨','锦程 ','书瑶','佳宁 ','浩然',
        '清妍','星瑶 ','景琛','知夏 ','慕言',
        '晚晴','安禾 ','云舒']
    ming_n=len(ming)


    s=""



    _set=set()
    with open('student1.txt', 'w') as file:
        for i in range(10000):
            _="姓名："
            xingming=str(xing[random.randint(0,xing_n-1)]) \
                +str(ming[random.randint(0,ming_n-1)])            
            chengji="\t"+"成绩："+str(random.randint(0,100))+"\n"
            
            if xingming not in _set:
                if len(xingming)<=2:
                    s=s+_+xingming+"  "+chengji
                else:
                    s=s+_+xingming+chengji

                _set=_set | {xingming}

        file.writelines(s)
    return

ss()