#Set tuple K about keys
K=("White","Red","Black")

#Set tuple V about values
V=(1000,1001,0)

def makeDict(k,v):
    d=zip(k,v)
    return d

print("K :",K)
print("V :",V)

# Print dictionary
D=makeDict(K,V)
print("D :", end=" ")
for a,b in D:
    print("{} : {}".format(a,b),end=" ")
