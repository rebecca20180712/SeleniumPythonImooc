from selenium import webdriver
from business.register_business import RegisterBusiness
from util.excel_util import ExcelUtil
import os
import unittest
import time
import HTMLTestRunner
import ddt

ex = ExcelUtil()
data = ex.get_data()

@ddt.ddt
class FirstDdtCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.driver.maximize_window()
        # 当前项目路径
        self.base_dir = os.path.dirname(os.path.abspath('.'))
        # 图片路径
        self.code_name = os.path.join(self.base_dir, 'Image', 'code.png')
        # self.file_name = file_name
        self.login = RegisterBusiness(self.driver)

    def tearDown(self):
        time.sleep(2)
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                error_image_name = case_name + '.png'
                error_image_path = os.path.join(self.base_dir, 'report', error_image_name)
                print("error_image_path:%s" % error_image_path)
                self.driver.save_screenshot(error_image_path)
        self.driver.close()

    # @ddt.data(
    #         ["1", "wanxiaoyu1122", "111111", "code", "user_email_error", "请输入有效的电子邮件地址"],
    #         ["@qq.com", "wanxiaoyu1122", "111111", "code", "user_email_error", "请输入有效的电子邮件地址"],
    #         ["123456789@qq.com", "wanxiaoyu1122", "111111", "code", "user_email_error", "请输入有效的电子邮件地址"]
    #     )
    # @ddt.unpack
    @ddt.data(*data)
    def test_register_case(self, data):
        email, username, password, code_name, asserterror, asserttext = data
        password = int(password)
        email_error = self.login.register_function(email, username, password, code_name, asserterror, asserttext)
        self.assertTrue(email_error, "Error: email没有错误提示，此条case执行失败！")


if __name__ == '__main__':
    # 当前项目路径
    base_dir = os.path.dirname(os.path.abspath('.'))
    # 图片路径
    file_name = os.path.join(base_dir, 'report', 'first_case1.html')
    # wb表示以二进制的方式写文件
    f = open(file_name, 'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="This is first report1", description="这个第一个自动化测试报告1",
                                           verbosity=2)
    runner.run(suite)