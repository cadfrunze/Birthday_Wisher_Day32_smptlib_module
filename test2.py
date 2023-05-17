import datetime as dt
import smtplib
import random

target = dt.datetime.now()

moment = dt.datetime.now()

user = 'test@test.test'
password = 'parola'
with open('./quotes.txt', 'r') as file:
    lista = file.readlines()

random_sentence = random.choice(lista)
print(random_sentence)


if moment.weekday() == target.weekday():
    with smtplib.SMTP('smtp.mail.yahoo.com') as conectiunea:
        conectiunea.starttls()
        conectiunea.login(user=user, password=password)
        conectiunea.sendmail(from_addr=user,
                             to_addrs='test@test.test',
                             msg=f'Subject:Test3\n\n{random_sentence}')