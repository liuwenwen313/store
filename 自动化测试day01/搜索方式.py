from selenium import webdriver
import time
frame1=webdriver.Chrome()
frame1.get(r"D:\测试自动化\练习的html\练习的html\frame.html")
frame1.find_element_by_xpath("//*[@id='input1']").send_keys('123434')
time.sleep(3)
frame1.quit()
