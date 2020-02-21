from PIL import Image
from ShowapiRequest import ShowapiRequest
from page.register_page import RegisterPage
from selenium import webdriver
import time


class GetCode:
    """获取验证码图片，解析验证码图片并返回验证码值"""
    def __init__(self, driver):
        self.driver = driver

    def get_code_image(self, code_name):
        """
        全屏截图
        获取验证码图片，并保存到file_name中
        :param file_name:
        """
        self.driver.save_screenshot(code_name)
        # 定位验证码
        code_element = RegisterPage(self.driver).get_user_element("code_image")
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
        im = Image.open(code_name)
        # 将指定的某部分裁剪出来
        img = im.crop((left_x, left_y, right_x, right_y))
        img.save(code_name)
        time.sleep(2)

    def code_online(self, code_name):
        """
            将file_name中的验证码图片进行识别，用于注册时验证码的输入
            :return: 验证码字符串
        """
        self.get_code_image(code_name)
        r = ShowapiRequest("http://route.showapi.com/184-4", "144729", "e3e550c74b9d4e0b85c3889ce3ec3bfc")
        # ShowapiRequest 的第一个参数是万维易源网的url ，第二个参数是易源网上你个人的appId ， 第三个参数是易源网上的密钥

        r.addBodyPara("typeId", "35")  # typeId：表示识别几位数的图片验证码 ；35：'3'表示英数结合的验证码，'5'表示5位数的验证码   ； 31：一位数的验证码
        r.addBodyPara("convert_to_jpg", "0")
        r.addFilePara("image", code_name)  # 添加要识别验证码的图片
        res = r.post()
        # print(res.text)  # {"showapi_res_error":"","showapi_res_id":"6f0e4cdb977141b293ea12178ad3d37e","showapi_res_code":0,"showapi_res_body":{"Id":"5bac83cc-5637-4e2d-bc91-25a78b527241","Result":"ANLZZ","ret_code":0}}
        code_text = res.json()['showapi_res_body']['Result']  # 以json格式读取：showapi_res_body 下 Result 的值
        # print(text)  # 返回信息：ANLZZ (识别正确)
        time.sleep(2)
        return code_text

if __name__ == "__main__":
    driver = webdriver.Firefox()
    getcode = GetCode(driver)
    getcode.get_code_image("D:/pycharm_file/自动化实战/Image/error.png")