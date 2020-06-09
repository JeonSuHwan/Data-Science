#-*-coding: utf8-*-
import pandas as pd
import numpy as np
import io
import warnings
warnings.filterwarnings(action='ignore')

from pandas import Series, DataFrame
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

#import the data file
#data: interview pass or not
#interview column is label
df=pd.read_csv('decision_tree_data.csv', encoding='utf-8')
print(df.head())

dd = pd.get_dummies(df)
#Split dataset into train and test data (Ratio-> 9:1)
x = dd.drop('interview',axis=1)
y = dd['interview']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.1)

#Using decision tree
clf=DecisionTreeClassifier()
clf.fit(x_train,y_train)

print("\nPredict")
pred=clf.predict(x_test)
print(pred)
print("Y test")
print(y_test.values)

print("\nAccuracy")
print(clf.score(x_test,y_test))



