#-*-coding utf8-*-
import pandas as pd
import numpy as np
import io
import warnings
warnings.filterwarnings(action='ignore')

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV

#K-Nearest Neighbors Algorithm
from pandas import Series, DataFrame

df=pd.read_csv('knn_data.csv', encoding='utf-8')
df['longitude']=pd.to_numeric(df['longitude'])
df['latitude']=pd.to_numeric(df['latitude'])
print(df.head())

x=df.drop(columns=['lang'])
y=df['lang'].values

#Use k-fold cross-validation
knn=KNeighborsClassifier(n_neighbors=3)
scores = cross_val_score(knn,x,y,cv=5)

print()
print(scores)
print('scores mean: {}'.format(np.mean(scores)))

#Hypertuning optimization
knn2 = KNeighborsClassifier()
param_grid={'n_neighbors':np.arange(1,25)}
knn_gscv=GridSearchCV(knn2,param_grid,cv=5)
knn_gscv.fit(x,y)
print()
print(knn_gscv.best_params_)
print(knn_gscv.best_score_)
