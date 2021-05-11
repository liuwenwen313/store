class cup:
    __host=0
    __volume=0
    __color=""
    __material=""
    def setHost(self,host):
        self.__host=host
    def getHost(self):
        return  self.__host
    def setVolume(self,volume):
        self.__volume=volume
    def getVolume(self):
        return  self.__volume
    def setColor(self,color):
        self.__color=color
    def getColor(self):
        return self.__color
    def setMaterial(self,material):
        self.__material=material
    def getMaterial(self):
        return self.__material
    def liquid(self, Cliquid):
        print(self.__color,"的杯子""装有一半的",Cliquid)
l = cup()
l.setHost(120)
l.setVolume(1)
l.setColor("绿色")
l.setMaterial("亚克力")
l.liquid("红色的可乐")