import random
shu = random.randint(0,50)
count =0
coin =210
while True:
    count =count + 1
    coin =coin-30
    num1 = input("请输入你猜的数字：")
    num1 = int(num1)
    if count>7:
        print("锁定")
        break
    elif num1 > shu:
        print("您输入的数字大了")
    elif num1 < shu:
        print ("您输入数小了")
    else:
        print("哇偶，yes！！！！")
        break
