#coding:utf-8
import unittest
import readConfig
import os
import time
from test_case import test_submitOrder
from common import commons
from common import configEmail
import HTMLTestRunner

def get_report_path():
    #本地路径
    report_path = os.path.join(readConfig.proDir,'test_report')
    #将测试报告放置到Tomcat下
    #report_path = "D:\\apache-tomcat-8.5.33\\webapps\\Lsh_Interface_Test_Report"
    #print(report_path)
    local_time = commons.commonMethod().getTime()
    report_name = "LSH_"+local_time+"TestReport.html"
    #print(report_name)
    report = os.path.join(report_path,report_name)
    return report
def get_testsuite():

    suit = unittest.TestSuite()
    '''一个一个添加
    suit.addTest(test_submitOrder.submitOrder('test_a_null'))
    suit.addTest(test_submitOrder.submitOrder('test_b_one'))
    '''
    #查找case路径下所有的测试用例必须以test开头命名
    case_path = os.path.join(readConfig.proDir,'test_case')
    discover = unittest.defaultTestLoader.discover(case_path,pattern='test*.py',top_level_dir=None)
    suit.addTest(discover)
    return suit
def get_email_path():
    report_path = os.path.join(readConfig.proDir,'test_report')
    #将测试报告放置到Tomcat下
    report_path = "D:\\apache-tomcat-8.5.33\\webapps\\Lsh_Interface_Test_Report"
    report_file = commons.commonMethod().sortReport(report_path)
    local_time = commons.commonMethod().getTime()
    report_name = "LSH_"+local_time+"TestReport.html"
    send_report = os.path.join(report_path,report_file)
    #print(send_report)
    #configEmail.Email().sendEmail(send_report,report_name)
    return send_report,report_name
if __name__ == '__main__':
    report = get_report_path()
    suit = get_testsuite()
    #email_path,report_name = get_email_path()
    fp=open(report,'wb')
    #runner = unittest.TextTestRunner()
    runner=HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'利星行接口测试报告',
    description=u'用例执行情况：')
    runner.run(suit)
    fp.close()
   # configEmail.Email().sendEmail(email_path,report_name)


