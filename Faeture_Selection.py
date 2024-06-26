# -*- coding: utf-8 -*-
"""

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ODt8qWKf6fSkIbBGNK3IvyNLuZOYGsOm

## Feature Selection on semi-conductor Dataset


Dataset Link : https://archive.ics.uci.edu/ml/datasets/SECOM

### `Intially accuracy was 84% after applying feature Selection accuracy is 91% and intitally my dataset have 592 columns and after feature Selection 100 columns.`
"""

import pandas as pd

data = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vQtBXo5cBnDsM2fmfHPm6u72KGUS5FjPHNGMxOfYjA9-CAhmnRpwkIw_rOR3sANJIToiUU__6fbBvig/pub?gid=572763137&single=true&output=csv")

data.info()

data.head()

data.isnull().sum().sum()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np

data = data.drop('Time',axis=1)

for column in data.columns:
  min_value = data[column].min()
  max_value = data[column].max()

  random_values = np.random.uniform(min_value,max_value,size=data[column].isnull().sum())
  random_series = pd.Series(random_values,index=data[column][data[column].isnull()].index)

  data[column].fillna(random_series,inplace=True)

X = data.drop('Pass/Fail',axis=1)
y = data['Pass/Fail']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

print(X_train.shape)
print(X_test.shape)

log_reg = LogisticRegression(max_iter=10000)
log_reg.fit(X_train,y_train)

y_pred = log_reg.predict(X_test)

accuracy = accuracy_score(y_test,y_pred)
print("Test Accuracy",accuracy)

from sklearn.feature_selection import VarianceThreshold, SelectKBest, chi2, f_classif
from scipy.stats import pearsonr

duplicated_cols = data.columns[data.T.duplicated()]
data = data.drop(columns=duplicated_cols)

X_train = X_train.drop(columns=duplicated_cols)

X_test = X_test.drop(columns=duplicated_cols)

X_test.shape

sel = VarianceThreshold(threshold=0.05)

sel.fit(X_train)

sum(sel.get_support())

columns = X_train.columns[sel.get_support()]

X_train = sel.transform(X_train)
X_test = sel.transform(X_test)

X_train = pd.DataFrame(X_train,columns=columns)
X_test = pd.DataFrame(X_test,columns=columns)

print(X_train.shape)
print(X_test.shape)

corr_matrix = X_train.corr()

column_name = corr_matrix.columns

columns_to_drop = []

for i in range(len(column_name)):
  for j in range(i+1,len(column_name)):
    if corr_matrix.loc[column_name[i],column_name[j]]>0.95:
      columns_to_drop.append(column_name[j])

print(len(columns_to_drop))

columns_to_drop = set(columns_to_drop)

len(columns_to_drop)

X_train = X_train.drop(columns=columns_to_drop,axis=1)

X_train.shape

X_test = X_test.drop(columns=columns_to_drop,axis=1)

X_test.shape



from sklearn.feature_selection import f_classif
from sklearn.feature_selection import SelectKBest

model = SelectKBest(f_classif,k=100).fit(X_train,y_train)
X_train.columns[model.get_support()]

columns_for_anova = X_train.columns[model.get_support()]

X_train = model.transform(X_train)
X_test = model.transform(X_test)

X_train = pd.DataFrame(X_train,columns=columns_for_anova)
X_test = pd.DataFrame(X_test,columns=columns_for_anova)

print(X_train.shape)
print(X_test.shape)

log_reg = LogisticRegression(max_iter=1000)
log_reg.fit(X_train,y_train)

y_pred = log_reg.predict(X_test)

accuracy = accuracy_score(y_test,y_pred)
print("Test accuracy",accuracy)
