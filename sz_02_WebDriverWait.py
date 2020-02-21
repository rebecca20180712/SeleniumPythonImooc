from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
#使用expected_conditions判断元素是否可见
driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://www.5itest.cn/register")
locator = (By.ID, 'register_email')
# WebDriverWait(driver,timeout,poll_frequency=0.5,ignored_exceptions=None)
# driver：浏览器驱动
# timeout：最长超时时间，默认以秒为单位
# WebDriverWait(driver,10).until(method，message="")
# 调用该方法提供的驱动程序作为参数，直到返回值为True
# 在设置时间（10s）内，等待后面的条件发生。如果超过设置时间未发生，则抛出异常。
# 在等待期间，每隔一定时间（默认0.5秒)，
# 调用until或until_not里的方法，直到它返回True或False.
wait = WebDriverWait(driver,3)
# locator = (By.CLASS_NAME, 'register_email')
element = wait.until(EC.visibility_of_element_located(locator), message="没有找到该元素")
print(element)
time.sleep(2)
driver.quit()
