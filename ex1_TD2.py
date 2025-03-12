def saisi_l():
    l=[]#liste
    for i in range(n):
        nom=str(input("nom: "))
        moy=float(input("moyenne: "))
        etud=(nom,moy)#tuple
        l.append(etud)
    return l
def admis(l,n):
    l1=[]
    a=l[0][1]
    s=0;
    for etud in l:
        nom,moy=etud
        adm=()
        if moy>=10:
            adm=(nom)
            l1.append(adm)
        if moy>a:
            a=moy
            b=nom
        s=s+moy
    
    best=(b,a)
    l1.append(best)
    moye=s/n
    l1.append(moye)
    return l1

n=int(input("n= "))    
l=saisi_l()
print (l)
l=admis(l,n)
print(l)