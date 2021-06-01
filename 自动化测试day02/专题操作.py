from selenium import webdriver
from selenium.webdriver import ActionChains
import time
#连接到谷歌
driver=webdriver.Chrome()
#连接到柠檬云记账软件
driver.get("https://www.ningmengyun.com/")
#窗口最大化
driver.maximize_window()
#点击登录
driver.find_element_by_xpath("//*[@id='loginNav']/div").click()
#停留时间扫码登录
time.sleep(8)
driver.find_element_by_xpath("//*[@id='menuEnlarge2']").click()
ele=driver.find_element_by_xpath("//*[@id='10100000']")
#Actionchain 事件链
# 将整个页面交给actionchain进行管理。获取管理对象
ac=ActionChains(driver)
# 通过管理对象模拟鼠标和键盘所有操作
ac.move_to_element(ele).perform()  # perform 执行该操作
time.sleep(2)
driver.find_element_by_link_text("新增凭证").click()
driver.quit()
