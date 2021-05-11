# -*- coding:utf-8 -*-
#i.	定义了一个学生类：属性:学号，姓名，年龄，性别，身高，体重，成绩，家庭地址，电话号码。行为：学习（要求参数传入学习的时间），玩游戏（要求参数传入游戏名），编程（要求参数传入写代码的行数），数的求和（要求参数用变长参数来做，返回求和结果）
class studen:
    xhao=""
    name=""
    age=0
    xingb=""
    shenggao=0
    tiz=0
    chengji=0
    zhuzhi=""
    dianhua=0
    def xuexi(self,time):
        print("我在学习，时间为",time)
    def youxi(self,game):
        print("游戏名字为", game)
    def bianchen(self,hanshu):
        print("我在打代码，代码的行数为",hanshu)
    def sum(self,*num):
        print(*sum)
        a=0
        for i in num:
            a=a+i
        print(a)
  #  def sum(self):(变长参数不会）
  #ii.	车类：属性：车型号，车轮数，车身颜色，车重量，油箱存储大小 。功能：跑（要求参数传入车的具体功能，比如越野，赛车）创建：法拉利，宝马，铃木，五菱，拖拉机对象
s=studen()
s.xhao=1234567
s.name="kk"
s.age=34
s.xingb="男"
s.shenggao=190
s.tiz=140
s.chengji=100
s.dianhua=189237737
s.xuexi(2)
s.youxi(111)
s.bianchen(333)


class cat:
    xinhao=""
    chelun=0
    yanse=""
    zhong=0
    youxiang=0
    def gongn(self,gn):
        print("此车功能为",gn)
c=cat()
c.xinhao="法拉利"
#iii.	笔记本：属性：型号，待机时间，颜色，重量，cpu型号，内存大小，硬盘大小。  行为：打游戏（传入游戏的名称）,办公。
class notebook:
    xinghao=""
    daji=0
    yanse=""
    zhonglaing=""
    cpu=""
    ncun=""
    yingban=""
    def youxi(self,youxiname):
        print("我在打",youxiname,"游戏")
    def work(self,work1):
        print("我在用",work1,"工作")
#iv.	猴子类：属性：类别，性别，身体颜色，体重。行为：造火（要求传入造火的材料：比如木棍还是石头），学习事物（要求参数传入学习的具体事物，可以不止学习一种事物）
class houzi:
    leibie=""
    xingb=""
    yanse=""
    tizhong=""
    def zaohuo(self,cailiao):
        print("猴子要造火用到",cailiao)
    def xuexi(self,xxi,xxx9):
        print("猴子学习用到",xxi,xxx9)