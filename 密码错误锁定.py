count =0

while True:
    count =count+1
    a = input("请输入用户名：")
    b = input("请输入密码：")
    if count<=3:
        print("密码错误，请再次输入")
    else:
        print("锁定")
        break
