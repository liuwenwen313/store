# _#_ coding:utf-8 _*
#开发情景：
#面包店：
#6个厨师在同时做面包，做完扔进篮子里
#5个窗口有5个人抢买面包
#面包篮子只能存300个
#厨师发现满了就停3秒然后继续
#跑五分钟时间统计厨师总共做了多少个顾客买了多少个，一个十块钱，每个顾客付了多少钱
from threading import  Thread
import time
t=0
cumas=0
he = 0
class Clock(Thread):
    def run(self) -> None:
        global t
        while t<300:
            time.sleep(1)
            t=t+1

class Cook(Thread):
    cookname=""
    count=0
    def run(self) -> None:
        global cumas
        global he
        while t<300:
            if cumas>=300:
                print("篮子满了")
                time.sleep(3)
            else:
                cumas=cumas+1
                self.count=self.count+1
                he = he +1
        else:
            print("时间到.",self.cookname,"做了",self.count,"六个人一个做了",he)
            time.sleep(3)

class Cliant(Thread):
        cliantname=""
        count1=0
        #money=0
        def run(self) -> None:
            global cumas

            while t<300:
                if cumas>0:
                    cumas=cumas-1
                    self.count1=self.count1+1
                    #money=self.count1*10+money
            else:

                print("时间到",self.cliantname,"买了",self.count1,"付了",self.count1*10)
                time.sleep(2)


c=Clock()
c1=Cook()
c2=Cook()
c3=Cook()
c4=Cook()
c5=Cook()
c6=Cook()
c1.cookname="厨师1"
c2.cookname="厨师2"
c3.cookname="厨师3"
c4.cookname="厨师4"
c5.cookname="厨师5"
c6.cookname="厨师6"
cl1=Cliant()
cl2=Cliant()
cl3=Cliant()
cl4=Cliant()
cl5=Cliant()
cl1.cliantname="顾客1"
cl2.cliantname="顾客2"
cl3.cliantname="顾客3"
cl4.cliantname="顾客4"
cl5.cliantname="顾客5"
c.start()
c1.start()
c2.start()
c3.start()
c4.start()
c5.start()
c6.start()
cl1.start()
cl2.start()
cl3.start()
cl4.start()
cl5.start()