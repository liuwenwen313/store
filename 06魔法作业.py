#现在有这样一个叫scores.txt的文件，里面有赫敏、哈利、罗恩、马尔福四个人的几次魔法作业的成绩。但是呢，因为有些魔法作业有一定难度，教授不强制同学们必须上交，所以大家上交作业的次数并不一致。
#罗恩 23 35 44
####希望你来统计这四个学生的魔法作业的总得分，然后再写入一个txt文件。
#-*- coding:gbk-*-

num=0
s=open(file="scores.txt",mode="r+",encoding="GBK")
s2=open(file="sum.txt",mode="w+",encoding="GBK")
score=s.readlines()
for i in score:
    qg=i.replace("\n","").split(",")
    for i in qg:
        qg2 = i.replace(" ",",").split(",")
        name=qg2[0]
        del qg2[0]
        for i in qg2:
            i=int(i)
            num=num+i
        s2.write(name)
        s2.write(str(num))
        s2.write("\n")
s.close()
s2.close()
