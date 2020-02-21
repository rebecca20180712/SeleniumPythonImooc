import ddt
import unittest

A=[1,2,3,4,5]
B=[{"name":"xiaohai","sex":"male"},{"name":"xiaoming","sex":"female"}]
C=[[2,3],[10,11],[12,13]]
@ddt.ddt
class DataTest(unittest.TestCase):
    def setUp(self):
        print("这是初始化设置")

    def tearDown(self):
        print("这是结束设置")
    # @ddt.data(
    #      [1,2],
    #      [3,4],
    #      [5,6]
    #  )
    # @ddt.unpack
    # result = [[1, 2], [3, 4], [5, 6]]
    # @ddt.data(*result)
    # def test_addNum(self, result):
    #     a, b = result
    #     sum = a + b
    #     print(sum)
    # result = ({"a": 2, "b": 3}, {"c": 4, "d": 8}, {"e": 5, "f": 7})
    # @ddt.data(*result)
    # def test_print(self, a):
    #     print(a)
    # @ddt.data({"name": "xiaohai", "sex": "male"})
    # @ddt.data(*A)
    @ddt.data(*B)
    def test_ddt0(self, a):  # a可以任意命名，接收值,可以看做一个占位符
        print(a["sex"])


if __name__ == '__main__':
    unittest.main()