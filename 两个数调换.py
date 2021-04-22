A=56
B=78
P=0
num=input("请输入+或者-：")
if num=="+" or num=="-":
    P=A
    A=B
    B=P
    print("A输出结果为",A,"B输出结果为",B)
else:
    print("输入不正确哦！！！！！！")
