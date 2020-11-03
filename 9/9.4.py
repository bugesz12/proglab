def megallok(metro2):
    
    lista = []
    
    with open(metro2, "rt", encoding="utf-8") as f:
        for sor in f:
            megvagott = sor.strip("\n")
            lista.append(megvagott)
    return lista


def atszallo(metro1, metro2):
    
    kozos = []
    lista1 = megallok(metro1)
    lista2 = megallok(metro2)
    for i in lista1:
        for j in lista2:
            if i == j:
                kozos.append(j)
    if len(kozos) > 0:
        return kozos
    else:
        return None
    
def main():

    metro1 = "m1.txt"
    metro2 = "m2.txt"
    metro3 = "m3.txt"
    metro4 = "m4.txt"
    
    print(megallok(metro2))

    print(atszallo(metro1, metro2))
    
main()