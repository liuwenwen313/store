list = [1,2,3,4,5,6,7,8,9]
list2=[]
a=0
while a<len(list):
    a = a + 1
    list2.insert(a,list[len(list)-a])
print(list2)