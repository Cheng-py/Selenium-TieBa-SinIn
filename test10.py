from selenium import webdriver
import time
import requests
import json
import os


class TieBa:
    def __init__(self):
        pass

    def main_html(self):
        self.driver = webdriver.Chrome()
        self.url = 'https://www.baidu.com'
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
            with open("TieBaCookies3.txt", 'w+') as f:
                f.write(json_cookie)
            print("保存成功")
        except:
            print("保存失败")


    def get_html(self):
        se = requests.Session()
        with open("TieBaCookies3.txt", 'r', encoding='UTF-8') as f:
            listCookies = json.loads(f.read())
            for cookie in listCookies:
                se.cookies.set(cookie['name'], cookie['value'])
            url = 'http://www.tieba.com'
            html = se.post(url)
            print(html.text)  # 可以看到用户名变为你自己了。即为成功。


if __name__ == '__main__':
    tieba = TieBa()
    if not os.path.exists('TieBaCookies3.txt'):
        tieba.main_html()
        tieba.get_cookie()
        tieba.get_html()
    else:
        tieba.get_html()


