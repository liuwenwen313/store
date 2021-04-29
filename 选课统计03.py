#语文 = ['小明','小张','小黄','小杨']
#数学 = ['小黄','小李','小王','小杨','小周']
#英语 = ['小杨','小张','小吴','小冯','小周']
chine = ['小明','小张','小黄','小杨']
math = ['小黄','小李','小王','小杨','小周']
english = ['小杨','小张','小吴','小冯','小周']
#1)	求选课学生总共有多少人
Q=[]
for i in chine:
    Q.append(i)
for i in math:
    Q.append(i)
for i in english:
    Q.append(i)
Q=set (Q)
print("Q")
num=len(Q)
print("选课学生一共",num,"人")
##2)	求只选了第一个学科的人的数量和对应的名字
q=[]
num2=0
for i in math:
    q.append(i)
for i in english:
    q.append(i)
for i in chine:
   if i not in q:
    num2=num2+1
    print("只选了一个学科数量",num2,"对应名字有",i)

#3)	求只选了一门学科的学生的数量和对应的名字
num3=0
w=[]
w2=[]
for i in chine:
    w.append(i)
for i in math:
    w.append(i)
for i in english:
    w.append(i)
for  i in w :
    count=w.count(i)
    if count <= 1:
        w2.append(i)
        num3=num3+1
print("只选了一门课有",num3,"个选了一门课,分别是",w2)
