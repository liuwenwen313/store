from selenium import webdriver
import time
main1=webdriver.Chrome()
main1.get(r"D:\测试自动化\练习的html\练习的html\main.html")
#切换输入框
main1.switch_to.frame("frame")
main1.find_element_by_xpath("//*[@id='input1']").send_keys(123456)
time.sleep(3)
main1.quit()