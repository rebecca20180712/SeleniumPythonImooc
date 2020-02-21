import unittest
import os

class RunCase(unittest.TestCase):

    def test_case01(self):
        path = os.path.dirname(os.path.abspath(__file__))
        print(path)
        suite = unittest.defaultTestLoader.discover(path, 'unittest_*.py')
        unittest.TextTestRunner().run(suite)
if __name__ == '__main__':
    unittest.main()