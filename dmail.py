import smtplib
from email.message import EmailMessage

def sendmail(to,subject,body):
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('sirishadasari1113gmail.com','yamw yack zros jtsx')
    msg = EmailMessage()
    msg['From']='datta@codegnan.com'
    msg['To'] = to
    msg['Subject'] = subject
    msg.set_content(body)
    server.send_message(msg)
    server.quit()


# sendmail('sumapriya@gmail.com','hi this is codegnan','Ur are from GEC how was the class going?')
# print('mailsended')