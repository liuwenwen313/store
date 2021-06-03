from selenium import webdriver
import time
from  ddt import ddt
from  ddt import data
import unittest
from nmPage import Logindata
from nmloginopera import Loginlogic
# 1.将测试类用@ddt修饰
@ddt
class LoginTest(unittest.TestCase):
        def setUp(self) -> None:# 在所有测试方法之前运行
            self.driver=webdriver.Chrome()
            #获取网址
            self.driver.get("https://www.ningmengyun.com/")
            # 窗口最大化
            self.driver.maximize_window()
            #点击登录
            self.driver.find_element_by_xpath("//*[@id='loginNav']").click()
            time.sleep(3)
            #选择密码登录
            self.driver.find_element_by_xpath("//*[@id='loginModel']/div/div/div[1]/div[2]/div/div/div[3]/a[1]").click()
        def tearDown(self) -> None:
             time.sleep(20)
             self.driver.quit()
        #登录测试成功用例
    #2.data引入数据源
        @data(*Logindata.success_data)
        def test_success_login(self,data):
            # 创建页面操作逻辑对象
            l=Loginlogic(self.driver)
            #执行登录逻辑
            l.login(data["username"],data["password"])
            #获取实际结果
            result=l.get_success_login()
            #把期望结果提取出来
            expect=data["expect"]
            #断言
            self.assertEqual(result,expect)
        #密码错误测试用例
        @data(*Logindata.password_error_data )
        def test_password_login(self, data):
            # 创建页面操作逻辑对象
            l = Loginlogic(self.driver)
            # 执行登录逻辑
            l.login(data["username"], data["password"])
            # 获取实际结果
            result = l.get_error_password_login()
            # 把期望结果提取出来
            expect = data["expect"]
            # 断言
            self.assertEqual(result, expect)
        #用户错误测试用例
        @data(*Logindata.username_error_data )
        def test_username_login(self, data):
            # 创建页面操作逻辑对象
            l = Loginlogic(self.driver)
            # 执行登录逻辑
            l.login(data["username"], data["password"])
            # 获取实际结果
            result = l.get_error_password_login()
            # 把期望结果提取出来
            expect = data["expect"]
            # 断言
            self.assertEqual(result, expect)
        #用户为空
        @data(*Logindata.nousername_error_data)
        def test_nousername_login(self, data):
            # 创建页面操作逻辑对象
            l = Loginlogic(self.driver)
            # 执行登录逻辑
            l.login(data["username"], data["password"])
            # 获取实际结果
            result = l.get_error_nousername_login()
            # 把期望结果提取出来
            expect = data["expect"]
            # 断言
            self.assertEqual(result, expect)