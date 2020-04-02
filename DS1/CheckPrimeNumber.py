import math as m

#Check Prime Number
def isPrime(n):
    for i in range(2,int(m.sqrt(n))):
        if n/i==0:
            print(n,"is not prime")
            print("i is",i)
            return
        else:
            print(i,',',n,"is prime")

#Read an integer number
n=int(input("Integer number n in 2 to 32767 : "))
isPrime(n)
