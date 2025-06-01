L=["Paracetamol", "Ciprofloxacine", "Loratadine", "Metformine" ]
LI = [["LOT12345", 1.50, "01/24", "01/26", 9, 0, True], ["LOT12349", 5.00, "05/23", "05/25", 7, 2, True], ["LOT12350", 1.75, "06/25", "06/26", 18, 0, True], ["LOT12351", 2.50, "02/25", "06/27", 0, 3, False] ]

def concat(l,l1):
    d={}
    for i in range(len(l)):
        d[l[i]]=l1[i]
    return d

def supp(d,nom):
    if nom not in d.keys():
        return False
    del(d[nom])
    return d

def augmentation(d,t,p):
    for element in d.values():
        if t in element :
            element[1]=element[1]+p
    return d

def rupture(d):
    l=[]
    for element in d:
        if d[element][5]!=0 and d[element][4]<10:
            l.append(element)
    return tuple(l)
            
def commande(d,c):
    for element in d:
        for el in c:
            if element== el[0]:
                d[element][4]=el[1]
    return d

def affichage(d,t):
    l=[]
    for element in d:
        if d[element][5]==t and d[element][6]==True:
            l.append(element)
            print(element)
    return l

d=concat(L,LI)
print(d)
d=supp(d,"Ciprofloxacine")
print(d)
print("~~~~~~~~~~~~~~~~~~~~~")
d=augmentation(d,0,2.5)
print(d)
t=rupture(d)
print(t)
c=(("Paracetamol", 30), ("Metformine", 10))
d=commande(d,c)
print(d)
l=affichage(d,0)
print(l)
