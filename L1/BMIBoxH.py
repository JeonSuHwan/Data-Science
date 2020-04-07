#NumPy Exercise
import numpy as np
wt=np.random.uniform(40,90,size=100)
ht=np.random.randint(140,200,size=100)
BMI=wt/(ht*0.01)**2

#MatPlotLib Exercise
import matplotlib.pyplot as plt

uw=wt[BMI<18.5]
h=wt[np.logical_and(BMI>=18.5,BMI<25.0)]
ow=wt[np.logical_and(BMI>=25.0,BMI<30.0)]
o=wt[BMI>=30.0]

plotData=[uw,h,ow,o]
plt.boxplot(plotData)
plt.show()







