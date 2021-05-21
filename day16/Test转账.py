import unittest
from bank import Logic
from bank import User
class Testlogic(unittest.TestCase):
    def kaihu(self):
        self.account=1
        self.username=1
        self.password=1
        self.country=1
        self.province=1
        self.street=1
        self.door=1
        self.money=1000
        self.bank="中国工商银行的昌平支行"
        l=Logic()
        s1=l.kaihu(self.account,self.username,self.password,self.country,self.province,self.street,self.door,self.bank,self.money)
        self.account = 2
        self.username = 1
        self.password = 1
        self.country = 1
        self.province = 1
        self.street = 1
        self.door = 1
        self.money = 100
        self.bank = "中国工商银行的昌平支行"
        l = Logic()
        s2 = l.kaihu(self.account, self.username, self.password, self.country, self.province, self.street, self.door,
                     self.bank, self.money)
    #正常转账
    def test_bank_transfer1(self):
        self.kaihu()
        self.u=User()
        self.account1=1
        self.account2=2
        self.password=1
        self.money=100
        s=0
        l= Logic()
        s1=l.bank_transfer(self.account1,self.account2,self.password,self.money)
        self.assertEqual(s, s1)
        from DBUtils import update
        sql = "delete  from users "
        param = []
        data = update(sql, param)
    #转出钱账号不存在
    def test_bank_transfer2(self):
        self.kaihu()
        self.u = User()
        self.account1 = 2
        self.account2 = 2
        self.password = 1
        self.money = 100
        s = 1
        l = Logic()
        s1 = l.bank_transfer(self.account1, self.account2, self.password, self.money)
        self.assertEqual(s, s1)
        from DBUtils import update
        sql = "delete  from users "
        param = []
        data = update(sql, param)
    #转入钱的账号不存在
    def test_bank_transfer3(self):
        self.kaihu()
        self.u = User()
        self.account1 = 1
        self.account2 = 3
        self.password = 1
        self.money = 100
        s = 1
        l = Logic()
        s1 = l.bank_transfer(self.account1, self.account2, self.password, self.money)
        self.assertEqual(s, s1)
        from DBUtils import update
        sql = "delete  from users "
        param = []
        data = update(sql, param)
    #两个账号都不存在
    def test_bank_transfer4(self):
        self.kaihu()
        self.u = User()
        self.account1 = 2
        self.account2 = 3
        self.password = 1
        self.money = 100
        s = 1
        l = Logic()
        s1 = l.bank_transfer(self.account1, self.account2, self.password, self.money)
        self.assertEqual(s, s1)
        from DBUtils import update
        sql = "delete  from users "
        param = []
        data = update(sql, param)
    #密码错误
    def test_bank_transfer5(self):
        self.kaihu()
        self.u = User()
        self.account1 = 1
        self.account2 = 2
        self.password = 3
        self.money = 100
        s = 2
        l = Logic()
        s1 = l.bank_transfer(self.account1, self.account2, self.password, self.money)
        self.assertEqual(s, s1)
        from DBUtils import update
        sql = "delete  from users "
        param = []
        data = update(sql, param)
    #密码账号都错误
    def test_bank_transfer6(self):
        self.kaihu()
        self.u = User()
        self.account1 = 3
        self.account2 = 2
        self.password = 3
        self.money = 100
        s = 1
        l = Logic()
        s1 = l.bank_transfer(self.account1, self.account2, self.password, self.money)
        self.assertEqual(s, s1)
        from DBUtils import update
        sql = "delete  from users "
        param = []
        data = update(sql, param)
    #余额不足
    def test_bank_transfer7(self):
        self.kaihu()
        self.u = User()
        self.account1 = 1
        self.account2 = 2
        self.password = 1
        self.money = 3000
        s = 3
        l = Logic()
        s1 = l.bank_transfer(self.account1, self.account2, self.password, self.money)
        self.assertEqual(s, s1)
        from DBUtils import update
        sql = "delete  from users "
        param = []
        data = update(sql, param)