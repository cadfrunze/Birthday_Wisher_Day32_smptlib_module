import pandas as pd
import random
import datetime as dt

SCRISORI = ['scrisoarea1', 'scrisoarea2', 'scrisoarea3']


def aniversare():
    """Functie cautare/confirmare zi nastere"""
    data = pd.read_csv('./data/data.csv')
    prezent = dt.datetime.now()
    prezent_luna = prezent.month
    prezent_zi = prezent.day
    data_luna = data[data.luna == prezent_luna]
    data_nume = data_luna[data_luna.day == prezent_zi]
    numele = ''.join(data_nume.name)
    return numele


def random_scrisoare():
    """ALegerea random unei scrisori"""
    scrisoarea = random.choice(SCRISORI)
    return scrisoarea
