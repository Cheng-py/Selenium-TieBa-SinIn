
import requests
import os
import json
se = requests.Session()


with open("TieBaCookies2.txt", 'r', encoding='UTF-8') as f:
    listCookies = json.loads(f.read())
    for cookie in listCookies:
        se.cookies.set(cookie['name'],cookie['value']
        )
    url = 'http://www.tieba.com'
    html = se.post(url)
    print(html.text)

