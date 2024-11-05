import pickle

import pandas as pd


with open('../model.pkl', mode='rb') as f:
    loaded_model = pickle.load(f)

data_test = pd.read_csv('../data_test.csv')
X_test = data_test[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch']].values

print(loaded_model.predict(X_test[0:1]))