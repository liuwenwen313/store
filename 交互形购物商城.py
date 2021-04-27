import random
n=0
shop=[
    [0,"三只松鼠辣条大礼包",600],
    [1,"lenovo thinkpad e580",5000],
    [2,"蟹黄锅巴",200],
    [3,"运动小白鞋",300],
    [4,"ysl复古小黑包",18000],
    [5,"雅诗兰黛粉底液",450],
    [6,"流心蛋黄酥",70],
    [7,"可爱小猪毛绒玩具",100],
    [8,"草莓味蛋糕",100],
]
#1.优惠券
youhui=[
    [0,10],
    [1,20],
]
myq=[]
if youhui[0][1]>=0 or youhui[1][1]>0:
  q=random.randint(1,2)
  if q==1:
    youhui[0][1]=youhui[0][1]-1
    myq.append(youhui[0])
    print("恭喜获得辣条满600减300")
  elif q==2:
       youhui[1][1]=youhui[1][1]-1
       myq.append(youhui[1])
       print("恭喜获得电脑半折券")
else:
    print("优惠已经没有了")
print("剩余辣条券",youhui[0][1])
print("剩余电脑券",youhui[1][1])
print("我的券包有以下",myq)
## 2.初始化自己的薪资
salary=input("请输入你的钱包余额：")
if salary.isdigit():
   salary=int(salary)
else:
    print("请输入正确钱数")
###3.我的购物车
mycart=[]
##4.展示商品
while True:
    for index,value in enumerate(shop):
      print(index,value )
      # 4.输入要买的编号:num 是商品编号
    num=input("请输入你要购买的商品编号：")
    if num.isdigit():
       num=int(num)
       if num>len(shop):
           print("商品不存在")
       else:
           if salary>=shop[num][2]:
               mycart.append(shop[num])  # 添加购物车
               print("已经将",shop[num][1],"放进你的购物车，您的余额为",salary)
               if num==0 and myq[0][0]==shop[0][0]:
                  while True:
                        m=input("请选择是否使用优惠券，0为不使用 ，1为使用优惠券：")
                        if m.isdigit():
                          m=int(m)
                          if m==0:
                           print("原价购买，我有钱")
                           break
                          elif m==1:
                            shop[num][2]=shop[num][2] - 300
                            break
                        else:
                         print("您输入非法")
               elif num == 1 and myq[0][0]==shop[1][0]:
                   while True:
                         m = input("请选择是否使用优惠券，0为不使用 ，1为使用优惠券：")
                         if m.isdigit():
                            m=int(m)
                            if m== 0:
                                print("原价购买，我有钱")
                                break
                            elif m== 1:
                                shop[num][2] = shop[1][2] / 2
                                break
                         else:
                           print("您输入非法了")
               else:
                  print("没有任何优惠")
               salary = salary - shop[num][2]
           else:
               print("您的余额不够购买哦，钱包需要鼓起来！！！")
           n = n + shop[num][2]
    elif num=="q" or num=="Q":
       print("将离开商城，期待你下次再来")
       break
    else:
       print("您输入非法，请重新输入")
#打印购物小票
print("您购物商品如下：")
for index,value in enumerate(mycart):
    print(index, "  ", value)
print("您的余额为：", salary,"您的积分为",n/10)

