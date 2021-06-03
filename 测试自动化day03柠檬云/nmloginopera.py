from selenium import webdriver
import  time
class Loginlogic:#登录逻辑
    def __init__(self,driver):
        self.driver = driver
    # 封装登录逻辑
    def login(self,username,password):
        #输入用户名
        self.driver.find_element_by_id("userName").send_keys(username)
        #输入密码
        self.driver.find_element_by_id("password").send_keys(password)
        #定位到输入验证码s
        # self.driver.find_element_by_id("confirmCode").click()
        # time.sleep(20)#手动输入验证码
        #点击登录
        self.driver.find_element_by_id("btn_login").click()
        time.sleep(3)
    #获取登录成功的实际结果
    def get_success_login(self):
        return self.driver.title
    #获取密码错误情况的登录失败的结果
    def get_error_password_login(self):
        return self.driver.find_element_by_xpath("//*[@class='layui-layer-content']").text
   #获取密码错误情况的登录失败的结果
    def get_error_username_login(self):
        return self.driver.find_element_by_xpath("//*[@class='layui-layer-content']").text
    # 获取无账号的实际结果
    def get_error_nousername_login(self):
        return self.driver.title
