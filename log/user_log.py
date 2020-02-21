import logging
import os
import datetime

class UserLog(object):

    def __init__(self):
        # 获取logger实例
        self.logger = logging.getLogger()
        # 指定日志的最低输出级别，默认为WARN级别
        self.logger.setLevel(logging.DEBUG)
        # 控制台输出日志
        # console = logging.StreamHandler()
        #文件输出日志
        #文件名
        log_name = datetime.datetime.now().strftime("%Y-%m-%d") + '.log'
        base_path = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_path, 'logs', log_name)
        print(file_path)
        self.file_handle = logging.FileHandler(file_path,mode='a', encoding='utf-8')
        self.file_handle.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s %(levelno)s:%(levelname)s-->%(filename)s-->%(module)s-->%(funcName)s-->%(lineno)d:%(message)s')
        self.file_handle.setFormatter(formatter)
        # 为logger添加的日志处理器
        # logger.addHandler(console)
        self.logger.addHandler(self.file_handle)
        # self.logger.debug("test123")
        # self.logger.info("info123")
        #关闭控制台
        # console.close()
        # self.file_handle.close()
        # 移除一些日志处理器
        # logger.removeHandler(console)
        # self.logger.removeHandler(self.file_handle)

    def get_logger(self):
        return self.logger

    def close_handle(self):
        self.file_handle.close()
        self.logger.removeHandler(self.file_handle)

if __name__ == '__main__':
    userlog = UserLog()
    log = userlog.get_logger()
    userlog.close_handle()