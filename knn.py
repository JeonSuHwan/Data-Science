import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Make dataset with page 86
df = pd.DataFrame({'Height(cm)':[158, 158, 158, 160, 160, 163, 163, 160, 163, 165, 165, 165, 168, 168, 168, 170, 170, 170], 
                        'Weight(kg)':[58, 59, 63, 59, 60, 60, 61, 64, 64, 61, 62, 65, 62, 63, 66, 63, 64, 68], 
                        'T_shirt_size':['M', 'M', 'M', 'M', 'M', 'M', 'M', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L']})

#Check data
print(df.head())

#check number of rows and columns in dataset
print(df.shape)

df_x = df[["Height(cm)","Weight(kg)"]]
df_y = df[["T_shirt_size"]]

#Create KNN

def classify(dataset, target, category, k):
    diffMat=target-dataset
    sqDiffMat=diffMat**2
    row_sum=sqDiffMat.sum(axis=1)
    distance=np.sqrt(row_sum)
    sortDist=distance.argsort()

    result={}
    for i in range(k):
        c=category[sortDist[i]]
        result[c]=class_result.get(c,0)+1

    return result

#Set k value
k=5

    
    


