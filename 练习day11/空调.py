# -*- coding:utf-8 -*-
class airconditioning:
# 1、空调有品牌和价格两个属性，并且将属性私有化，提供公有的getXxx与setXxx方法
    __price=0
    __brand=""
    def setPrice(self,price):
        self.__price=price
    def getPrice(self):
        return self.__price
    def setBrand(self,brand):
        self.__brand=brand
    def getBrand(self):
        return  self.__brand

# 2、提供一个无返回值的无参数的开机的方法，内容打印一句话：“空调开机了...”；
    def open(self):
        print("空调开机了")

# 3、提供一个无返回值的带1个int类型参数的定时关机的方法,(int类型的参数表示设定的分钟数)，内容打印一句话：“空调将在xxx分钟后自动关闭...”；
    def close(self,time):
        time=int(time)
        print("空调在",time,"分钟之后自动关闭")


# 5、使用空调对象获取空调的品牌和价格并打印到控制台上；
    def kongtiao(self):
        print("品牌:",self.__brand,"价格:",self.__price)

# 4、在测试类中创建出空调对象，并给空调的品牌和价格赋任意值；
a=airconditioning()
a.setPrice(10000)
a.setBrand("格力")
a.kongtiao()
a.open()
a.close(60)


