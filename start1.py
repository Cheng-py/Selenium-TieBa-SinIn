from selenium import webdriver
from selenium.webdriver.common import keys
import time
import json
import requests
#
#
#
driver = webdriver.Chrome()
main_url = "http://www.baidu.com"


def return_main_url(url):
    driver.get(main_url)
    driver.find_element_by_xpath('//*[@id="s-top-left"]/a[6]').click()
    res = driver.window_handles[1]
    driver.switch_to.window(res)
    driver.find_element_by_xpath('//*[@id="com_userbar"]/ul/li[4]/div/a').click()
    # driver.refresh()
    time.sleep(10)
    url = driver.current_url
    res = requests.get(url=url)
    print(res.text)
    cookie = driver.get_cookies()
    res = requests.get(url=url)
    print(cookie)
    return url


if __name__ == '__main__':

    return_main_url(main_url)


