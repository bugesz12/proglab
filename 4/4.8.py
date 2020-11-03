v = input("Sebesség? ")
v_lista = []
while v != "":
    v_lista.append(v)
    v = input("Sebesség? ")
    
v_lista2 = [0]*20
for i in v_lista:
    tized = int(i)/10
    egesz,nemegesz = divmod(tized,1)
    v_lista2[int(egesz)] = v_lista2[int(egesz)]+1

print("km/h\tautók száma")
kis = 0
nagy = 9
for i in range(20):
    print("{0}-{1}\t\t{2}".format(kis,nagy,v_lista2[i]))
    kis += 10
    nagy +=10
    
    
    
    