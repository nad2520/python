def saisi():
    n=int(input("saisir le nombre de monomes: "))
    while n<0:
        n=int(input("saisir le nombre de monomes: "))
    return n

def construction_dict(n):
    dictt={}
    for i in range(n):
        deg=str(input("saisir le degré du monome: "))
        coef=str(input("saisir le coefficient du monome: "))
        dictt[deg]=coef
    return dictt

def polynome(d):
    ch=""
    for element in d:
        ch=ch+str(d[element])+"*x**"+str(element)+"+"
    return ch[:len(ch)-1]

def evaluation(x,d):
    evall=0
    for element in d:
        evall=evall+int(d[element])*x**(int(element))
    return evall

n=saisi()
dictt=construction_dict(n)
p=polynome(dictt)
eva=evaluation(2,dictt)
print(dictt)
print(p)
print(eva)

