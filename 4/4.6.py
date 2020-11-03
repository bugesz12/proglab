print("Adja meg a távolságokat: ")

lista = []

sor = input()
while sor != "":
    szam = float(sor)
    lista.append(szam)
    sor = input()

minert = lista[0]
minhely = 0

print("A lista: ", end="")
for i in range(len(lista)):
     print("[{0}]={1} ".format(i,lista[i]),end="")
     if i > 0:
        if lista[i] < minert:
            minhely = i
            minert = lista[i]
        
print()
print("A legkisebb elem:[{0}]={1}".format(minhely,minert))

for i in range(len(lista)):
    if i == minhely:
        print("[{0}]={1}[MIN] ".format(i, lista[i]), end="")
    else:
        print("[{0}]={1} ".format(i, lista[i]), end="")