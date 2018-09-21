import unittest
import HTMLTestRunner
import HTMLTestReportCN

class Test_Unittest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_add(self):
        self.assertEqual(1+1,2,msg="1+1=2;pass")
        #print("1+1=2通过")
    def test_jian(self):
        self.assertEqual(3-2,2,msg="3-1=2;pass")
       # print("3-1=2通过")



def get_suit():
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(Test_Unittest('test_add'))
    suiteTest.addTest(Test_Unittest('test_jian'))
    return suiteTest
if __name__ == '__main__':
    #unittest.main()
    filePath = "C:\\Users\\yanchuanjie\\Desktop\\test_CN.html"
    fp = open(filePath,'wb')
    #生成报告的Title,描述
    runner = HTMLTestReportCN.HTMLTestRunner(
        stream=fp,
        title='自动化测试报告',
        description='详细测试用例结果',
        tester='chenwt'
        )
    #运行测试用例
    runner.run(get_suit())
    # 关闭文件，否则会无法生成文件
    fp.close()
