
# -*- coding:utf-8 -*-
class people:
    name=""
    sex=""
    age=""
    huafei=0
    paizi=""
    dianchi=""
    pingmu=""
    daji=""
    jifeng=0
    def duanxing(self,nr):
        print("您发送了一条短信",nr)
    def dadianhua(self,haoma,time):
        if haoma!="" :
            if self.huafei>1:
               print("电话拨号成功")
               if time<10:
                   self.huafei=self.huafei-time*1
                   self.jifeng=self.jifeng+time*15
                   print(self.huafei, self.jifeng)
               elif 10<time<20:
                   self.huafei=self.huafei-time*0.8
                   self.jifeng = self.jifeng + time * 39
                   print(self.huafei,self.jifeng)
               else:
                   self.huafei=self.huafei-time*0.65
                   self.jifeng = self.jifeng + time * 48
                   print(self.huafei, self.jifeng)
            else:
                print("您话费不足")
        else:
            print("您输入号码为空")
p=people()
p.huafei=8
p.dadianhua(10,10)


