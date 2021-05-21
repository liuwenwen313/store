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
        self.money=0
        self.bank="中国工商银行的昌平支行"
        l=Logic()
        s1=l.kaihu(self.account,self.username,self.password,self.country,self.province,self.street,self.door,self.bank,self.money)
    def test_bank_savemoney1(self):
        self.kaihu()

        self.u = User()
        self.u.setAccount(1)
        self.u.setMoney(1)
        s=1
        l = Logic()
        s1=l.bank_savemoney(self.u.getAccount(),self.u.getMoney())
        self.assertEqual(s,s1)
        from DBUtils import update
        sql = "delete  from users "
        param = []
        data = update(sql, param)
    def test_bank_savemoney2(self):
        self.kaihu()

        self.u=User()
        self.u.setAccount(2)
        self.u.setMoney(1)
        s= False
        l=Logic()
        s1=l.bank_savemoney(self.u.getAccount(),self.u.getMoney())
        self.assertEqual(s, s1)
        from DBUtils import update
        sql = "delete  from users "
        param = []
        data = update(sql, param)