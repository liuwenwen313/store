from selenium import webdriver
import time
list=webdriver.Chrome()
list.get(r"D:\测试自动化\练习的html\练习的html\上传文件和下拉列表\autotest.html")
#输入用户名
list.find_element_by_xpath("//*[@id='accountID']").send_keys("刘雯雯")
#输入密码
list.find_element_by_xpath("//*[@id='passwordID']").send_keys("liuwenwen")
#下拉数据框选择地区
list.find_element_by_xpath("//*[@id='areaID']").send_keys("天津市")
#选择性别
list.find_element_by_xpath("//*[@id='sexID2']").click()
#选择四季
list.find_element_by_xpath("//*[@value='winter']").click()
list.find_element_by_xpath("//*[@value='Auterm']").click()
#选择上传文件
list.find_element_by_xpath("//*[@name='file' and @type='file']").send_keys(r"D:\测试自动化\练习的html\练习的html\464b1fb0af41632ec1aaaa9caefc11a.jpg")
#点击确定
list.find_element_by_xpath("//*[@id='buttonID']").click()
time.sleep(3)
list.switch_to.alert.accept()
time.sleep(2)
list.quit()