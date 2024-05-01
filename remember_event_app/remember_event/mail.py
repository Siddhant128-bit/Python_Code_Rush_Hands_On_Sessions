import datetime as dt
import time
import smtplib
import schedule
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(recipient_email, message_content, send_datetime):
    email_user = 'pdawadi20@gmail.com'
    email_password = 'uelk sjrn serw ghqd'
    subject = 'Reminder Mail'

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message_content, 'plain'))

    send_datetime_obj = dt.datetime.strptime(send_datetime, '%Y-%m-%dT%H:%M')
    time_difference = (send_datetime_obj - dt.datetime.now()).total_seconds()

    if time_difference > 0:
        time.sleep(time_difference)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_user, email_password)
        server.sendmail(email_user, recipient_email, msg.as_string())
        server.quit()

        print('Email sent')
    else:
        print('Invalid send_datetime')


# def wrapper_mail():
#     is_sent=False
#     def send_email():
#         email_user = 'pdawadi20@gmail.com'
#         server = smtplib.SMTP ('smtp.gmail.com', 587)
#         server.starttls()
#         server.login(email_user, 'uelk sjrn serw ghqd')
#         send_time = dt.datetime(2024,4,29)
#         #EMAIL
#         message = 'sending this from python!'
#         today = dt.datetime.today()
#         if send_time.date() == today.date():
#             server.sendmail(email_user, email_user, message)
#             is_sent = True
#         server.quit()

#     schedule.every().day.at("20:42").do(send_email)

#     while not is_sent:
#         schedule.run_pending()
#         time.sleep(1)


# send_time = dt.datetime(2024,4,29,20,24,0) # set your sending time in UTC
# time.sleep(send_time.timestamp() - time.time())
# send_email()
# print('email sent')
