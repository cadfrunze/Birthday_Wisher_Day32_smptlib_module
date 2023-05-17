import pandas as pd

data = {
    'name': ['Tata', 'Mama', 'Frate_Mare', 'Frate_Mic'],
    'day': [9, 17, 14, 27],
    'luna': [5, 5, 10, 8],
}

data_csv = pd.DataFrame(data)
data_csv.to_csv('./data/data.csv', index=False)
