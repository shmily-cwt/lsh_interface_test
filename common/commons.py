#coding: utf-8
'''
该类实现所有公用方法
'''
import os,json
import time
import xlrd
import readConfig
class commonMethod:

    def __init__(self):
        self.localDir = os.path.join(readConfig.proDir,'common').replace('\\','/')

    def readExcel(self,excelname,sheet_name):
        '''
        该方法实现读取接口文档并传入Excel表名称返回数据的全部对象
        获取后需对数据进行处理返回为list类型
        '''
        datas = []
        filePath = os.path.join(readConfig.proDir,'test_file')
        excelpath = os.path.join(filePath,excelname).replace('\\','/')
        excel_data = xlrd.open_workbook(excelpath)
        table_data = excel_data.sheet_by_name(sheet_name)
        table_nrows = table_data.nrows
        # print table_nrows
        for i in range(0,table_nrows):
            row_value = table_data.row_values(i)
            datas.append(row_value)
        test_url = datas[0][0]
        test_method = datas[1][0]
        # print test_url,'\n',test_method
        # print datas
        return datas

    def readNewExcel(self,excelname):
        '''
        该方法实现读取接口文档并传入Excel表名称返回数据的全部对象
        获取后需对数据进行处理返回为list类型,针对上一模板进行修改
        '''
        datas_new = []
        filePath = os.path.join(readConfig.proDir,'test_file')
        excelpath = os.path.join(filePath,excelname).replace('\\','/')
        excel_data = xlrd.open_workbook(excelpath)
        table_data = excel_data.sheets()[0]
        table_nrows = table_data.nrows
        # print table_nrows
        for i in range(1,table_nrows):
            row_value = table_data.row_values(i)
            datas_new.append(row_value)
        test_url = datas_new[0][0]
        test_method = datas_new[1][0]
        # print test_url,'\n',test_method
        # print datas
        return datas_new

    def subStr(self,allStr,frontStr,afterStr):
        '''
        该方法实现字符串分割传入想获取的字符的前一个字符和后一个字符
        返回中间的字符，返回类型为str类型
        '''
        # if frontStr == '':
        #     result = allStr.split(afterStr)[0]
        #     return result
        # if afterStr == '':
        #     result = allStr.split(frontStr)[1]
        #     return result
        # else:
        result = allStr.split(frontStr)[1].split(afterStr)[0]
        # print result1
        # print type(result1)
        # result = result1.split(afterStr)[0]
        return result

    def getTime(self):
        '''
        该方法实现获取系统时间，根据需求返回不同格式的时间戳
        可以实现文件命名使用等，返回多个值
        '''
        now_time = time.strftime("%Y%m%d%H%M%S",time.localtime())
        return now_time

    def sortReport(self,filepath):
        '''
        该方法实现测试报告的排序返回最新的测试报告
        传入测试报告路径返回最新的测试报告路径
        '''
        #返回路径下所有的文件  list类型
        #print(filepath)
        lists = os.listdir(filepath)
        #对返回的lists中文件和文件夹按照时间进行排序
        lists.sort(key = lambda fn: os.path.getmtime(filepath+"\\"+fn))
        new_file = os.path.join(filepath,lists[-1])
        return new_file



#if __name__ == '__main__':
    # print(readConfig.proDir)
    # ct = commonMethod()
    # #ct.readExcel('test_submitOrder.xlsx')
    # a = {
    # "resCode":"00100000",
    # "obj":"[{\"id\":1,\"udPeriod\":12,\"doudouLevel\":\"103\",\"ruleId\":1,\"udGrowthValue\":\"500\"},{\"id\":2,\"udPeriod\":12,\"doudouLevel\":\"104\",\"ruleId\":1,\"udGrowthValue\":\"2000\"},{\"id\":3,\"udPeriod\":12,\"doudouLevel\":\"105\",\"ruleId\":1,\"udGrowthValue\":\"10000\"},{\"id\":4,\"udPeriod\":12,\"doudouLevel\":\"106\",\"ruleId\":1,\"udGrowthValue\":\"20000\"},{\"id\":5,\"udPeriod\":12,\"doudouLevel\":\"107\",\"ruleId\":1,\"udGrowthValue\":\"40000\"},{\"id\":6,\"udPeriod\":12,\"doudouLevel\":\"108\",\"ruleId\":1,\"udGrowthValue\":\"70000\"},{\"id\":7,\"udPeriod\":12,\"doudouLevel\":\"109\",\"ruleId\":1,\"udGrowthValue\":\"100000\"}]"
    # }
    # e = json.dumps(a)
    # print e
    # b = '"res'
    # c = '":'
    # ct.subStr(e,b,c)
    # filepath = os.path.join(readConfig.proDir,'test_report')
    # ct.sortReport(filepath)

