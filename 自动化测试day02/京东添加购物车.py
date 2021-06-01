from selenium import webdriver
from  selenium.webdriver import ActionChains
import  time
driver=webdriver.Chrome()
#获取网址连接
driver.get("https://www.jd.com/?cu=true&utm_source=baidu-search&utm_medium=cpc&utm_campaign=t_262767352_baidusearch&utm_term=53344535735_0_ecb18c970f6941c999d03872541f6808")
#窗口最大化
driver.maximize_window()
time.sleep(4)
#定位登录模块
driver.find_element_by_link_text("你好，请登录").click()
#切换窗口
#获取所有窗口句柄
# wins=driver.window_handles
# print(wins)
#切换到账户登录
driver.find_element_by_link_text("账户登录").click()
#输入账户
driver.find_element_by_xpath("//*[@id='loginname']").send_keys("17320093059")
#输入密码
driver.find_element_by_xpath("//*[@id='nloginpwd']").send_keys("liuwenwen313")
#点击登录
driver.find_element_by_xpath("//*[@id='loginsubmit']").click()
#手动拖动滑块的时间
time.sleep(15)#手动拖动滑块的时间
#定位输入框。输入电脑
driver.find_element_by_xpath("//*[@id='key']").send_keys("电脑")
time.sleep(2)
#点击搜索
driver.find_element_by_xpath("//*[@id='search']/div/div[2]/button/i").click()
time.sleep(3)
#创建Actionchain
ac=ActionChains(driver)
ac.move_by_offset(0,200).perform()
driver.find_element_by_xpath("//*[@id='J_goodsList']/ul/li[1]/div/div[1]/a/img").click()
time.sleep(2)
#获取所有窗口
wins=driver.window_handles
print(wins)
#切换到需要的窗口
driver.switch_to.window(wins[1])
time.sleep(4)
#选择电脑配置
driver.find_element_by_xpath("//*[@id='choose-attr-1']/div[2]/div[3]/a/i").click()
#加入购物车
driver.find_element_by_xpath("//*[@id='btn-reservation']").click()
time.sleep(4)
driver.quit()