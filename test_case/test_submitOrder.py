#coding:utf-8
import unittest
import requests
import json
import readConfig
from common import commons,logger

class submitOrder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dates = commons.commonMethod().readExcel('test_submitOrder.xlsx')
        cls.testUrl = cls.dates[0][0]
        cls.testmethod = cls.dates[1][0]
        cls.log = logger.Log('submitOrder')
        cls.logger = cls.log.getLog('test_SubmitOrder_interface')

    def test_a_null(self):
        '''测试入参为空'''
        casename = self.dates[3][0]
        self.logger.info('casename: %s'% casename)
        self.logger.info('request: %s' % self.testUrl)
        heards = json.dumps(self.dates[3][1])
        parameters = json.dumps(self.dates[3][2])
        self.logger.info('parameters: %s' % parameters)
        status_code = self.dates[3][3]
        check_text = self.dates[3][4]
        result = requests.post(self.testUrl,data=parameters).text
        self.logger.info('response: % s' % result)
        print(result)

    def test_b_one(self):
        '''测试一个入参'''
        casename = self.dates[4][0]
        print(casename)
        headers = json.loads(self.dates[4][1])
        parameters = json.dumps(self.dates[4][2])
        status_code = self.dates[4][3]
        check_text = self.dates[4][4]
        result = requests.post(self.testUrl,headers=headers,data=parameters).json()
        print(result)
        self.assertEqual(result['message'],u'核销明细查询成功')

    @classmethod
    def tearDownClass(cls):
        pass

# if __name__ == '__main__':
#     unittest.main()