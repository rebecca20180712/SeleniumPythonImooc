from selenium import webdriver

from util.read_init import ReadIni


class FindElement(object):

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, key):
        """
        获取元素
        :param key: LocalElement.ini文件中的user_email（举例）
        :return: driver.find_element_by_xxxx(value)
        value是LocalElement.ini文件中的.//*[@id='register_email']（举例）
        """
        readini = ReadIni()
        data = readini.get_value(key)
        # print("data:%s" % data)
        by = data.split('>')[0]
        value = data.split(">")[1]
        # print("by:%s" % by)
        # print("value:%s" % value)
        try:
            if by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)
            elif by == 'className':
                return self.driver.find_element_by_class_name(value)
            elif by == 'xpath':
                return self.driver.find_element_by_xpath(value)
            else:
                return self.driver.find_element_by_css(value)
        except Exception as e:
            print("find_element错误信息：", format(e))
            return None

def main():
    driver = webdriver.Firefox()
    findelement = FindElement(driver)
    findelement.get_element("user_email")
    driver.quit()

if __name__ == '__main__':
    main()
