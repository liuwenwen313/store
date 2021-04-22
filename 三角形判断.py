A=input("请输入三角形A边长度：")
B=input("请输入三角形B边长度：")
C=input("请输入三角形C边长度：")
A=int(A)
B=int(B)
C=int(C)
if A+B>C and A+C>B and C+B>A:
    if A==B or  B==C or A==C:
        print("该三角形为等腰三角形")
    elif A==B==C:
        print("该三角形为等边三角形")
    elif A*A+B*B==C*C or C*C+B*B==A*A or A*A+C*C==B*B:
              print("该三角形为直角三角形")
    else:
                print("该三角形为普通三角形")
else:
    print("不能构成三角形")

