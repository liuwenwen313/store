# encoding=utf-8
from appium import webdriver
import time
server = r'http://localhost:4723/wd/hub'      # Appium Server, 端口默认为4723
desired_capabilities = {
    'platformName': 'Android',
    'deviceName': '127.0.0.1:62001',          # 需替换成你的driverName
    'platformVersion': '7.1.2',
    'appPackage': 'com.jingdong.app.mall',
    'appActivity': 'com.jingdong.app.mall.main.MainActivity'
}
driver = webdriver.Remote(server, desired_capabilities) # 连接手机和APP
time.sleep(2)
#点击输入框
el0 = driver.find_element_by_id("com.jingdong.app.mall:id/bqd")
el0.click()
time.sleep(2)
#点击输入框
driver.tap([(295,184)],50)
time.sleep(4)
#搜索衣服
el1=driver.find_element_by_class_name("android.widget.EditText")  # 点击更多
el1.send_keys("衣服")
#搜索按钮
time.sleep(2)
el2 = driver.find_element_by_accessibility_id("搜索，按钮")
el2.click()
time.sleep(5)
#选中商品
el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]")
el3.click()
#点击商品
time.sleep(5)
el6 = driver.find_element_by_id("com.jd.lib.productdetail.feature:id/pd_invite_friend")
el6.click()
# driver.switch_to.frame("com.jingdong.app.mall:id/ap_")
time.sleep(3)
#选择颜色
el4 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.view.ViewGroup/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.TextView")
el4.click()
time.sleep(5)
#选择尺码
el5 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.TextView")
el5.click()
#加入购物车
el17 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.RelativeLayout")
el17.click()
time.sleep(9)
driver.quit()
