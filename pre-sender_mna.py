import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from_addr='SENDER\'S NAME'
to_addr=['XXXXX']
#to_addr=['A1','A2']
msg=MIMEMultipart()
msg['From']=from_addr
msg['To']=" ,".join(to_addr)
msg['subject']='SUBJECT'

body='BODY'

msg.attach(MIMEText(body,'plain'))

email='ACCOUNT'
password='PASS'

mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login(email,password)
text=msg.as_string()
mail.sendmail(from_addr,to_addr,text)
mail.quit()