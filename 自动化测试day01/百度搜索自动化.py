from selenium import webdriver
import time
#1.创捷谷歌游览器对象
chrome1=webdriver.Chrome()
#2.打开相应的网页
chrome1.get("http://www.baidu.com")
#3.窗口最大化
chrome1.maximize_window()
#4.定位输入框，并输入查找内容
chrome1.find_element_by_id("kw").send_keys("自动化测试") #send_keys()发送一个值
#5.自动点击百度一下按钮
chrome1.find_element_by_id("su").click()#click点击
#6等待时间
time.sleep(3)
#7.关闭浏览器
chrome1.quit()