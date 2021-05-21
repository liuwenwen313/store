# -*- coding:utf-8 -*-
import random
from DBUtils import select
from DBUtils import update
# 2.银行的名称写死
bank_name = "中国工商银行的昌平支行"
# 打印欢迎页面
#1.界面类

    #用户类
class User:
    __account=0
    __name=""
    __password=""
    __address=None
    __money=0
    __bank_name="中国工商银行的昌平支行"

    # def __init__(self,account,name,password,address,bank):
    #     self.__account=account
    #     self.__name=name
    #     self.__password=password
    #     self.__address=address
    #     self.__bank=bank
    def setAccount(self,account):
        self.__account=account
    def getAccount(self):
        return self.__account
    def setName(self,name):
        self.__name=name
    def getName(self):
        return self.__name
    def setPassword(self, password):
        self.__password = password
    def getPassword(self):
        return self.__password
    def setAddress(self,address):
        self.__address=address
    def getAddress(self):
        return  self.__address
    def setMoney(self, money):
        self.__money = money

    def getMoney(self):
        return self.__money

    def setBank_name(self, bank_name="中国工商银行的昌平支行"):
        self.__bank_name =bank_name

    def getBank_name(self):
        return self.__bank_name

#地址类
class Address:
    __country=""
    __province=""
    __street=""
    __door=""
    # def __init__(self,country,province,street,door):
    #     self.__country=country
    #     self.__province=province
    #     self.__street=street
    #     self.__door=door

    def setCountry(self,country ):
        self.__country = country

    def getCountry(self):
        return self.__country

    def setProvince(self, province):
        self.__province = province

    def getProvince(self):
        return self.__province

    def setStreet(self, street):
        self.__street = street

    def getStreet(self):
        return self.__street

    def setDoor(self, door):
        self.__door = door

    def getDoor(self):
        return self.__door
#银行类
# class Bank:

    # def __init__(self,money,bank_name):
    #     self.__money=money
    #     self.__bank_name=bank_name


#数据库帮助类
class DBUtils:
    import pymysql
    __host="localhost"
    __user = "root"
    __passsword = ""
    __database = "银行数据库"

    def setHost(self, host):
        self.__host = host

    def getHost(self):
        return self.__host

    def setUser(self, user):
        self.__user = user

    def getUser(self):
        return self.__user

    def setPasssword(self, passsword):
        self.__passsword=passsword

    def getPasssword(self):
        return self.__passsword

    def setDatabase(self, database):
        self.__database = database

    def getDatabase(self):
        return self.__database
    con=pymysql.connect( host=__host,user=__user,password=__passsword,database=__database)
    cursor = con.cursor()
    def update(self,sql,param):
        self.cursor.execute(sql,param)
        self.con.commit()
        self.cursor.close()
        self.con.close()
        return self.cursor.execute(sql,param)

    def select(self, sql, param):
        self.cursor.execute(sql, param)
        self.con.commit()
        self.cursor.close()
        self.con.close()
        return self.cursor.fetchall()
#逻辑方法类
class Logic:
#开户
     def kaihu(self,account,username,password,country,province,street,door,bank,money):
         sql = "select * from   users"
         #调用方法 select
         user=select(sql,[])
         if len(user) >=100 :
            return 3
        # 判断是否存在
         sql = "select 账号  from users  where 账号= %s;"
         param = [account]
         user=select(sql,param)
         if len(user) > 0:
             return 2
    #正常开户
         sql = "insert into users  values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
         param = [account,username, password, country, province, street, door,  money,  '中国工商银行的昌平支行']
         # #调用方法 update
         update(sql,param)
         return 1
#存钱
     def bank_savemoney(self,account,money):
            sql = "select 账号  from users  where 账号= %s;"
            param = [account]
            # 调用select方法
            user = select(sql, param)
            if len(user) > 0:
                sql = "update  users set 余额=余额+ %s where 账号= %s"
                param = [money,account]
                ##调用方法update
                update(sql, param)  # (sql模板，param实际的填充参数)
                return 1
            else:
                return False
