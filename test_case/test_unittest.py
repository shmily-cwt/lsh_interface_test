import unittest
import HTMLTestRunner

class Test_Unittest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_add(self):
        assert (1+2) == 3

    def test_jian(self):
        assert (3-1) == 2



# if __name__ == '__main__':
#     #unittest.main()
