from selenium import webdriver
from base.find_element import FindElement
import time


class ActionMethod(object):

    def __init__(self):
        self.driver = None

    def open_browser(self, browser):
        """
        打开浏览器
        :param browser:浏览器类型
        :return: driver
        """
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "ie":
            self.driver = webdriver.Edge()
        else:
            self.driver = webdriver.Firefox()


    def get_url(self, url):
        """
        输入url
        :param url:网址
        """
        self.driver.get(url)

    def get_element(self, key):
        """
        定位元素
        :param key: LocalElement.ini文件中的key
        :return: driver.find_element_by_xxxx(value)
        """
        find_element = FindElement(self.driver)
        element = find_element.get_element(key)
        return element

    def element_send_keys(self, key, value):
        """
        输入元素
        :param key: LocalElement.ini文件中的key
        :param value: 要输入的值
        """
        element = self.get_element(key)
        element.send_keys(value)

    def click_element(self, key):
        """
        点击元素
        :param key:LocalElement.ini文件中的key
        """
        element = self.get_element(key)
        element.click()

    def get_title(self):
        return self.driver.title

    def sleep_time(self, times):
        """
        等待时间
        :param times: 需要等待的时间
        """
        time.sleep(times)

    def close_browser(self):
        """
        关闭浏览器
        """
        self.sleep_time(3)
        self.driver.close()