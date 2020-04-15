import numpy as np
import pandas as pd

#Create Numpy array
df=pd.DataFrame({'column_a':[3.,'?',2.,5.],
                'column_b':['*',4.,5.,6.],
                'column_c':['+',3.,2.,'&'],
                'column_d':[5.,'?',7.,'!']})


#Replace any non-numeric value with NaN
df.replace({'?':np.nan,'*':np.nan,'+':np.nan,'&':np.nan,'!':np.nan}, inplace=True)

#fillna with bfill
print(df.fillna(axis=1,method='bfill',limit=1))
