import pandas as pd


def set_ohe(arg):
    return 0 if arg == 'male' else 1


data = pd.read_csv('dataset/train.csv')
data['Sex'] = data['Sex'].apply(set_ohe)
data.to_csv('dataset/train.csv')
