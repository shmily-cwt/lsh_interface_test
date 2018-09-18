#coding:utf-8
import logging
import os
from common.commons import commonMethod
import readConfig

class Log:

    def __init__(self,filename):
        self.local_proDir = readConfig.proDir  #获取跟目录
        self.log_path = os.path.join(self.local_proDir,'test_log') #获取logpath路径
        self.local_time = commonMethod.getTime(self)
        self.log_out_path = os.path.join(self.log_path,filename+'output.log')

    def getLog(self,interface_name):
        logger = logging.getLogger(interface_name) #给logger一个名字可以方便知道日志从哪里打印的
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler(self.log_out_path)#处理输出日志的路径
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)#处理输出格式
        logger.addHandler(handler)
        return logger

# if __name__ == '__main__':
#     a = Log()
#     print a.local_proDir
#     print a.log_path
#     print a.log_out_path
#     logger = a.getLog('abc')
#     logger.info('this is first test')



