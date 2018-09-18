import unittest
import requests
import json
import readConfig
import time
from common import commons,logger

class salesFunnelOperation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dates = commons.commonMethod().readExcel('Lsh_Interface.xlsx','Test_Sale_Funnel_Operation')
        #cls.dates_new = commons.commonMethod().readNewExcel('testcase.xlsx')
        cls.testUrl = cls.dates[0][0]
        cls.testmethod = cls.dates[1][0]
        cls.log = logger.Log('salesFunnelOperation')
        cls.logger = cls.log.getLog('test_salesFunnelOperation_interface')
    def test_a_select_fortime_all(self):
        '''测试销售漏斗运营表日期维度查询全量'''
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
        self.assertEqual(respones_json[0]['projectValue'],str(check_text),msg='验证通过')
        print("验证字段值为：projectValue")
        print(respones_json[0]['projectValue']+"="+str(check_text)+"\t"+"验证通过")
    def test_b_select_fordiyu_all(self):
        '''测试销售漏斗运营表地域维度查询全量'''
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
        self.assertEqual(respones_json[0]['projectValue'],str(check_text),msg='验证通过')
        print("验证字段值为：projectValue")
        print(respones_json[0]['projectValue']+"="+str(check_text)+"\t"+"验证通过")

    # def test_c_select_for(self):
    #     for index in range(len(self.dates_new)):
    #         casename = self.dates_new[index][0]
    #         test_url = self.dates_new[index][1]
    #         print(test_url)
    #         head = json.loads(self.dates_new[index][2])
    #         print(head)
    #         test_parameters = self.dates_new[index][3]
    #         print(test_parameters)
    #         status_code = self.dates_new[index][4]
    #         check_text = self.dates_new[index][5]
    #         print(check_text)
    #         respones = requests.post(url=test_url,data=test_parameters,headers=head)
    #         respones_json = respones.json()
    #         print("返回状态码:",respones.status_code)
    #         self.assertEqual(respones_json[0]['projectValue'],str(check_text),msg='验证通过')
    #         print(respones_json[0]['projectValue']+"="+str(check_text)+"\t"+"验证通过")
    def test_c_select_forpinpaichexi_all(self):
        '''测试销售漏斗运营表品牌车系维度查询全量'''
        casename = self.dates[5][0]
        self.logger.info('casename: %s'% casename)
        self.logger.info('request: %s' % self.testUrl)
        head = json.loads(self.dates[5][1])
        #print(type(head))
        parameters = self.dates[5][2]
        #print(parameters)
        self.logger.info('parameters: %s' % parameters)
        status_code = self.dates[5][3]
        check_text = self.dates[5][4]
        respones = requests.post(url=self.testUrl,data=parameters,headers=head)
        #print(respones.text)
        respones_json = respones.json()
        print("返回状态码:",respones.status_code)
        self.assertEqual(respones_json[0]['projectValue'],str(check_text),msg='验证通过')
        print("验证字段值为：projectValue")
        print(respones_json[0]['projectValue']+"="+str(check_text)+"\t"+"验证通过")

    @classmethod
    def tearDownClass(cls):
        pass


# if __name__ == "__main__":
#     unittest.main()

