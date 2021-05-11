class notebook:
    __screensize=0
    __price=0
    __cputype=""
    __cupsize=0
    __hour=0
    def setScreensize(self,screensize):
        self.__screensize=screensize
    def getScreensize(self):
        return self.__screensize
    def setPrice(self,price):
        self.__price=price
    def getPrice(self):
        return self.__price
    def setCputype(self,cputype):
        self.__cputype=cputype
    def getCputype(self):
        return  self.__cputype
    def setCupsize(self,cupsize):
        self.__cupsize=cupsize
    def getCupsize(self):
        return  self.__cupsize
    def setHour(self,hour):
        self.__hour=hour
    def getHour(self):
        return  self.__hour

    def type(self,typeing):
        print("丽丽用电脑""打字",typeing)
    def palyGame(self,gameName):
        print("丽丽用电脑""正在玩",gameName)
    def tv(self,tving):
        print("丽丽用电脑""正在看",tving)

n=notebook()
n.setScreensize(1000)
n.setPrice(10000)
n.setCputype("y")
n.setCupsize(1000)
n.setHour(100)
n.type("做表格")
n.palyGame("跳一跳")
n.tv("喜羊羊")