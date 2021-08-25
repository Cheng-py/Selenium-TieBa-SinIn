from selenium import webdriver
from selenium.webdriver.common import keys
import time
url = 'http://news.baidu.com/'

driver = webdriver.Chrome()

driver.get(url)
driver.find_element_by_xpath('//*[@id="channel-all"]/div/ul/li[2]/a').click()
time.sleep(2)
driver.back()