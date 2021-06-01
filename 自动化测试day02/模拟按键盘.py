#（key_down,key_up）（key_down,key_up）
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.find_element_by_xpath("//*[@id='kw']").send_keys(Keys.NUMPAD3)
