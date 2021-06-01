from selenium import webdriver
from selenium.webdriver import ActionChains
import time
#连接谷歌
driver=webdriver.Chrome()
#获取网址
driver.get("https://www.suning.com")
#定位输入框，输入搜索商品名
driver.find_element_by_xpath("//*[@id='searchKeywords']").send_keys("电脑")
#点击搜索
driver.find_element_by_xpath("//*[@id='searchSubmit']").click()
time.sleep(2)
#关闭拦截，广告
driver.find_element_by_xpath("//*[@id='pop418']/a").click()
#选择需要商品
driver.find_element_by_xpath("//*[@id='ssdsn_search_pro_baoguang-1-0-1_1_01:0000000000_12157019776']/i/img").click()
time.sleep(4)
#获取所有界面
wins=driver.window_handles
print(wins)
#切换界面
driver.switch_to.window(wins[1])
#选择配置
driver.find_element_by_xpath("//*[@id='colorItemList']/dd/ul/li[11]/a/span").click()
time.sleep(2)
#加入购物车
driver.find_element_by_xpath("//*[@id='addCart']").click()
driver.quit()