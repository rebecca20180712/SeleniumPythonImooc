import unittest
import os



class FirstCase01(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("这是所有case执行之前的前置")

    @classmethod
    def tearDownClass(cls):
        print("这是所有case执行之后的后置")

    def setUp(self):
        print("这是初始条件")

    def tearDown(self):
        print("这是结束设置")

    def testfirst01(self):
        print("这是第一条case")
    @unittest.skip("不执行第二条case")
    def testfirst02(self):
        print("这是第二条case")

    def testfirst03(self):
        print("这是第三条case")

if __name__ == "__main__":
    #用这种方法会执行所有的case，并且case的执行顺序是按数字的升序进行执行的
    # unittest.main()
    #只执行指定的case,用容器的方式，可以指定case执行的顺序
    suite = unittest.TestSuite()
    # suite.addTest(FirstCase01("testfirst02"))
    # suite.addTest(FirstCase01("testfirst01"))
    suite.addTest(FirstCase01("testfirst03"))
    unittest.TextTestRunner().run(suite)