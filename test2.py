# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Chrome()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def hd():
    for handle in driver.window_handles:
        return handle

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

elem = driver.find_element_by_xpath('//*[@id="kw"]')

elem.send_keys("狗狗")

elem.send_keys(Keys.ENTER)

driver.execute_script("window.open('http://www.hao123.com');")  # 注意js语句要带分号
# driver.get("http://www.hao123.com")
driver.switch_to.window(hd()[0])

    # driver.get("http://www.sohu.com")
# driver.switch_to.window(handle[1])
hd()[3].driver.execute_script("window.open('http://www.hao123.com');")  # 注意js语句要带分号