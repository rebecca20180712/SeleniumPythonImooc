import configparser
import os


class ReadIni(object):

    def __init__(self, file_name = None, node = None):
        # 初始化
        if file_name is None:
            base_path = os.path.dirname(os.path.abspath('.'))
            self.file_name = os.path.join(base_path, 'config', 'LocalElement.ini')
        else:
            self.file_name = file_name
        if node is None:
            # 配置文件中的某个节点
            self.node = 'RegisterElement'
        else:
            self.node = node
        self.cf = self.load_ini()
        # print(self.file_name)

    def load_ini(self):
        # 加载文件
        cf = configparser.ConfigParser()
        cf.read(self.file_name)
        return cf

    def get_value(self, key):
        # 获取配置文件中key的value值
        data = self.cf.get(self.node, key)
        # print(data)
        return data


def main():
    ri = ReadIni()
    ri.get_value('user_name')

if __name__ == '__main__':
    main()