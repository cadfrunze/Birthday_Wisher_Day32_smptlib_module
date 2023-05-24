##################### Extra Hard Starting Project ######################
import pandas as pd
import random
import smtplib
import datetime as dt

# 1. Update the birthdays.csv
data_birthdays = pd.read_csv('./birthdays.csv')
data_datetime = dt.datetime(year=2023, month=12, day=21)
month = data_datetime.month
day = data_datetime.day
today = (float(day), float(month))
new_dict = {(col['day'], col['month']): col for (index, col) in data_birthdays.iterrows()}

# 2. Check if today matches a birthday in the birthdays.csv
if today in new_dict:
    persoana_tinta = new_dict[today]
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    with open(f'./letter_templates/letter_{random.randint(1, 3)}.txt', 'r') as letter:
        scrisoarea = letter.read()
        scrisoarea = scrisoarea.replace('[NAME]', f'{persoana_tinta["name"]}')
        scrisoarea = scrisoarea.replace('Angela', 'Maryus')

    # 4. Send the letter generated in step 3 to that person's email address.
    # with smtplib.SMTP('smtp.test.test') as conectiunea:
    #     conectiunea.starttls()
    #     conectiunea.login(user='user_test@test.test', password='password_test')
    #     conectiunea.sendmail(to_addrs=persoana_tinta['email'],
    #                          from_addr='test@test.test',
    #                          msg=f'Subjet: Test\n\n{scrisoarea}')
