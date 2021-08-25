import json
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# def get_cookie(self):
#     dict_cookie = self.driver.get_cookies()
#     json_cookie = json.dumps(dict_cookie)
#     with open("TieBaCookies.txt", 'w') as f:
#         f.write(json_cookie)
#     print("保存成功")
#
#
# def load_cookie():
#     with open("TieBaCookies.txt", 'r', encoding='UTF-8') as f:
#         listCookies = json.loads(f.read())
#     for cookie in listCookies:
#         cookie_dict = {
#             'domain': '.baidu.com',
#             'expiry':cookie.get('expiry'),
#             "httpOnly": 'true',
#             'name': cookie.get('name'),
#             'path': '/',
#             "sameSite": "None",
#             "secure": 'true',
#             'value': cookie.get('value'),
#         }
#         print(cookie_dict)
#
# load_cookie()

import os

# if os.path.exists('TieBaCookies.txt'):
#     print("在")
#
#
# def test1(func):
#     func()
#
# def test2():
#     print("Test2")
#
# test1(test2)

from selenium import webdriver
from selenium.webdriver.common import keys
def test1():
    url = "http://www.baidu.com"
    driver = webdriver.Chrome()

    driver.get(url)
    # 获取可用元素的文本、'新闻', 'hao123', '地图', '直播', '视频', '贴吧', '学术'
    res = driver.find_elements_by_xpath('//*[@id="s-top-left"]/a') # 用了 elements 是个列表，注意有个　Ｓ
    time.sleep(5)
    a = [] # 为了处理数据更方便
    for i in range(len(res)):
        a.append(res[i].text)

    for i in range(len(a)):
        driver.find_element_by_link_text("{}".format(a[i])).click()  # 把每个元素文本依次点击
        driver.switch_to.window(driver.window_handles[1]) # 切换到 新子窗口
        time.sleep(2)
        driver.close() # 关闭 子窗口
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[0])  # 切换到主页面。
    print("Success!")
test1()

