import datetime as dt
import time
import smtplib


###################################### Email Loop Automater ######################################

def send_email_group_a():
    email_user = '<Insert Email Username Here>'
    email_pass = '<Insert Email Password Here>'
    email_receiver = ["<Insert Receiving Email Here>"]
    email_provider_port = '<Insert Email Provider Port Without Quotations Here>' # Example: 487 for Gmail
    email_provider_server = '<Insert Email Provider Server Here>' # Example: smtp.gmail.com for Gmail
    server = smtplib.SMTP (email_provider_server, email_provider_port)
    server.starttls()
    server.login(email_user, email_pass)

    #EMAIL
    message = "<Insert Email Message Here>"
    server.sendmail(email_user, email_receiver, message)
    server.quit()

def send_email_group_a_at(send_time_group_a):
    time.sleep(send_time_group_a.timestamp() - time.time())
    send_email_group_a()
    print('Email Sent')

group_a_email_time = dt.datetime(2021,1,1,0,0,0) # set your sending time in UTC # Year, Month, Day, Hour, Minute, Second
interval_a = dt.timedelta(minutes=5) # set the interval for sending the email

send_time_group_a = group_a_email_time

while True:
    send_email_group_a_at(send_time_group_a)
    send_time_group_a = send_time_group_a + interval_a
