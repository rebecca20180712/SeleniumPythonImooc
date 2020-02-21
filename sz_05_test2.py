import pytesseract
from PIL import Image
import os

#当前项目路径
base_dir = os.path.dirname(os.path.abspath(__file__))
#图片路径
image_path = os.path.join(base_dir, 'Image', 'imooc.png')
#验证码路径
code_path = os.path.join(base_dir, 'Image', 'code.png')
# 测试的是pytesseract自带的图片，效果十分理想，完全没毛病
image = Image.open(code_path)
image = image.resize((500,500))
string = pytesseract.image_to_string(image)
print(string)
