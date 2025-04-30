import numpy as np
def saisie(n):
    t=[]
    for i in range(n):
        element=int(input())
        t.append(element) #t.append(int(input()))
    return np.array(t)

def parcours(t):
    k=[]
    for element in t:
        k.append(element*2)
    return np.array(k)
        
t=saisie(4)
k=parcours(t)
print(k)
