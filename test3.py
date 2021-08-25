from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
url = 'http://www.baidu.com'
driver.get(url)
driver.find_element_by_id('kw').send_keys('新冠病毒')
driver.find_element_by_id("su").click()
time.sleep(1.5)
driver.find_element_by_link_text("资讯").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div[5]/div/div[2]/div[2]/div[2]/h3/a/em").click()
time.sleep(1)
#生成一个新窗口或新标签页的句柄，代表这个窗口的模拟driver
n = driver.window_handles
#打印所有的句柄
print('当前句柄: ', n)
#driver切换至最新生产的页面
driver.switch_to.window(n[-1])
time.sleep(2)
driver.refresh()
time.sleep(1)
driver.refresh()
time.sleep(1)
driver.close()