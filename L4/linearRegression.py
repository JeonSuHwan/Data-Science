#-*-coding utf8-*-
import pandas as pd
import numpy as np
import io
import warnings
warnings.filterwarnings(action='ignore')

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#import data file
#Distance (meter), Delivery Time (minute)
df=pd.read_csv("linear_regression_data.csv", encoding='utf-8')
print(df.head())

#Split data into training and testing set (Ratio: 4/5, 1/5)
x=df['Distance']
y=df['Delivery Time']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

#train using linear regression
lin=LinearRegression()
lin.fit(x_train.values.reshape(-1,1),y_train)

#caculate accuracy
print('\n<Accuracy>')
print(lin.score(x_test.values.reshape(-1,1), y_test))
