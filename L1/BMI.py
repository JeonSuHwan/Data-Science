#NumPy Exercise
import numpy as np

#weight array
wt=np.random.uniform(40,90,size=100)
#height array
ht=np.random.randint(140,200,size=100)

#BMI array (weight in kilograms and height in meters)
BMI=wt/(ht*0.01)**2

print(BMI)
