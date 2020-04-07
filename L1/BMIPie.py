#NumPy Exercise
import numpy as np
wt=np.random.uniform(40,90,size=100)
ht=np.random.randint(140,200,size=100)
BMI=wt/(ht*0.01)**2

import matplotlib.pyplot as plt

uw=len(BMI[BMI<18.5])
h=len(BMI[np.logical_and(BMI>=18.5,BMI<25.0)])
ow=len(BMI[np.logical_and(BMI>=25.0,BMI<30.0)])
o=len(BMI[BMI>=30.0])

level=["Underweight","Healthy","Overweight","Obese"]
bmi=[uw,h,ow,o]
plt.pie(bmi,labels=level,autopct="%1.2f%%")
plt.title("Pie Chart")
plt.show()
