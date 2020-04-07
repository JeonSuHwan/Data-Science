#NumPy Exercise
import numpy as np
wt=np.random.uniform(40,90,size=100)
ht=np.random.randint(140,200,size=100)
BMI=wt/(ht*0.01)**2

import matplotlib.pyplot as plt

#height
uw=ht[BMI<18.5]
h=ht[np.logical_and(BMI>=18.5,BMI<25.0)]
ow=ht[np.logical_and(BMI>=25.0,BMI<30.0)]
o=ht[BMI>=30.0]

#weight
UW=wt[BMI<18.5]
H=wt[np.logical_and(BMI>=18.5,BMI<25.0)]
OW=wt[np.logical_and(BMI>=25.0,BMI<30.0)]
O=wt[BMI>=30.0]

plt.scatter(uw,UW,color="red")
plt.scatter(h,H,color="blue")
plt.scatter(ow,OW,color="green")
plt.scatter(o,O,color="yellow")
plt.xlabel("height (cm)")
plt.ylabel("weight (kg)")
plt.title("Scatter plot")
plt.show()
