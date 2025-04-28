tuple1=("Alice", 20, "IA")

print("nom :", tuple1[0])
print("age :", tuple1[1])
print("spécialité :", tuple1[2])

tuple2=list(tuple1)
    
tuple2[1]=29

for element in tuple2:
    print(element)
    
tuple3=tuple(tuple2)
print(tuple3)





