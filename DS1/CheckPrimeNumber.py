import math as m

#Check Prime Number
def isPrime(n):
    for i in range(2,n):
        if n%i==0: #if the remainder is zero, n is not prime then print i
            print(n,"is not prime")
            print("i is",i)
            return 

    print(n,"is prime.") #If not zero for all i, n is prime

#Read an integer number
n=int(input("Integer number n in 2 to 32767 : "))
isPrime(n)
