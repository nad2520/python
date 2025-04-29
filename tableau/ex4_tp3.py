import numpy as np
tableau1 = np.array([1, 2, 3])
tableau2 = np.array([4, 5, 6])

somme1=np.sum(tableau1)
somme2=np.sum(tableau2)
somme=somme1+somme2
print("la somme des 2 tableaux est : ",somme)

for i in range(3):
    tableau1[i]=tableau1[i]*2
print(tableau1)
print(np.max(tableau2))

 


