import pandas as pd


data = pd.read_csv('dataset/train.csv', index_col='Unnamed: 0')
data.fillna(data['Age'].mean(), inplace=True)
data.to_csv('dataset/train.csv', index=False)

print('Ok')
