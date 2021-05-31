from selenium import webdriver
import time
tan=webdriver.Chrome()
tan.get(r"D:\测试自动化\练习的html\练习的html\弹框的验证\dialogs.html")
tan.find_element_by_xpath("//*[@id='confirm']").click()
time.sleep(3)
tan.switch_to.alert.dismiss()#点击取消
time.sleep(3)
tan.find_element_by_xpath("//*[@id='alert']").click()
time.sleep(3)
tan.switch_to.alert.accept()#点击确定
time.sleep(3)
tan.quit()
tan.quit()