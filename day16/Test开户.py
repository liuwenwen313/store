import unittest
from bank import Logic
class Testlogic(unittest.TestCase):
    def test_kaihu1(self):
        self.account=2
        self.username=1
        self.password=1
        self.country=1
        self.province=1
        self.street=1
        self.door=1
        self.money=0
        self.bank="中国工商银行的昌平支行"
        s= 1
        l=Logic()
        s1=l.kaihu(self.account,self.username,self.password,self.country,self.province,self.street,self.door,self.bank,self.money)
        self.assertEqual(s,s1)
        from DBUtils import update
        sql = "delete  from users "
        param = []
        data = update(sql, param)

    def test_kaihu2(self):
        self.account = 4
        self.username = 1
        self.password = 1
        self.country = 1
        self.province = 1
        self.street = 1
        self.door = 1
        self.money = 0
        self.bank = "中国工商银行的昌平支行"

        l = Logic()
        s1 = l.kaihu(self.account, self.username, self.password, self.country, self.province, self.street,
                     self.door, self.bank, self.money)
        s1 = l.kaihu(self.account, self.username, self.password, self.country, self.province, self.street,
                     self.door, self.bank, self.money)
        s=2
        self.assertEqual(s, s1)
        from DBUtils import update
        sql = "delete  from users "
        param = []
        data = update(sql, param)
    def test_kaihu3(self):
        for i  in range (99):
            self.account = i
            self.username = 1
            self.password = 1
            self.country = 1
            self.province = 1
            self.street = 1
            self.door = 1
            self.money = 0
            self.bank = "中国工商银行的昌平支行"
            l = Logic()
            s1 = l.kaihu(self.account, self.username, self.password, self.country, self.province, self.street,
                         self.door, self.bank, self.money)
        s = 1
        self.assertEqual(s, s1)
        from DBUtils import update
        sql = "delete  from users "
        param = []
        data = update(sql, param)
    def test_kaihu4(self):
        for i  in range (100):
            self.account = i
            self.username = 1
            self.password = 1
            self.country = 1
            self.province = 1
            self.street = 1
            self.door = 1
            self.money = 0
            self.bank = "中国工商银行的昌平支行"
            l = Logic()
            s1 = l.kaihu(self.account, self.username, self.password, self.country, self.province, self.street,
                         self.door, self.bank, self.money)
        s = 1
        self.assertEqual(s, s1)
        from DBUtils import update
        sql = "delete  from users "
        param = []
        data = update(sql, param)

    def test_kaihu5(self):
        for i in range(101):
            self.account = i
            self.username = 1
            self.password = 1
            self.country = 1
            self.province = 1
            self.street = 1
            self.door = 1
            self.money = 0
            self.bank = "中国工商银行的昌平支行"
            l = Logic()
            s1 = l.kaihu(self.account, self.username, self.password, self.country, self.province, self.street,
                         self.door, self.bank, self.money)
        s = 3
        self.assertEqual(s, s1)
        from DBUtils import update
        sql = "delete  from users "
        param = []
        data = update(sql, param)