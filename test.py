import datetime as dt

acest_moment = dt.datetime.now()

an = acest_moment.year
luna = acest_moment.month
zi = acest_moment.day
ora = acest_moment.hour
minute = acest_moment.minute


with open('./work_log.txt', 'a') as file1:
    file1.writelines(f'{zi}/{luna}/{an}|{ora}:{minute}\n')
