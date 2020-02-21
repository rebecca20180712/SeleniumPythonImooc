from base.find_element import FindElement


class RegisterPage(object):
    """获取元素所在位置"""
    def __init__(self, driver):
        self.fd = FindElement(driver)
    #获取邮箱元素
    def get_email_element(self):
        return self.fd.get_element("user_email")

    # 获取用户名元素
    def get_username_element(self):
        return self.fd.get_element("user_name")

    # 获取密码元素
    def get_password_element(self):
        return self.fd.get_element("user_password")

    # 获取验证码元素
    def get_code_element(self):
        return self.fd.get_element("code_text")

    # 获取注册按钮元素
    def get_button_element(self):
        return self.fd.get_element("register_button")

    # 获取邮箱错误元素
    def get_email_error_element(self):
        return self.fd.get_element("user_email_error")

    # 获取用户名错误元素
    def get_name_error_element(self):
        return self.fd.get_element("user_name_error")

    # 获取密码错误元素
    def get_password_error_element(self):
        return self.fd.get_element("user_password_error")

    # 获取验证码错误元素
    def get_code_error_element(self):
        return self.fd.get_element("code_text_error")

    def get_user_element(self, key):
        """
        定位用户信息，获取element
        :param key:配置文件中key
        :return:user_element
        """
        user_element = self.fd.get_element(key)
        return user_element

    def send_user_info(self, key, data):
        """
        输入用户信息
        :param key:配置文件中key
        :param data:文本框输入值
        """
        self.get_user_element(key).send_keys(data)