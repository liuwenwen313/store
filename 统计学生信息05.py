students = [
    {'name':'张三','age':23,'score':88,'tel':'23423532','gender':'男'},
    {'name':'李四','age':26,'score':80,'tel':'12533453','gender':'女'},
    {'name':'王五','age':15,'score':58,'tel':'56453453','gender':'男'},
    {'name':'赵六','age':16,'score':57,'tel':'86786785','gender':'保密'},
    {'name':'小明','age':18,'score':98,'tel':'23434656','gender':'女'},
    {'name':'小红','age':23,'score':72,'tel':'67867868','gender':'女'},
]
#1.统计没有及格的学生
c=0
for i,m in enumerate(students):
    score=students[i]["score"]
    if score<60:
       c= c+1
print("没有及格的学生有",c,"名")

#"2.统计未成年的学生
num1=0
for i,m in enumerate(students):
    age=students[i]["age"]
    if age<18:
        num1=num1+1
print("未成年的学生有",num1,"名")
#3.统计手机尾号是8的学生
num2=0
name=0

for i,m in enumerate(students):
    tel = students[i]["tel"]
    if tel.endswith("8"):
        name=(students [i]["name"])
        num2=num2+1
print("手机尾号是8的学生有",num2,"名是",name)
#4	打印最高分和对应的学生的名字
max=students[i]["score"]
name1=0
for i,m in enumerate(students):
    if max<=students[i]["score"]:
        name1=(students [i]["name"])
        max=students[i]["score"]
print("最高分",max ,name1)
#5)	将列表按学生成绩从大到小排序
s=[]
#for i,m in enumerate(students):
   # score1 = students[i]["students"]
   # if score1<=students[i]["score"]:
     #   s.append(m)
     #   students.remove(m)
     #   print(s)
#print(m)
#sorted_students = sorted(students, key=lambda students : students['name'], reverse=True )
#print("排序",students)
import operator
sorted_students = sorted(students, key=operator.itemgetter('score'), reverse=True)
print(sorted_students)

#6删除保密学生
for i,n in enumerate(students):
    if students[i]["gender"]=="保密":
        del students[i]
    else:
     print(students[i])