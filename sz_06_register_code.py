from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from PIL import Image
from ShowapiRequest import ShowapiRequest

import time
import os
import random


class RegisterOperate(object):

    def __init__(self, file_name):
        self.driver = webdriver.Firefox()
        self.driver.get('http://www.5itest.cn/register')
        self.driver.maximize_window()
        # self.driver.implicitly_wait(10)
        self.file_name = file_name

    def get_element(self, xpath):
        # 获取element信息
        element = self.driver.find_element_by_xpath(xpath)
        return element

    @staticmethod
    def get_range_for_user():
        # 获取随机字符串，用于邮箱随机输入、用户名随机输入
        user_info = ''.join(random.sample("1234567890abcdefg", 9))
        return user_info

    def get_code_image(self):
        # 获取验证码图片，并保存到file_name中
        # 全屏截图
        self.driver.save_screenshot(self.file_name)
        # 定位验证码
        code_element = self.get_element(".//*[@id='getcode_num']")
        # print(code_element.location)
        # print(code_element.size)
        # 定位左上角x值
        left_x = code_element.location['x']
        # 定位左上角y值
        left_y = code_element.location['y']
        # 定位右上角x值
        right_x = code_element.size['width'] + left_x
        # 定位右上角y值
        right_y = code_element.size['height'] + left_y
        # print(left_x, left_y, right_x, right_y)
        # 使用PIL下的Image打开截图的imooc.png图片
        im = Image.open(self.file_name)
        # 将指定的某部分裁剪出来
        img = im.crop((left_x, left_y, right_x, right_y))
        img.save(self.file_name)

    def code_online(self):
        # 将file_name中的验证码图片进行识别，用于注册时验证码输入
        r = ShowapiRequest("http://route.showapi.com/184-4", "144729", "e3e550c74b9d4e0b85c3889ce3ec3bfc")
        # ShowapiRequest 的第一个参数是万维易源网的url ，第二个参数是易源网上你个人的appId ， 第三个参数是易源网上的密钥

        r.addBodyPara("typeId", "35")  # typeId：表示识别几位数的图片验证码 ；35：'3'表示英数结合的验证码，'5'表示5位数的验证码   ； 31：一位数的验证码
        r.addBodyPara("convert_to_jpg", "0")
        r.addFilePara("image", self.file_name)  # 添加要识别验证码的图片
        res = r.post()
        # print(res.text)  # {"showapi_res_error":"","showapi_res_id":"6f0e4cdb977141b293ea12178ad3d37e","showapi_res_code":0,"showapi_res_body":{"Id":"5bac83cc-5637-4e2d-bc91-25a78b527241","Result":"ANLZZ","ret_code":0}}
        code_text = res.json()['showapi_res_body']['Result']  # 以json格式读取：showapi_res_body 下 Result 的值
        # print(text)  # 返回信息：ANLZZ (识别正确)
        return code_text

    def browser_quit(self):
        self.driver.quit()

    def run_main(self):
        #主程序
        #用户名
        user_name = self.get_range_for_user()
        #邮箱
        user_email = self.get_range_for_user() + '@qq.com'
        # 邮箱定位
        self.get_element(".//*[@id='register_email']").send_keys(user_email)
        # 用户名
        self.get_element(".//*[@id='register_nickname']").send_keys(user_name)
        # 密码
        self.get_element(".//*[@id='register_password']").send_keys("11111111")
        # 验证码
        self.get_code_image()
        code_text = self.code_online()
        print(code_text)
        self.get_element(".//*[@id='captcha_code']").send_keys(code_text)
        # 注册
        self.get_element(".//*[@id='register-btn']").click()
        time.sleep(5)
        self.browser_quit()

if __name__ == "__main__":
    # 当前项目路径
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # 图片路径
    file_name = os.path.join(base_dir, 'Image', 'code.png')
    register_ope = RegisterOperate(file_name)
    register_ope.run_main()
