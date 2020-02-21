from selenium import webdriver
from selenium.webdriver.support import expected_conditions
import time
import random
import os
from PIL import Image
from ShowapiRequest import ShowapiRequest

#启动浏览器
driver = webdriver.Firefox()
#窗口最大化
driver.maximize_window()
driver.implicitly_wait(10)
#打开网页
driver.get("http://www.5itest.cn/register")
#打印页面的标题
print(driver.title)
# 判断页面的标题中是否有注册两字
is_live = expected_conditions.title_contains("注册")
print(is_live)
#产生随机数
random_num = ''.join(random.sample('1234567890abcdefg', 5))

#获取验证码的图片
#当前项目路径
base_dir = os.path.dirname(os.path.abspath(__file__))
#图片路径
image_path = os.path.join(base_dir, 'Image', 'imooc.png')
#验证码路径
code_path = os.path.join(base_dir, 'Image', 'code.png')
#全屏截图
driver.save_screenshot(image_path)
#定位验证码
# code_element= driver.find_element_by_xpath(".//*[@id='getcode_num']")
code_element = driver.find_element_by_id("getcode_num")
print(code_element.location)
print(code_element.size)
#定位左上角x值
left_x = code_element.location['x']
#定位左上角y值
left_y = code_element.location['y']
#定位右上角x值
right_x = code_element.size['width'] + left_x
#定位右上角y值
right_y = code_element.size['height'] + left_y
print(left_x, left_y, right_x, right_y)
# 使用PIL下的Image打开截图的imooc.png图片
im = Image.open(image_path)
# 将指定的某部分裁剪出来
img = im.crop((left_x, left_y, right_x, right_y))
img.save(code_path)
# image = Image.open(code_path)
# text = pytesseract.image_to_string(image)



r = ShowapiRequest("http://route.showapi.com/184-4","144729","e3e550c74b9d4e0b85c3889ce3ec3bfc" )
# ShowapiRequest 的第一个参数是万维易源网的url ，第二个参数是易源网上你个人的appId ， 第三个参数是易源网上的密钥

r.addBodyPara("typeId", "35")  #typeId：表示识别几位数的图片验证码 ；35：'3'表示英数结合的验证码，'5'表示5位数的验证码   ； 31：一位数的验证码
r.addBodyPara("convert_to_jpg", "0")
r.addFilePara("image", code_path) # 添加要识别验证码的图片
res = r.post()
print(res.text)  # {"showapi_res_error":"","showapi_res_id":"6f0e4cdb977141b293ea12178ad3d37e","showapi_res_code":0,"showapi_res_body":{"Id":"5bac83cc-5637-4e2d-bc91-25a78b527241","Result":"ANLZZ","ret_code":0}}
text = res.json()['showapi_res_body']['Result']# 以json格式读取：showapi_res_body 下 Result 的值
print(text) # 返回信息：ANLZZ (识别正确)







#邮箱定位
email = driver.find_element_by_xpath(".//*[@id='register_email']")
email.send_keys(random_num + '@qq.com')
#用户名
name = driver.find_element_by_xpath(".//*[@id='register_nickname']")
name.send_keys(random_num)
#密码
password = driver.find_element_by_xpath(".//*[@id='register_password']")
password.send_keys(random_num)
#验证码
code = driver.find_element_by_xpath(".//*[@id='captcha_code']")
code.send_keys(text)
#注册
register = driver.find_element_by_xpath(".//*[@id='register-btn']")
register.click()
time.sleep(5)
driver.quit()

