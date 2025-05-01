import numpy as np
temperatures = np.array([22, 24, 19, 30, 28, 25, 20, 18, 23, 27, 31, 26, 29, 24, 22, 20, 19, 25,
28, 30, 32, 27, 26, 24, 23, 21, 20, 18, 17, 19])

def supp(temperatures):
    sup=[]
    for element in temperatures:
        if element>25:
            sup.append(element)
    return np.array(sup)

def nb_j(temperatures):
    nb=0
    for element in temperatures:
        if element<20:
            nb+=1
    return nb

def remplacer(t):
    n=np.size(t)
    t1=[]
    for i in range(n):
        if t[i]<20:
            t1.append(np.mean(t))
        else:
            t1.append(t[i])
    return np.array(t1)

t=supp(temperatures)
print(t)
nb=nb_j(temperatures)
print(nb)
tt=remplacer(temperatures)
print(tt)
