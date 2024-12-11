import pandas as pd


data = pd.read_csv('dataset/train.csv')
print(data.columns)
data = data.loc[:, ['Pclass', 'Sex', 'Age']]
print(data.columns)
data.to_csv('dataset/train.csv')

