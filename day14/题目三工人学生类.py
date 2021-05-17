class People:
    __age=0
    __sex=""
    __name=""
    def setAge(self,age):
        self.__age=age
    def getAge(self):
        return self.__age

    def setSex(self, sex):
        self.__sex= sex
    def getSex(self):
        return self.__sex

    def setName(self,name):
        self.__name=name
    def getName(self):
        return  self.__name

class Worker(People):
    def work(self):
        print("一名叫",self.getName(),"的",self.getSex(),"工人,他说他今年",self.getAge(),"了说完开始干活了")
class Student(People):
    __sid=""
    def setSid(self,sid):
        self.__sid=sid
    def getSid(self):
        return self.__sid
    def sing(self):
        print("学号为",self.getSid(),self.getName(),"边学习边唱歌")
w=Worker()
w.setName("lili")
w.setAge(30)
w.setSex("男")
w.work()
s=Student()
s.setName("kk")
s.setSid("d16809")
s.sing()