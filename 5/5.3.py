
import random
lista = [1,2,4,7,98,423,234,54645,645645,234432432,12,23]

# for i in range(len(lista)-1,0,-1):
#     j = random.randrange(0,i)
#     temp = lista[i]
#     lista[i] = lista[j]
#     lista[j] = temp
#     print(lista)
# print(lista)
# print()
# print()

ujlista =[]
for i in range(0, len(lista)):
    j = random.randrange(0, len(lista))
    ujlista.append(lista.pop(j))
    print(ujlista,lista)