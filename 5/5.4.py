print("Adja meg a távolságokat: ")
 
lista = []
sor = input()
while sor != "":
    szam = float(sor)
    lista.append(szam)
    sor = input()

lista2 = []
summ = 0

for i in lista:
    summ = summ + i
    print("{0:g} km,".format(i),end = " ")
    lista2.append(i)
    hehe = sum(lista2) + i
    if i == lista[-1]:
        print("vége.")
        break
    if hehe >= 150:
        print("szünet.",end = " ")
        lista2.clear()
        print()
        
    
        

       
        
        