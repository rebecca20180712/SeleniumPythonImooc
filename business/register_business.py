from handle.register_handle import RegisterHandle


class RegisterBusiness:
    """测试注册页面form表单功能情况"""

    def __init__(self, driver):
        self.register_h = RegisterHandle(driver)

    def user_base(self, email, name, password, code_name):
        self.register_h.send_user_email(email)
        self.register_h.send_user_name(name)
        self.register_h.send_user_password(password)
        self.register_h.send_user_code(code_name)
        self.register_h.click_register_button()

    def register_succes(self):
        if self.register_h.get_register_btn_text() == None:
            # 注册成功
            return True
        else:
            return False

    # 唯一case
    def register_function(self, email, name, password, code_name, asserterror, asserttext):
        self.user_base(email, name, password, code_name)
        if self.register_h.get_user_text(asserterror, asserttext) == None:
            # print("无错误，邮箱检验不成功")
            return False
        else:
            return True

    # 邮箱错误
    def login_email_error(self, email, name, password, code_name):
        self.user_base(email, name, password, code_name)
        if self.register_h.get_user_text('user_email_error', "请输入有效的电子邮件地址") == None:
            # print("邮箱输入无错误，case检验不成功")
            return False
        else:
            return True

    def login_name_error(self, email, name, password, code_name):
        self.user_base(email, name, password, code_name)
        if self.register_h.get_user_text('user_name_error', "字符长度必须大于等于4，一个中文字算2个字符") == None:
            # print("用户名检验不成功")
            return False
        else:
            return True

    # 密码错误
    def login_password_error(self, email, name, password, code_name):
        self.user_base(email, name, password, code_name)
        if self.register_h.get_user_text('password_error', "最少需要输入 5 个字符") == None:
            # print("密码检验不成功")
            return False
        else:
            return True

    # 验证码错误
    def login_code_error(self, email, name, password, code_name):
        self.user_base(email, name, password, code_name)
        if self.register_h.get_user_text('code_text_error', "验证码错误") == None:
            # print("验证码检验不成功")
            return False
        else:
            return True