def saisie():
    n=int(input("n="))
    while(n<=0):
        n=int(input("n="))
    return n
def construction_dict(n):
    d={}
    for i in range(n):
        x=int(input("saisir le degré : "))
        a=int(input("saisir le coeff : "))
        d[x]=a
    return d
def polynome(d):
    ch=""
    for i in d:
        ch=ch+str(d[i])+"*x**"+str(i)+"+"
        
    return ch[:len(ch)-1]
def evaluer(z,d):
    s=0;
    for i in d:
        s=s+d[i]*z**i
    return s
n=saisie()
d=construction_dict(n)
print(d)
ch=polynome(d)
print(ch)
s=evaluer(2,d)
print(s)