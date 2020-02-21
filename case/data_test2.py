import unittest
import ddt


A=[1,2,3,4,5]
B=[{"name":"xiaohai","sex":"male"},{"name":"xiaoming","sex":"female"}]
C=[[2,3],[10,11],[12,13]]
@ddt.ddt#ddt是一个装饰器
class DataTest(unittest.TestCase):
    @ddt.data(*C)
    # @ddt.unpack#单独取C中[2,3]两个值
    def test_ddt1(self,a,b):
        print(a,b)
        print(a+b)



    @ddt.data({"name":"xiaohai","sex":"male"})
    @ddt.data(*A)
    @ddt.data(*B)
    def test_ddt0(self,a):#a可以任意命名，接收值,可以看做一个占位符
     print(a["sex"])

def main():
    dd = DataTest()
    dd.test_ddt1()

if __name__ == '__main__':
    main()