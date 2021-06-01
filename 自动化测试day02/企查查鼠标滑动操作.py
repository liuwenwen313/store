from  selenium import webdriver
from  selenium.webdriver import ActionChains
import time
driver=webdriver.Chrome()
driver.get(r"https://www.qcc.com/?utm_source=baidu&utm_medium=cpc&utm_term=%E6%9F%A5%E6%9F%A5%E4%BC%81")
driver.maximize_window()
time.sleep(5)
#取消拦截
driver.find_element_by_xpath("//*[@id='addfavorModal']/div/div/div[1]").click()
#用文本定位登录
driver.find_element_by_link_text("登录 | 注册").click()
time.sleep(4)
#获取滑块
hk=driver.find_element_by_xpath("//*[@id='nc_1_n1z']")
#创建Actionchain
ac=ActionChains(driver)
ac.click_and_hold(hk).move_by_offset(348,0).perform()
time.sleep(6)
driver.quit()
