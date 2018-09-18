import os
import readConfig
from xml.etree import ElementTree as ET
class readXml:

    def __init__(self):
        self.base_path = readConfig.proDir
        #self.database = {}

    def readxml(self,filename):
        xml_path = os.path.join(self.base_path,"test_file",filename)
        print(xml_path)
        tree = ET.parse(xml_path)
        root = tree.getroot()
        #print(root)
        databases = {}
        for database in root.findall('database'):
            db_name = database.get('name')
            tables={}
            for table in database.getchildren():
                tb_name = table.get('name')
                sql={}
                for data in table.getchildren():
                    sql_id = data.get('id')
                    sql[sql_id] = data.text
                tables[tb_name] = sql
            databases[db_name] = tables
        return databases

    def get_sql(self,filename,database_name,table_name,sql_id):
        database_dict = readXml.readxml(self,filename)
        sql = database_dict.get(database_name).get(table_name).get(sql_id)
        return sql







if __name__ == '__main__':
    rx = readXml()

    sql = rx.get_sql('test.xml','newtest','newtable','select_num')
    print(sql)




