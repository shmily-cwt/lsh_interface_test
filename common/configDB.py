import pymysql
from readConfig import readConfig
from common import logger
from  sshtunnel import *
from decimal import *

class DB:

    def __init__(self):
        self.sit_host = readConfig().getDB('sit_host')
        self.sit_username = readConfig().getDB('sit_username')
        self.sit_password = readConfig().getDB('sit_password')
        self.sit_port = readConfig().getDB('sit_port')
        self.sit_db_name = readConfig().getDB('sit_db_name')
        self.environment = readConfig().getDB('environment')
        self.ssh_address_or_host= readConfig().getDB('ssh_address_or_host')
        self.ssh_address_port = readConfig().getDB('ssh_address_port')
        self.ssh_username = readConfig().getDB('ssh_username')
        self.ssh_password = readConfig().getDB('ssh_password')
        self.demo_host = readConfig().getDB('demo_host')
        self.demo_username = readConfig().getDB('demo_username')
        self.demo_password = readConfig().getDB('demo_password')
        self.demo_db_name = readConfig().getDB('demo_db_name')
        self.demo_port = readConfig().getDB('demo_port')
        self.log = logger.Log('Connect_DB')
        self.mylog = self.log.getLog('ConnectDB_LOG')

    def connect_DB(self):
        '''创建数据库方法'''

        if self.environment == 'Demo':
            #print(self.ssh_address_or_host,self.ssh_address_port,self.ssh_username,self.ssh_password,self.demo_host,self.demo_port)
            try:
                server = SSHTunnelForwarder(
                ssh_address_or_host = (self.ssh_address_or_host,int(self.ssh_address_port)),  # 指定ssh登录的跳转机的address
                ssh_username = self.ssh_username,  # 跳转机的用户
                ssh_password = self.ssh_password,  # 跳转机的密码
                remote_bind_address = (self.demo_host,int(self.demo_port)))
                server.start()
                self.mylog.info("demo数据库跳板机创建成功")
                #print("连接跳板机成功")
            except BaseException as e:
                self.mylog.info("demo数据库跳板机创建失败:",e)
                #print("连接跳板机失败")
            try:
                db = pymysql.connect(host=self.demo_host,
                                     user=self.demo_username,
                                     passwd=self.demo_password,
                                     db=self.demo_db_name,
                                     port=server.local_bind_port)

                self.mylog.info("demo数据库连接成功")
                #print("连接成功")
                return db,server
            except BaseException as e:
                self.mylog.info("demo数据连接失败",e)
                #print("连接失败",e)

        elif self.environment == 'Sit':
            server = False
            #print(self.sit_host,self.sit_username,self.sit_password,self.sit_db_name,self.sit_port)
            try:
                db = pymysql.connect(host=self.sit_host,
                                     user=self.sit_username,
                                     passwd=self.sit_password,
                                     db=self.sit_db_name)
                self.mylog.info("测试数据库连接成功")
                #print("连接成功")
                return db,server
            except BaseException as e:
                #print("连接失败",e)
                self.mylog.info("测试数据库连接失败",e)
        else:
            self.mylog.info("数据库配置配置错误，请检查配置文件。")
            #print("配置错误")

    def implement_sql(self,sql):
        '''执行sql语句方法'''
        db,server = DB.connect_DB(self)
        if server == False:
            try:
                cursors = db.cursor()
                cursors.execute(sql)
                data = cursors.fetchall()
                cursors.close()
                db.close()
                return data
            except BaseException as e:
                self.mylog.info("数据库可能没连上。",e)


        else:
            try:
                cursors = db.cursor()
                cursors.execute(sql)
                data = cursors.fetchall()
                cursors.close()
                db.close()
                server.close()
                return data
            except BaseException as e:
                self.mylog.info("数据库可能没连上。",e)




# if __name__ == '__main__':
#     db = DB()
#     sql = "SELECT * FROM `lsh车型` WHERE `Variant` = '2314571     CN5'"
#     db.implement_sql(sql)