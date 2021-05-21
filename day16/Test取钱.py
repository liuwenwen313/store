import  unittest
from bank import Logic
from bank import User
class Testlogic1(unittest.TestCase):
    def kaihu(self):
        self.account=1
        self.username=1
        self.password=1
        self.country=1
        self.province=1
        self.street=1
        self.door=1
        self.money=900
        self.bank="中国工商银行的昌平支行"
        l=Logic()
        s1=l.kaihu(self.account,self.username,self.password,self.country,self.province,self.street,self.door,self.bank,self.money)
    #正常取钱
    def test_bank_getmoney(self):
        self.kaihu()
        self.u=User()
        self.acccount = 1
        self.password = 1
        self.gmoney=0
        s=0
        l=Logic()
        s1=l.bank_getmoney(self.acccount,self.password,self.gmoney)
        self.assertEqual(s,s1)
        from DBUtils import update
        sql = "delete  from users "
        param = []
        data = update(sql, param)
    #账号错误
    def test_bank_getmoney2(self):
        self.kaihu()
        self.u = User()
        self.acccount = 2
        self.password = 1
        self.gmoney = 100
        s = 1
        l = Logic()
        s1 = l.bank_getmoney(self.acccount, self.password, self.gmoney)
        self.assertEqual(s, s1)
        from DBUtils import update
        sql = "delete  from users "
        param = []
        data = update(sql, param)
    #密码错误
    def test_bank_getmoney3(self):
        self.kaihu()
        self.u = User()
        self.acccount = 1
        self.password = 3
        self.gmoney = 100
        s = 2
        l = Logic()
        s1 = l.bank_getmoney(self.acccount, self.password, self.gmoney)
        self.assertEqual(s, s1)
        from DBUtils import update
        sql = "delete  from users "
        param = []
        data = update(sql, param)
    #密码账号都错误，组合验证
    def test_bank_getmoney4(self):
        self.kaihu()
        self.u = User()
        self.acccount = 2
        self.password = 2
        self.gmoney = 100
        s = 1
        l = Logic()
        s1 = l.bank_getmoney(self.acccount, self.password, self.gmoney)
        self.assertEqual(s, s1)
        from DBUtils import update
        sql = "delete  from users "
        param = []
        data = update(sql, param)
    #余额不足验证
    def test_bank_getmoney5(self):
        self.kaihu()
        self.u = User()
        self.acccount = 1
        self.password = 1
        self.gmoney = 1000
        s = 3
        l = Logic()
        s1 = l.bank_getmoney(self.acccount, self.password, self.gmoney)
        self.assertEqual(s, s1)
        from DBUtils import update
        sql = "delete  from users "
        param = []
        data = update(sql, param)