from appium import webdriver
import time
server = r'http://localhost:4723/wd/hub'      # Appium Server, 端口默认为4723
desired_capabilities = {
    'platformName': 'Android',
    'deviceName': '127.0.0.1:62001',          # 需替换成你的driverName
    'platformVersion': '7.1.2',
    'appPackage': 'com.ss.android.ugc.aweme',
    'appActivity': 'com.ss.android.ugc.aweme.splash.SplashActivity '
}
driver = webdriver.Remote(server, desired_capabilities) # 连接手机和APP
time.sleep(10)
el1 = driver.find_element_by_id("com.ss.android.ugc.aweme:id/bdb")
el1.click()
while True:
    time.sleep(5)
    driver.swipe(421,856,421,266,200)