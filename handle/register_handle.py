from page.register_page import RegisterPage
from util.get_code_value import GetCode


class RegisterHandle(object):
    """打开页面后自动输入相应信息"""

    def __init__(self, driver):
        self.driver = driver
        self.register_p = RegisterPage(self.driver)

    # 输入邮箱
    def send_user_email(self, email):
        # self.loger.info("输入的邮箱值是："+email)
        self.register_p.get_email_element().send_keys(email)

    # 输入用户名
    def send_user_name(self, username):
        # self.loger.info("输入的用户名是："+username)
        self.register_p.get_username_element().send_keys(username)

    # 输入密码
    def send_user_password(self, password):
        # self.loger.info("输入的密码是："+password)
        self.register_p.get_password_element().send_keys(password)

    # 输入验证码
    def send_user_code(self, code_name):
        # get_code_text = GetCode(self.driver)
        # code = get_code_text.code_online(code_name)
        code = code_name
        self.register_p.get_code_element().send_keys(code)

    # 获取文字信息
    def get_user_text(self, info, user_info):
        try:  # 容错处理
            if info == 'user_email_error':
                text = self.register_p.get_email_error_element().text  # 获取邮箱错误信息
            elif info == 'user_name_error':
                text = self.register_p.get_name_error_element().text  # 获取用户名错误信息
            elif info == 'user_password_error':
                text = self.register_p.get_password_error_element().text  # 获取用户密码错误信息
            else:
                text = self.register_p.get_code_error_element().text  # 获取验证码错误信息
        except:
            text = None
        return text

    # 点击注册按钮
    def click_register_button(self):
        self.register_p.get_button_element().click()

    # 获取注册按钮文字
    def get_register_btn_text(self):
        """如获取不到信息，表明页面已成功跳转"""
        return self.register_p.get_button_element().text