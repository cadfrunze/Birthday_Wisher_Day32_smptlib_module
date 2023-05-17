import smtplib
from functionalitati import aniversare, random_scrisoare
from tkinter import messagebox

# Configurarea continutului si trimiterea prin smtp

USER = 'test@test.test'
PASSWORD = 'parola'

expeditor = input('Numele expeditorului: ').capitalize()

nume_aniversar = aniversare() # Din functionalitati
scrisoarea = random_scrisoare() # Din functionalitati

with open(f'./data/{scrisoarea}.txt', 'r') as sablon:
    sablon_scrisoare = sablon.read()
    sablon_scrisoare = sablon_scrisoare.replace('[Name]', nume_aniversar)
    sablon_scrisoare = sablon_scrisoare.replace('[Expeditor]', expeditor)

# Transmiterea datelor @
with smtplib.SMTP('smtp.test.test') as conncection:
    conncection.starttls()
    conncection.login(user=USER, password=PASSWORD)
    try:
        conncection.sendmail(from_addr=USER,
                             to_addrs='test@test.test',
                             msg=f'Subject:De la {expeditor}\n\n{sablon_scrisoare}'
                             )
    except smtplib.SMTPServerDisconnected:
        messagebox.showerror(title='Eroare', message='Eroare nu s-a putut trimite!')
    else:
        with open(f'./save_data/Expeditor:{expeditor}, Continut: {scrisoarea}', 'w') as save_scrisoarea:
            save_scrisoarea.write(sablon_scrisoare)
        messagebox.showinfo(title='Succes', message='Date transmise cu succes!')
