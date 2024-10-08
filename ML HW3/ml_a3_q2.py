# -*- coding: utf-8 -*-
"""ML_A3_q2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WjnIUEt4WTfQtfNMk9m6bqTijGvtf1cR
"""

import pandas as pd
import numpy as np
from sklearn.datasets import load_boston
import random
from sklearn import linear_model
from sklearn import preprocessing

boston_dataset = load_boston()
df = pd.DataFrame(boston_dataset.data, columns=boston_dataset.feature_names)
df['MEDV'] = boston_dataset.target
df.head()

x = df.drop(columns=['MEDV'])
x.shape

x = x.values #returns a numpy array
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
df = pd.DataFrame(x_scaled, columns=boston_dataset.feature_names)
df['MEDV'] = boston_dataset.target
df.head()

def get_subsets(train_ratio,x):
  nsamples = int(np.round(len(x)*0.8))
  ind = random.sample(range(len(x)),nsamples)
  ind = list(np.sort(ind))
  x_sub_train = x.iloc[ind]
  y_sub_train = x_sub_train['MEDV']
  x_sub_train = x_sub_train.drop(columns=['MEDV'])

  ind_test = []
  for i in range(len(x)):
    if i not in ind:
      ind_test.append(i)

  ind_test = list(np.sort(ind_test))
  x_sub_test = x.iloc[ind_test]
  y_sub_test = x_sub_test['MEDV'] 
  x_sub_test = x_sub_test.drop(columns=['MEDV'])   

  return x_sub_train, y_sub_train, x_sub_test, y_sub_test

x_train, y_train, x_test, y_test = get_subsets(0.8,df)

x_train.shape,y_train.shape,x_test.shape, y_test.shape

ridgeReg = linear_model.Ridge(alpha=0.01)
ridgeReg.fit(x_train,y_train)

scores = []
for i in range(0,10):
  x_train, y_train, x_test, y_test = get_subsets(0.8,df)
  ridgeReg = linear_model.Ridge(alpha=0.01, tol=1e-4)
  ridgeReg.fit(x_train,y_train)
  ridgeReg.predict(x_test)
  score = ridgeReg.score(x_test,y_test)
  scores.append(score)
mean_r2 = np.mean(scores)
print(f'Mean r-Squared value over 10 iterations = {mean_r2}')

