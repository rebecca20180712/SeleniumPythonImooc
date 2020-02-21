from selenium import  webdriver
import time
import os
from PIL import Image
from ShowapiRequest import ShowapiRequest

import pytesseract
#截图验证码时，电脑的分辨率应设置为100%，不然截取不到验证码
driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://www.5itest.cn/register")
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
image = Image.open(code_path)
# image = image.resize((320, 480) ,Image.ANTIALIAS)
# image = Image.open(r"C:\Users\34518\Desktop\1.png")
# text = pytesseract.image_to_string(image)
# print("text:%s" % text)


r = ShowapiRequest("http://route.showapi.com/184-4","144729","e3e550c74b9d4e0b85c3889ce3ec3bfc" )
# ShowapiRequest 的第一个参数是万维易源网的url ，第二个参数是易源网上你个人的appId ， 第三个参数是易源网上的密钥

r.addBodyPara("typeId", "35")  #typeId：表示识别几位数的图片验证码 ；35：'3'表示英数结合的验证码，'5'表示5位数的验证码   ； 31：一位数的验证码
r.addBodyPara("convert_to_jpg", "0")
r.addFilePara("image", code_path) # 添加要识别验证码的图片
res = r.post()
print(res.text)  # {"showapi_res_error":"","showapi_res_id":"6f0e4cdb977141b293ea12178ad3d37e","showapi_res_code":0,"showapi_res_body":{"Id":"5bac83cc-5637-4e2d-bc91-25a78b527241","Result":"ANLZZ","ret_code":0}}
text = res.json()['showapi_res_body']['Result']# 以json格式读取：showapi_res_body 下 Result 的值
print(text) # 返回信息：ANLZZ (识别正确)

time.sleep(3)
driver.quit()

