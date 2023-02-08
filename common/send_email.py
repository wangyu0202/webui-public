import smtplib
from email.mime.text import MIMEText
from email.header import Header


class Email(object):

    def __init__(self, failpath, failname):
        self.failpath = failpath
        self.failname = failname

    def s_email(self):
        s = smtplib.SMTP()
        host = 'smtp'
        s.connect(host=host, port=00)
        user = ''
        pwd = ''
        s.login(user=user, password=pwd)
        with open(self.failpath, 'r', encoding='utf-8') as f:
            content = f.read()
        msg = MIMEText(content, 'html')
        Subject = 'ui自动化测试报告'
        msg['Subject'] = Header(Subject, 'utf-8')
        msg['from'] = user
        receiver = ['xxx.com', 'xxx.com']
        msg.add_header('content-disposition', 'attachment', filename=self.failname)
        for to_addr in receiver:
            s.sendmail(user, to_addr, msg.as_string())


























# def send_email(failpath):
#     # 第一步：创建一个SMTP对象
#     s = smtplib.SMTP()
#
#     # 第二步：链接到SMTP服务器
#     host = 'smtp.163.com'
#     s.connect(host=host,port=25)
#
#     # 第三步：登录smtp服务器
#     user = 'wy1206422976@163.com'
#     pwd = 'wangyu123'
#     s.login(user=user , password=pwd)
#
#     # 构造一封邮件（读取HTML文件中的内容来进行发送）
#     # 打开要发送的文件，读取里面的内容
#     with open(failpath,'r',encoding='utf-8') as f:
#         content = f.read()
#
#     # 1、初始化邮件
#     msg = MIMEText(content,'html')
#
#     # 2、添加邮件主题
#     Subject = '接口自动化测试报告'
#     msg['Subject'] = Header(Subject,'utf-8')
#
#     # 3、添加收件人
#     msg['To'] = '1206422976@qq.com'
#
#     # 4、添加发件人
#     msg['From'] = 'wy1206422976@163.com'
#
#     # 5、添加附件
#     msg.add_header('content-disposition', 'attachment', filename=failpath)
#
#     # 6、发送邮件
#     s.send_message(msg,'wy1206422976@163.com','1206422976@qq.com')
