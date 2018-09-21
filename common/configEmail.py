#coding:utf-8
import smtplib
from readConfig import readConfig
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

class Email:
    '''
    该类实现读取配置并提供发送邮件功能
    '''

    def __init__(self):
        #初始化数据
        self.host_mail = readConfig().getEmail('mail_host')
        self.username = readConfig().getEmail('mail_user')
        self.password = readConfig().getEmail('mail_pass')
        self.mail_port = readConfig().getEmail('mail_port')
        self.sender = readConfig().getEmail('sender')
        self.receivers = readConfig().getEmail('receivers')
        self.subject = readConfig().getEmail('subject')

    def get_receivers(self):
        send_receivers = self.receivers.split(',')
        return send_receivers

    def sendEmail(self,reportfile,email_content,filename):
        '''
        该方法实现发送邮件
        '''
        #创建一个带附件的实例
        message = MIMEMultipart()
        message['From'] = Header("接口自动化测试组", 'utf-8')
        message['To'] =  Header("各位同事及领导", 'utf-8')
        message['Subject'] = Header(self.subject, 'utf-8')
        message.attach(MIMEText(email_content, 'html', 'utf-8'))
        #构建邮件正文,
        #message = MIMEText('利星行接口测试报告，详情见附件！', 'plain', 'utf-8')
        #构造附件
        with open(reportfile,'rb') as f:
            att = MIMEText(f.read(), 'html','utf-8')
            att["Content-Type"] = 'application/octet-stream'
            # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
            att["Content-Disposition"] = 'attachment; filename=%s' %filename
            message.attach(att)
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.host_mail, int(self.mail_port))    # 25 为 SMTP 端口号
            smtpObj.login(self.username,self.password)
            smtpObj.sendmail(self.sender,Email.get_receivers(self), message.as_string())
            print(u"邮件发送成功")
            f.close()
        except smtplib.SMTPException as e:
            print(u"Error: 无法发送邮件",e)

# if __name__ == '__main__':
#     e = Email()
#     #print(Email().get_receivers())
#     #print(type(e.get_receivers()))
#     #print(e.host_mail)
#     e.sendEmail('D:\\pythonproject\\LSH_Interface_Test\\test_report\\LSH_20180821155338TestReport.html','LSH_TEST_REPORT.html')
