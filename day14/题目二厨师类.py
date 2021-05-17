class cook:
    __name=""
    __age=0
    def setName(self,name):
        self.__name=name
    def getName(self):
        return self.__name
    def setAge(self,age):
        self.__age=age
    def getAge(self):
        return self.__age
    def Steamedrice(self,):
        print("首先先加水和米，然后蒸")
class cookway(cook):
    def chao(self):
        print("加菜然后炒")
class cookd(cookway):
    def Steamedrice(self):
        print("首先先加纯净水水和大米，然后蒸半小时")
    def chao(self):
        print("一位大厨叫",self.getName(),"年龄为",self.getAge(),"加肉和菜和调料然后炒")
cook3=cookd()
cook3.setAge(30)
cook3.setName("lili")
cook3.Steamedrice()
cook3.chao()