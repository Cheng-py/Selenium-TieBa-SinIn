import requests
from selenium import webdriver
from selenium.webdriver.common import keys
import os
import json
import time
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
}
class TheSignIn:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.username = ''
        self.password = ''

    def close(self):
        self.driver.close()

    def get_cookie(self):
        try:
            dict_cookie = self.driver.get_cookies()
            json_cookie = json.dumps(dict_cookie)
            with open("TieBaCookies.txt",'w') as f:
                f.write(json_cookie)
            print("保存成功")
        except:
            print("保存失败")

    def load_cookie(self):
        # if not os.path.exists("TieBaCookies.txt"):
        #     self.get_cookie()
        try:
            with open("TieBaCookies.txt",'r',encoding='UTF-8') as f:
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
    def main_url(self):
        self.url = "https://www.baidu.com"
        self.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
        }
        return self.url

    def main_html(self):
        url = self.main_url()
        self.driver.get(url)
        self.driver.find_element_by_xpath('//*[@id="s-top-left"]/a[6]').click()
        # return self.driver.switch_to.window(self.driver.window_handles[1])

    def Not_Exists_Log(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        # self.driver.delete_all_cookies()
        # self.load_cookie()
        time.sleep(5)
        name = self.driver.find_element_by_xpath('//*[@id="com_userbar"]/ul/li[4  ]/div/a').text
        if(name == "登录"):
            self.driver.find_element_by_xpath('//*[@id="com_userbar"]/ul/li[4]/div/a').click()
            time.sleep(15)
            self.get_cookie()
            time.sleep(5)
            self.load_cookie()
            time.sleep(3)
            self.driver.refresh()
        return 1

    def Exists_Cookie_Log(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(1)
        self.load_cookie()
        time.sleep(5)
        # name = self.driver.find_element_by_xpath('//*[@id="com_userbar"]/ul/li[4  ]/div/a').text
        # if (name == "登录"):
        #     self.driver.find_element_by_xpath('//*[@id="com_userbar"]/ul/li[4]/div/a').click()
        #     time.sleep(15)
        #     # self.get_cookie()
        #     # time.sleep(5)
        #     self.load_cookie()
        #     time.sleep(3)
        #     self.driver.refresh()
        return 1

    def get_html(self,func):
        func()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.refresh()
        # self.driver.find_element_by_xpath('//*[@id="onekey_sign"]/a').click() # 一键签到罢了，没用
        self.driver.find_element_by_xpath('//*[@id="j_u_username"]/div[1]/a/span').click() # 点击用户名
        time.sleep(5)  # 等待加载网页时间

        self.driver.find_element_by_xpath('//*[@id="ihome_nav_wrap"]/ul/li[4]/div/p/a').click() # 点击关注的吧
        self.driver.switch_to.window(self.driver.window_handles[2])

    def SinIn(self):
        The_Value_List = []
        The_List = self.driver.find_elements_by_xpath('//*[@id="like_pagelet"]/div[1]/div[1]/table/tbody/tr[position()>1]/td[1]')  # 获取一页贴吧名，没问题

        for value in range(len(The_List)):
            The_Value_List.append(The_List[value].text)  # 一页的吧名
        print(The_Value_List)

        for value in range(len(The_Value_List)):
            if (value == len(The_Value_List) - 1):
                self.driver.find_element_by_xpath('//*[@id="j_pagebar"]/div/a[7]').click()
                value = 0
            else:
                time.sleep(2)
                self.driver.find_element_by_link_text(value).click()   # 点击吧名
                time.sleep(3)
                self.driver.find_element_by_xpath('//*[@id="signstar_wrapper"]/a').click() # 点击签到
                time.sleep(3)
                self.driver.back()

            # //*[@id="j_pagebar"]/div/a[7]   # 下一页




# ts = TheSignIn()
# ts.main_html()
# ts.Log()
# ts.get(tag)
if __name__ == '__main__':
    ts = TheSignIn()
    ts.main_url()
    ts.main_html()
    if not os.path.exists('TieBaCookies.txt'):
        func = ts.Not_Exists_Log
    else:
        func = ts.Exists_Cookie_Log
    ts.get_html(func)
    ts.SinIn()



