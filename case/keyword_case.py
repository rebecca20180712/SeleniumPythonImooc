from keywords.actionMethod import ActionMethod
from util.excel_util import ExcelUtil
import os


class KeywordCase(object):

     def run_main(self):
         self.action_method = ActionMethod()
         # 当前项目路径
         base_dir = os.path.dirname(os.path.abspath('.'))
         # 图片路径
         excel_path = os.path.join(base_dir, 'config', 'keyword.xls')
         ex = ExcelUtil(excel_path)
         # 获取行数
         rows = ex.get_rows()
         #判断行数
         if rows:
             for row in range(1, rows):
                 is_run = ex.get_cell_value(row, 3)
                 if is_run == 'yes':
                     method = ex.get_cell_value(row, 4)
                     send_value = ex.get_cell_value(row, 5)
                     handle_value = ex.get_cell_value(row, 6)
                     except_result_method = ex.get_cell_value(row, 7)
                     except_result = ex.get_cell_value(row, 8)
                     #''而不是None
                     self.run_method(method ,send_value, handle_value)
                     if except_result_method:
                         except_value = self.get_except_result_value(except_result)
                         if except_value[0] == 'text':
                             result = self.run_method(except_result_method)
                             if except_value[1] in result:
                                 ex.write_value(row, 9, "pass")
                             else:
                                 ex.write_value(row, 9, "fail")
                         elif except_value[0] == 'element':
                             result = self.run_method(except_result_method, except_value[1])
                             if result:
                                 ex.write_value(row, 9, "pass")
                             else:
                                 ex.write_value(row, 9, "fail")


     def get_except_result_value(self, except_result):
         """
            获取预期结果的值
         :param except_result: excel中的预期结果值
         :return: 返回的是一个列表
         """
         return except_result.split('=')

     def run_method(self,method ,send_value = '', handle_value = ''):
         method_value = getattr(self.action_method, method)
         if send_value == '' and handle_value != '':
             result = method_value(handle_value)
         elif send_value == '' and handle_value == '':
             result = method_value()
         elif send_value != '' and handle_value == '':
             result = method_value(send_value)
         elif send_value != '' and handle_value != '':
             result = method_value(handle_value, send_value)
         return result

if __name__ == '__main__':
    kc = KeywordCase()
    kc.run_main()



