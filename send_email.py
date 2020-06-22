from email.mime.text import MIMEText
import smtplib

def send_email(email, height,average_height):
    from_email="testingududud@gmail.com"
    from_password="test1234!"
    to_email=email

    subject="Height Data"
    message="Hey there, your height is <strong>%s</strong>. Average height of all is %s" %(height, average_height)

    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
