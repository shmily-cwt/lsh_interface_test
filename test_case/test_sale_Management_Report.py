import unittest
import requests
import json
import readConfig
import time
from common import commons,logger

class salesManagementReport(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dates = commons.commonMethod().readExcel('Lsh_Interface.xlsx','Sales_Management_Report')
        #cls.dates_new = commons.commonMethod().readNewExcel('testcase.xlsx')
        cls.testUrl = cls.dates[0][0]
        cls.testmethod = cls.dates[1][0]
        cls.log = logger.Log('salesManagementReport')
        cls.logger = cls.log.getLog('test_ManagementReport_interface')
    def test_a_select_fortime_all(self):
        '''测试销售管理报表日期维度查询全量'''
        casename = self.dates[3][0]
        self.logger.info('casename: %s'% casename)
        self.logger.info('request: %s' % self.testUrl)
        head = json.loads(self.dates[3][1])
        parameters = self.dates[3][2]
        self.logger.info('parameters: %s' % parameters)
        status_code = self.dates[3][3]
        check_text = self.dates[3][4]
        respones = requests.post(url=self.testUrl,data=parameters,headers=head)
        respones_json = respones.json()
        print("返回状态码:",respones.status_code)
        self.assertEqual(respones_json[0]['twoIndexNameOrder'],str(check_text),msg='验证通过')
        print("验证字段值为：twoIndexNameOrder")
        print(respones_json[0]['twoIndexNameOrder']+"="+str(check_text)+"\t"+"验证通过")
    def test_b_select_fordiyu_all(self):
        '''测试销售管理报表地域维度查询全量'''
        casename = self.dates[4][0]
        self.logger.info('casename: %s'% casename)
        self.logger.info('request: %s' % self.testUrl)
        head = json.loads(self.dates[4][1])
        parameters = self.dates[4][2]
        self.logger.info('parameters: %s' % parameters)
        status_code = self.dates[4][3]
        check_text = self.dates[4][4]
        respones = requests.post(url=self.testUrl,data=parameters,headers=head)
        respones_json = respones.json()
        print("返回状态码:",respones.status_code)
        self.assertEqual(respones_json[0]['twoIndexNameOrder'],str(check_text),msg='验证通过')
        print("验证字段值为：twoIndexNameOrder")
        print(respones_json[0]['twoIndexNameOrder']+"="+str(check_text)+"\t"+"验证通过")



    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == "__main__":
    unittest.main()

