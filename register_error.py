import os
import random
import time

from PIL import Image
from selenium import webdriver

from ShowapiRequest import ShowapiRequest
from base.find_element import FindElement


# import sys
# sys.path.append("D:/pycharm_file/自动化实战")


class RegisterFunction2(object):

    def __init__(self, url, i):
        self.driver = self.get_driver(url, i)

    def get_driver(self, url, i):
        """
        获取driver,并打开url
        :param url:网页地址
        :return:driver
        """
        if i == 0:
            driver = webdriver.Firefox()
        else:
            driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(url)
        return driver

    def get_user_element(self, key):
        """
        定位用户信息，获取element
        :param key:配置文件中key
        :return:user_element
        """
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(key)
        return user_element

    def send_user_info(self, key, data):
        """
        输入用户信息
        :param key:配置文件中key
        :param data:文本框输入值
        """
        self.get_user_element(key).send_keys(data)

    @staticmethod
    def get_range_for_user():
        """
        获取随机字符串，用于邮箱随机输入、用户名随机输入
        :return: 随机数的值
        """
        user_info = ''.join(random.sample("1234567890abcdefg", 9))
        return user_info

    def get_code_image(self, file_name):
        """
        全屏截图
        获取验证码图片，并保存到file_name中
        :param file_name:
        """
        self.driver.save_screenshot(file_name)
        # 定位验证码
        code_element = self.get_user_element("code_image")
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
        im = Image.open(file_name)
        # 将指定的某部分裁剪出来
        img = im.crop((left_x, left_y, right_x, right_y))
        img.save(file_name)

    def code_online(self, file_name):
        """
        将file_name中的验证码图片进行识别，用于注册时验证码的输入
        :return: 验证码字符串
        """
        self.get_code_image(file_name)
        r = ShowapiRequest("http://route.showapi.com/184-4", "144729", "e3e550c74b9d4e0b85c3889ce3ec3bfc")
        # ShowapiRequest 的第一个参数是万维易源网的url ，第二个参数是易源网上你个人的appId ， 第三个参数是易源网上的密钥

        r.addBodyPara("typeId", "35")  # typeId：表示识别几位数的图片验证码 ；35：'3'表示英数结合的验证码，'5'表示5位数的验证码   ； 31：一位数的验证码
        r.addBodyPara("convert_to_jpg", "0")
        r.addFilePara("image", file_name)  # 添加要识别验证码的图片
        res = r.post()
        # print(res.text)  # {"showapi_res_error":"","showapi_res_id":"6f0e4cdb977141b293ea12178ad3d37e","showapi_res_code":0,"showapi_res_body":{"Id":"5bac83cc-5637-4e2d-bc91-25a78b527241","Result":"ANLZZ","ret_code":0}}
        code_text = res.json()['showapi_res_body']['Result']  # 以json格式读取：showapi_res_body 下 Result 的值
        # print(text)  # 返回信息：ANLZZ (识别正确)
        return code_text

    def browser_quit(self):
        """
        关闭浏览器
        """
        self.driver.quit()

    def main(self):
        # 主程序
        # 用户名
        user_name = self.get_range_for_user()
        # 邮箱
        user_email = self.get_range_for_user() + '@qq.com'
        # 邮箱定位
        self.send_user_info("user_email", user_email)
        # 用户名
        self.send_user_info("user_name", user_name)
        # 密码
        self.send_user_info("user_password", "11111")
        # 验证码
        # 当前项目路径
        base_dir = os.path.dirname(os.path.abspath(__file__))
        # # 图片路径
        img_name= self.get_range_for_user() + '.png'
        file_name = os.path.join(base_dir, 'Image', img_name)
        print(file_name)
        # code_text = self.code_online(file_name)
        # print(code_text)
        self.send_user_info("code_text", "11111")
        # 注册
        self.get_user_element("register_button").click()
        code_text_error = self.get_user_element("code_text_error")
        if code_text_error is None:
            print("注册成功")
        else:
            print("注册失败")
            self.driver.save_screenshot(file_name)
        time.sleep(5)
        self.browser_quit()

if __name__ == "__main__":
    url = "http://www.5itest.cn/register"
    for i in range(2):
        registerfunction = RegisterFunction2(url, i)
        registerfunction.main()