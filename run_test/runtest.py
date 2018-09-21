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
    #report_path = os.path.join(readConfig.proDir,'test_report')
    #将测试报告放置到Tomcat下
    report_path = "D:\\apache-tomcat-8.5.33\\webapps\\Lsh_Interface_Test_Report"
    #print(report_path)
    local_time = commons.commonMethod().getTime()
    report_name = "LSH_"+local_time+"TestReport.html"
    #print(report_name)
    report = os.path.join(report_path,report_name)
    send_url = "http://192.168.13.56:8080"+report.split("webapps")[-1].replace("\\","/")
    return report,send_url
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
    #report_path = os.path.join(readConfig.proDir,'test_report')
    #将测试报告放置到Tomcat下
    report_path = "D:\\apache-tomcat-8.5.33\\webapps\\Lsh_Interface_Test_Report"
    report_file = commons.commonMethod().sortReport(report_path)
    local_time = commons.commonMethod().getTime()
    report_name = "LSH_"+local_time+"TestReport.html"
    send_report = os.path.join(report_path,report_file)
    #print(send_report)
    #configEmail.Email().sendEmail(send_report,report_name)
    return send_report,report_name
def get_email_tmpl(data_html,href_html):
    EMAIL_TMPL1 = """<html lang="zh-CN">

<head>
    <meta charset="utf-8">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <title>Test_Log</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<style type="text/css">
	.tftable {font-size:16px;color:#333333;width:80%;border-width: 1px;border-color: #729ea5;border-collapse: collapse;}
	.tftable th {font-size:16px;background-color:#acc8cc;border-width: 1px;padding-right: 8px;padding-top: 8px;padding-bottom: 8px;border-style: solid;border-color: #729ea5;}
	.tftable tr {background-color:#d4e3e5;}
	.tftable td {font-size:12px;border-width: 1px;padding: 8px;border-style: solid;border-color: #729ea5;}
	.tftable tr:hover {background-color:#ffffff;}


	.tftable1 {font-size:16px;color:#fbfbfb;width:50%;border-width: 1px;border-color: #686767;border-collapse: collapse;}
	.tftable1 th {font-size:16px;background-color:#171515;border-width: 1px;padding: 8px;border-style: solid;border-color: #686767;text-align:left;}
	.tftable1 tr {background-color:#171515;}
	.tftable1 td {font-size:12px;border-width: 1px;padding: 8px;border-style: solid;border-color: #686767;}
	<-- .tftable1 tr:hover {background-color:#666666;} -->
</style>
<body>
	<div width="100%" height="100%">
		<center>
			<div style="float:left;">
				<span style="float:left;">大家好:</span><br>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span>利星行接口自动化测试报告，详情如下：</span>
			</div>
			<center><br><br><br>
	</div>
	<div width="100%" height="100%">
		<center>
			<center>
				<h2>接口自动化测试报告</h2>
			</center>
			<hr>
			<table class="tftable1" border="1">
				<tr style="text-align:center;"><td>测试用例数</td><td>用例通过数</td><td>用例失败数</td><td>通过率</td></tr>
"""

    return EMAIL_TMPL1+data_html+href_html

if __name__ == '__main__':
    report,send_url = get_report_path()
    print(send_url)
    suit = get_testsuite()
    fp=open(report,'wb')
    #runner = unittest.TextTestRunner()
    runner=HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'利星行接口测试报告',
    description=u'用例执行情况：')
    result = runner.run(suit)
    email_path,report_name = get_email_path()
    # send_email_txt = email_tmpl % dict(
    #     count_total = str(result.success_count+result.failure_count+result.error_count),
    #     pass_case = str(result.success_count),
    #     failed_case = str(result.failure_count),
    #     tongguolv = str('%.2f'%(((result.success_count)/(result.success_count+result.failure_count+result.error_count))*100))+"%",
    #     report_lianjie = str(send_url)
    # )
    # print("count:",str(result.success_count+result.failure_count+result.error_count))
    # print("pass:",str(result.success_count))
    # print("fail",str(result.failure_count))
    # print("error:",str(result.error_count))
    # print("lv:",str('%.2f'%(((result.success_count)/(result.success_count+result.failure_count+result.error_count))*100)))
    EMAIL_TMPL2 = '<tr style="text-align:center;"><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr></table><br><div>' %(str(result.success_count+result.failure_count+result.error_count),str(result.success_count),str(result.failure_count),str('%.2f'%(((result.success_count)/(result.success_count+result.failure_count+result.error_count))*100))+"%")
    #print(EMAIL_TMPL2)
    EMAIL_TMPL3 = '<a href = "%s" target=_blank>报告详情链接</a></div>' %(send_url)
    #print(EMAIL_TMPL3)
    send_email_txt = get_email_tmpl(EMAIL_TMPL2,EMAIL_TMPL3)
    fp.close()
    configEmail.Email().sendEmail(email_path,send_email_txt,report_name)


