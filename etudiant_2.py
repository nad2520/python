def saisi ():
    n=int(input("n= "))
    while n<0:
        n=int(input("n= "))
    return n

def admis():
    global n
    l=[]
    t=()
    for i in range (n):
        ch=str(input("saisir votre nom: "))
        note=float(input("saisir votre note: "))
        t=(ch,note)
        l.append(t)
    print(l)
    t1=[]
    best=l[0][1]
    l1=[]
    tt=()
    moy=0
    for element in l:
        if element[1]>10:
            t1.append(element[0])
        
        if element[1]>best:
            nom=""
            best=element[1]
            nom=element[0]
            
        moy=moy+element[1]
        
    t2=tuple(t1)
    l1.append(t2)
    tt=(nom,best)
    moy=moy/n
    l1.append(tt)
    l1.append(moy)
    return l1

n=saisi()
l=admis()
print(l)

