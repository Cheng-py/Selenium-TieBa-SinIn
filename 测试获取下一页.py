a = [1,2,3,4,5]
for i in range(len(a)):
    if i == len(a)-1:
        print("等于")
        print(i,len(a)-1)
    # else:
    #     print("不")
    #     print(i,len(a))

from selenium import webdriver
from selenium.webdriver.common import keys
import time
url2  = 'https://www.baidu.com/s?wd=asdhadandlf&rsv_spt=1&rsv_iqid=0xfffcf7280000c40b&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=0&rsv_dl=tb&oq=asdhadandlfas&rsv_btype=t&inputT=509&rsv_t=3677OWpz8%2F6MCN0d4nboYVDntx%2BEYUOZFiiO2smWSc1TyliAIy88ezUKT1zGctMIQXFr&rsv_pq=fc812bd300033af3&rsv_sug3=95&rsv_sug2=0&rsv_sug4=729'
driver = webdriver.Chrome()
driver.get(url2)


try:
    while True:
        if (driver.find_element_by_xpath('//*[@id="page"]/div/a[2]')):
             print("True")

             driver.find_element_by_xpath('//*[@id="page"]/div/a[2]').click()
        else:
             driver.close()
             break
except:
    print("Success!")
# while (True):
#     if(True):
#         for i in range(1, 10):
#             print(i)
#     else:
#         print("不在")

# driver.find_element_by_xpath('//*[@id="channel-all"]/div/ul/li[2]/a').click()
# time.sleep(5)
# driver.back()

a = [1,2,3,4,5]
# for i in range(len(a)):
#     if i == len(a)-1:
#         print("大于")
#         i = 0
#     else:
#         print("小于")
#
# n = 0
# while(n<10):
#     print(n)
#     if (n==10):
#         n=1
#     else:
#         n+=1
# x= 1
# while(True):
#     x+=1
#     print(x)
#     if(x>10):
#         break

