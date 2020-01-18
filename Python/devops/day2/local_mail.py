# from email.mime.text import MIMEText
# from email.header import Header
# import smtplib
#
# msg = MIMEText('This is a python email test.\n','plain','utf8')
# msg['From']=Header('root','utf8')
# msg['To']=Header('tom','utf8')
# msg['Subject']=Header('py test','utf8')
#
# smtp=smtplib.SMTP('127.0.0.1')
# smtp.sendmail('root',['tom','root'],msg.as_bytes())


from email.mime.text import MIMEText
from email.header import Header
import smtplib

msg=MIMEText('我是谁\n','plain','utf8')
msg['From']=Header('root','utf8')
msg['To']=Header('tom','utf8')
msg['Subject']=Header('会议记录','utf8')

smtp=smtplib.SMTP('127.0.0.1')
smtp.sendmail('root','tom',msg.as_bytes())








