from selenium import webdriver
from business.register_business import RegisterBusiness
import os
import unittest
import time
import HTMLTestRunner



class FirstCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.driver.maximize_window()
        # 当前项目路径
        self.base_dir = os.path.dirname(os.path.abspath('.'))
        # 图片路径
        self.code_name = os.path.join(self.base_dir, 'Image', 'code.png')
        self.code_name = "code"
        # self.file_name = file_name
        self.login = RegisterBusiness(self.driver)

    def tearDown(self):
        time.sleep(2)
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                error_image_name = case_name + '.png'
                error_image_path = os.path.join(self.base_dir, 'report', error_image_name)
                # print("error_image_path:%s" % error_image_path)
                self.driver.save_screenshot(error_image_path)
        self.driver.close()

    @unittest.skip("不执行该case")
    def test_login_success(self):
        login_success = self.login.register_succes()
        if login_success:
            print("注册成功!")
        else:
            print("注册失败！")

    def test_login_email_error(self):
        email_error = self.login.login_email_error('3451875341','xiaoyu','111111',self.code_name)
        self.assertFalse(email_error, "Error: email没有错误提示，此条case执行失败！")
        # if email_error == True:
        #     print("Error: email没有错误提示，此条case执行失败！")
        # # self.login_success()
        # else:
        #     print("pass:email有错误提示，此条case执行成功")

    @unittest.skip("不执行该case")
    def test_login_username_error(self):
        # self.driver.refresh()
        username_error = self.login.login_name_error('3451875341@qq.com','bb1','111111',self.code_name)
        self.assertTrue(username_error, "pass:username没有错误提示，此条case执行成功")
        # if username_error == True:
        #     print("Error: username没有错误提示，此条case执行失败！")
        # # self.login_success()
        # else:
        #     print("pass:username有错误提示，此条case执行成功")

    def test_login_password_error(self):
        # self.driver.refresh()
        password_error = self.login.login_password_error('3451875342','ccccc11','1',self.code_name)
        self.assertTrue(password_error, "pass:password没有错误提示，此条case执行成功")
        # if password_error == True:
        #     print("Error: password没有错误提示，此条case执行失败！")
        # # self.login_success()
        # else:
        #     print("pass:password有错误提示，此条case执行成功")

    def test_login_code_error(self):
        # self.driver.refresh()
        code_error = self.login.login_code_error('3451875343@qq.com','dddddddd11','111111',self.code_name)
        self.assertTrue(code_error, "pass:验证码没有错误提示，此条case执行成功")
        # if code_error == True:
        #     print("Error: 验证码没有错误提示，此条case执行失败！")
        # # self.login_success()
        # else:
        #     print("pass:验证码有错误提示，此条case执行成功")

    def main_run(self):

        self.test_login_email_error()
        self.test_login_username_error()
        self.test_login_password_error()
        self.test_login_code_error()
        self.driver.close()




if __name__ == '__main__':
    #当前项目路径
    base_dir = os.path.dirname(os.path.abspath('.'))
    # 图片路径
    file_name = os.path.join(base_dir, 'report', 'first_case.html')
    print("file_name :%s" % file_name)
    suite = unittest.TestSuite()
    suite.addTest(FirstCase("test_login_email_error"))
    # suite.addTest(FirstCase("test_login_username_error"))
    # suite.addTest(FirstCase("test_login_password_error"))
    # suite.addTest(FirstCase("test_login_code_error"))
    #wb表示以二进制的方式写文件
    f = open(file_name, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="This is first report", description="这个第一个自动化测试报告", verbosity=2)
    runner.run(suite)