import time
class Oldphone:
    __brand=""
    def setBrand(self,brand):
        self.__brand=brand
    def getBrand(self):
        return self.__brand
    def callway(self,name):
        print(self.__brand,"正在给",name,"打电话")
class Newphone(Oldphone):
    def callway(self,name):
        for i in range(2):
            time.sleep(1)
            print("语言拨号中",".",end="")
        super().callway(name)
    def showway(self):
        print(self.getBrand(),"的手机很好用")
old=Oldphone()
old.setBrand("华为")
old.callway("程程")
new=Newphone()
new.callway("米")
new.setBrand("华为")
new.showway()



