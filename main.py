import smtplib

my_connection = 'test@test.test'
password = 'parola'
with smtplib.SMTP('smtp.mail.yahoo.com') as conectiunea:
    conectiunea.starttls()
    conectiunea.login(user=my_connection, password=password)
    conectiunea.sendmail(from_addr=my_connection,
                         to_addrs='test@test.test',
                         msg='Subject:Test\n\nTest Test'
                         )

