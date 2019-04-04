import smtplib
import email.mime.multipart
import email.mime.text

msg = email.mime.multipart.MIMEMultipart()
msg['Subject'] = '这是自动发送的邮件'
msg['From'] = 'xyz@163.com'
msg['To'] = 'xyz@qq.com'
content = '''
    你好，xiaoming
            这是一封自动发送的邮件。
        www.cs.com
'''
txt = email.mime.text.MIMEText(content)
msg.attach(txt)

smtp = smtplib.SMTP()
smtp.connect('smtp.163.com', '25')
smtp.login('xyz@163.com', 'password')
smtp.sendmail('xyz@163.com', 'xyz@qq.com', msg.as_string())
smtp.quit()
print('邮件发送成功email has send out !')