#取钱逻辑
     def bank_getmoney (slef,account,password,gmoney):
        # 账号是否存在
         sql="select 账号 from users where 账号 =%s"
         param=[account]
         user=select(sql,param)
         if len(user)>0:
    # 密码是否正确
            sql="select 账号 from users where 账号 =%s and  密码 = %s"
            param=[account,password]
            user=select(sql,param)
            if len(user)>0:
                #正常取钱
                sql="select 账号 from users where 余额>=%s and  账号 =%s"
                param = [gmoney, account]
                user=select(sql,param)
                if len(user) >0:
                   sql="update users set 余额=余额-%s where 账号 =%s"
                   param=[gmoney,account]
                   update(sql,param)
                   return 0
                else:
                     return 3
            else:
                return 2
         else:
            return 1
    #转账的逻辑
     def bank_transfer(self,account1, account2, password, money):
        # 两个账号是不是存在
        sql = "select 账号 from users where 账号=%s or 账号=%s"
        param = [account1, account2]
        user = select(sql, param)
        if len(user) == 2:
            # 转出账号密码是不是存在
            sql = "select * from users where 密码=%s and 账号=%s"
            param = [password, account1]
            user = select(sql, param)
            if len(user) > 0:
                # 转出金额是不是足够
                sql = "select 账号 from users where 余额>=%s and 账号=%s"
                param = [money, account1]
                user = select(sql, param)
                if len(user) > 0:
                    # 正常转出
                    sql = "update  users set 余额=余额- %s where 账号= %s "
                    param = [money, account1]
                    update(sql, param)
                    # 调用update方法
                    sql = "update  users set 余额=余额+ %s where 账号= %s "
                    param = [money, account2]
                    update(sql, param)
                    return 0
                else:
                    return 3
            else:
                return 2
        else:
            return 1
    #查询逻辑
     def bank_query(self,account,password):
        sql = "select 账号 from users where 账号=%s "
        param = [account]
        user=select(sql, param)
        if len(user) > 0:
            sql = "select * from users where  密码= %s and 账号 = %s"
            param = [password,account]
            user=select(sql, param)
            print(user)
            if len(user) > 0:
               account1=user[0][0]
               name=user[0][1]
               password=user[0][2]
               money= user[0][7]
               country=user[0][3]
               province=user[0][4]
               street=user[0][5]
               door=user[0][6]
               bank_name= user[0][8]
               info = '''
                           ------------个人信息----------------
                           账号：%s,
                           用户名：%s,
                           取款密码：%s,
                           地址信息：
                               国家：%s,
                               省份：%s,
                               街道：%s,
                               门牌号：%s,
                           余额：%s,
                           开户行：%s
                           -----------------------------------
                       '''
               print(info % (account1, name, password,money ,country, province, street, door, bank_name))

               return 1
            else:
                return 3
        else:
            return 2
#输入帮助类
class Input:
    #开户
    def  open_account(self):

         u.setAccount(random.randint(10000000, 99999999))
         u.setName(input("请输入你的姓名"))
         u.setPassword(input("请输入你的密码"))
         add.setCountry(input("请输入国家"))
         add.setProvince(input("请输入省份"))
         add.setStreet(input("请输入您的街道"))
         add.setDoor(input("请输入您的门牌号"))
         u.setBank_name()
         # u.setMoney()
         status =logic.kaihu(u.getAccount(),u.getName(),u.getPassword(),add.getCountry(),add.getProvince(),add.getStreet(),add.getDoor(),u.setBank_name(),u.getMoney())
         if status == 1:
             print("恭喜开户成功！")
             info = '''
                    ------------个人信息----------------
                    账号：%s,
                    用户名：%s,
                    取款密码：%s,
                    地址信息：
                        国家：%s,
                        省份：%s,
                        街道：%s,
                        门牌号：%s,
                    余额：%s,
                    开户行：%s
                    -----------------------------------
                '''
             print(info % (u.getAccount(), u.getName(), u.getPassword(), add.getCountry(), add.getProvince(), add.getStreet(), add.getDoor(), 0, u.setBank_name()))

         elif status == 2:
             print("对不起，该用户已存在！请稍后重试！！！")
         elif status == 3:
             print("对不起，该银行库已满，请携带证件到其他银行办理！！！")
    #存钱方法
    def savemoney(self):
        u.setAccount(input("请输入你的账号"))
        u.setMoney(input("请输入您的存款金额："))
        # if bank.getMoney.isdigit():
        #     bank.setMoney (int(bank.getMoney))
        #     break
        #   else:
        #     print("您输入非法重新输入")
        status0 = logic.bank_savemoney()
        if status0 == 1:
            print("存款成功")
        if status0 == False:
            print("您输入的账号不存在")
    #取钱方法
    def getmoney(self):
        u.setAccount ( input("请输入用户账号:"))
        u.setPassword(input("请输入您的用户密码:"))
        while True:
            gmoney = input("请输入您的取钱金额:")
            if gmoney.isdigit():
                gmoney = int(gmoney)
                break
            else:
                print("您输入非法重新输入")

        status1 = logic.bank_getmoney (u.getAccount(), u.getPassword(), gmoney )
        if status1 == 0:
            print("恭喜你，取款成功，")
        elif status1 == 1:
            print("账号不存在！")
        elif status1 == 2:
            print("密码不正确！")
        elif status1 == 3:
            print("您的余额不足！")
    #转账方法
    def transfer(self):
        u2 = User()
        u.setAccount (input("请输入转出钱的账号："))
        u2.setAccount(input("请输入转入钱的账号："))
        u.setPassword (input("请输入转出账号的密码："))
        while True:
            money = input("请输入您要转出的金额:")
            if money.isdigit():
                money = int(money)
                break
            else:
                print("您输入非法重新输入")

        status4 =logic.bank_transfer( u.getAccount(), u2.getAccount(), u.getPassword(), money)
        if status4 == 0:
            print("转账成功")
        elif status4 == 1:
            print("您输入的账号不存在：")
        elif status4 == 2:
            print("您输入的密码错误：")
        elif status4 == 3:
            print("您的余额不足：")
        input()
        #查询方式
    def query(self):
        u.setAccount(input("请输入您的账号："))
        u.setPassword(input("请输入您的密码："))
        status5=logic.bank_query(u.getAccount(),u.getPassword())
        if status5==1:
            print("查询信息如上",)
        elif status5 == 2:
            print("您输入的用户不存在")
        elif status5 == 3:
            print("您输入的密码有误")
#初始化必要对象
u=User()
add=Address()
dbu=DBUtils()
logic=Logic()
inp=Input()
#入口程序类


