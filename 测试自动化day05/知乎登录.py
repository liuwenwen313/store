from appium import webdriver
import  time
server = r'http://localhost:4723/wd/hub'      # Appium Server, 端口默认为4723
desired_capabilities={
    "platformName": "Android",
  	"platformVersion": "7.1.2",
    "deviceName": "127.0.0.1:62001",
    "appPackage": "com.zhihu.android",
    "appActivity": "com.zhihu.android.app.ui.activity.MainActivity"
}
driver = webdriver.Remote(server, desired_capabilities) # 连接手机和APP
time.sleep(3)
el2 = driver.find_element_by_id("com.zhihu.android:id/view_guide_info")
el2.click()
time.sleep(3)
el3 = driver.find_element_by_id("com.zhihu.android:id/login_username")
el3.send_keys("17320093059")
time.sleep(2)
el4 = driver.find_element_by_id("com.zhihu.android:id/login_password")
el4.send_keys("liuwenwen313")
time.sleep(7)
el5 = driver.find_element_by_id("com.zhihu.android:id/btn_func")
el5.click()
time.sleep(5)
driver.quit()

