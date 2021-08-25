from selenium import webdriver
from selenium.webdriver.common import keys
import time
import json
import os


class TieBa:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = 'https://www.baidu.com'

    def main_html(self):
        self.driver.get(self.url)
        self.driver.find_element_by_xpath('//*[@id="s-top-left"]/a[6]').click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.find_element_by_xpath('//*[@id="com_userbar"]/ul/li[4]/div/a').click()  # 扫码登录
        time.sleep(10)

    def get_cookie(self):
        time.sleep(3)
        try:
            dict_cookie = self.driver.get_cookies()
            json_cookie = json.dumps(dict_cookie)
            with open("TieBaCookies2.txt", 'w+') as f:
                f.write(json_cookie)
            print("保存成功")
        except:
            print("保存失败")

    def load_cookie(self):
        time.sleep(2)
        try:
            with open("TieBaCookies2.txt", 'r', encoding='UTF-8') as f:
                listCookies = json.loads(f.read())
            for cookie in listCookies:
                cookie_dict = {
                    "domain": "tieba.baidu.com",
                    'name': cookie.get('name'),
                    'path': '/',
                    'value': cookie.get('value'),

                }
                self.driver.add_cookie(cookie_dict)
            self.driver.refresh()
        except:
            print("打开失败")


if __name__ == '__main__':
    tb = TieBa()
    tb.main_html()
    if not os.path.exists('TieBaCookies2.txt'):
        tb.get_cookie()
        tb.load_cookie()
    else:
        tb.load_cookie()
