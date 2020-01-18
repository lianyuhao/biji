import getpass
from email.mime.text import MIMEText
from email.header import Header
import smtplib

def send_mail(text,sender,recievers,subject,server,passwd):
    msg=MIMEText(text,'plain','utf8')
    msg['From']=Header(sender,'utf8')
    msg['To']=Header(recievers[0],'utf8')
    msg['Subject']=Header(subject,'utf8')

    smtp=smtplib.SMTP()
    smtp.connect(server)
    smtp.login(sender,passwd)
    #smtp.starttls() # 如果服务器要求安全连接，打开此注释
    smtp.sendmail(sender,recievers,msg.as_bytes())

if __name__ == '__main__':
    text='python发送邮件测试 授权码:gvlpxjvggfavcaga\n'
    sender='464585640@qq.com'
    recievers=['464585640@qq.com','lianyuhao@icloud.com']
    subject='py邮件测试'
    server='smtp.qq.com'
    passwd=getpass.getpass()
    send_mail(text, sender, recievers, subject, server, passwd)
