import numpy as np
def saisie(n,m):
    M=np.ndarray((n,m),dtype=int)
    for i in range (n):
        for j in range (m):
            M[i,j]=int(input())
    return M

def parcours(t,n,m):
    for i in range(n):
        for j in range(m):
            t[i][j]=t[i][j]*2
    return t
        
m=saisie(2,2)
m=parcours(m,2,2)
print(m)
