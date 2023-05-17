import datetime as dt
import smtplib

target = dt.datetime(year=2023, month=5, day=17, hour=1, minute=14)


sender_pass = 'parola'
user = 'test@test.test'


while True:
    moment = dt.datetime.now()
    if moment.year == target.year and moment.month == target.month and moment.hour == target.hour and moment.minute == target.minute:
        with smtplib.SMTP('smtp.mail.yahoo.com') as conectiunea:
            conectiunea.starttls()
            conectiunea.login(user=user, password=sender_pass)
            conectiunea.sendmail(from_addr=user,
                                 to_addrs='test@test.test',
                                 msg='Subject: Test din nou\n\nMerge?'
                                 )
        break
