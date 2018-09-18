import os
import configparser

#获取当前文件绝对路径
proDir = os.path.split(os.path.realpath(__file__))[0]

#配置文件路径
configPath = os.path.join(proDir,'config.ini').replace('\\','/')

class readConfig:

    def __init__(self):
        # 实例化读取配置文件对象
        self.cf = configparser.ConfigParser()
        #读取配置文件
        self.cf.read(configPath,encoding='UTF-8')

    def getEmail(self,name):
        '''
        该方法获取EMAIL中数据
        '''
        value = self.cf.get('EMAIL',name)
        #print value
        return value

    def getDB(self,name):
        '''
        该方法获取DATABASE中数据
        '''
        value = self.cf.get('DATABASE',name)
        #print value
        return value

if __name__ == "__main__":
    rc = readConfig()
    print(rc.getEmail('receivers'))
    print(rc.getDB('sit_port'))
    # print (proDir)
    # print (configPath)

