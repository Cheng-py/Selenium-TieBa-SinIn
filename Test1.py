from selenium import webdriver  # 用来驱动浏览器的
from selenium.webdriver import ActionChains  # 破解滑动验证码的时候用的 可以拖动图片
from selenium.webdriver.common.by import By  # 按照什么方式查找，By.ID,By.CSS_SELECTOR
from selenium.webdriver.common.keys import Keys  # 键盘按键操作
from selenium.webdriver.support import expected_conditions as EC  # 和下面WebDriverWait一起用的
from selenium.webdriver.support.wait import WebDriverWait  # 等待页面加载某些元素
import time

driver=webdriver.Chrome()
try:
    wait=WebDriverWait(driver,10)
#1、访问百度
    driver.get('https://www.baidu.com/')
    #2、查找输入框
    #     input_tag = wait.until(
    #         # 调用EC的presence_of_element_located()
    #         EC.presence_of_element_located(
    #             # 此处可以写一个元组
    #             # 参数1: 查找属性的方式
    #             # 参数2: 属性的名字
    #             (By.ID, "kw")
    #         )
    #     )
    input_tag=wait.until(EC.presence_of_element_located((By.ID,"kw")))


#3、在搜索框在输入要搜索的内容
    input_tag.send_keys('狗狗')

    # 4、按键盘回车键
    input_tag.send_keys(Keys.ENTER)

    time.sleep(3)

finally:
    driver.close()

