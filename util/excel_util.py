import xlrd
from xlutils.copy import copy
import os
import time


class ExcelUtil(object):

    def __init__(self, excel_path = None, index = None):
        """
        读取excel文件初始化
        :param excel_path: 文件的路径
        :param index:excel的第几个sheet
        """
        if excel_path is None:
            # # 当前项目路径
            self.base_dir = os.path.dirname(os.path.abspath('.'))
            # 图片路径
            self.excel_path = os.path.join(self.base_dir, 'config', 'keyword.xls')
        else:
            self.excel_path = excel_path
        if index is None:
            self.index = 0
        else:
            self.index = index
        # 打开excel文件
        self.data = xlrd.open_workbook(self.excel_path)
        # 定位到第index个sheet
        self.table = self.data.sheets()[self.index]
        # 获取行数
        # self.rows = self.table.nrows

    def get_data(self):
        """
        获取excel数据，按照每行一个list，添加到一个大的list里面
        :return:返回一个大的list
        """
        result = []
        rows = self.get_rows()
        if rows != None:
            for i in range(rows):
                row_data = self.table.row_values(i)
                result.append(row_data)
            return result
        return None

    def get_rows(self):
        """
        获取行数
        :return: 返回行数
        """
        rows = self.table.nrows
        if rows >=1:
            return rows
        return None

    def get_cell_value(self, row, col):
        """
        获取单元格数据
        :param x: 行（从0开始）
        :param y: 列（从0开始）
        :return: 单元格的值
        """
        if self.get_rows() > row:
            data = self.table.cell(row, col).value
            return data
        return None

    def write_value(self, row, col, value):
        """
        在excel中写入数据
        :param row: 行（从0开始）
        :param col: 列（从0开始）
        :param value: 写入的值
        """
        data = xlrd.open_workbook(self.excel_path)
        write_data = copy(data)
        write_data.get_sheet(0).write(row, col, value)
        write_data.save(self.excel_path)
        time.sleep(1)

if __name__ == '__main__':
    # # 当前项目路径
    # base_dir = os.path.dirname(os.path.abspath('.'))
    # pycharm执行路径
    # base_dir = os.path.dirname(os.path.abspath('.'))
    # jenkins执行路径
    base_dir = os.path.abspath('.')
    # 图片路径
    excel_path = os.path.join(base_dir, 'config', 'keyword.xls')
    ex = ExcelUtil(excel_path)
    print(ex.get_rows())
    print(ex.get_cell_value(0, 2))
    # ex.write_value(1, 7, "输入密码成功")