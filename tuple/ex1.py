tuple1=()
tuple2=list(tuple1)
for i in range(3):
    ch=input(str("choix "+str(i)+" :"))
    tuple2.append(ch)
    
for element in tuple2:
    print(element)
    
print(tuple2[1])
    
#on ne peut pas modifier le tuple car il est immuable cela produira donc une erreur



