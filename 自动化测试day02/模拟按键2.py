#（key_down,key_up）（key_down,key_up）
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
#h获取百度地址
driver.get("https://www.baidu.com/")
#输入框
ele=driver.find_element_by_xpath("//*[@id='kw']")
#创建ActionChains
ac=ActionChains(driver)
#按住输入框
ele.click()
#利用键盘输入内容
ac.key_down("3").key_up("3").perform()
#时间停留3s
time.sleep(3)
#关闭
driver.quit()