class Tanulo:
    def __init__(self, neptun, nev, pont):
        self.neptun = neptun
        self.nev = nev
        self.pont = pont
    def __str__(self):
        return "{}:{}:{}".format(self.neptun, self.nev, self.pont)
    
    
def beolvas(fnev):
    lista = []
    with open(fnev, "rt", encoding = "UTF-8") as f:
        for sor in f:
            db = sor.split(":")
            lista.append(Tanulo(db[0],db[1],db[2]))
    return lista

def main():
    
    fnev = "zheredmeny.txt" 
    
    lista1 = beolvas(fnev)
    lista2 = list(lista1)
    
    print(lista1 is lista2)         # False, mert két külön listáról van szó

    print(lista1[0] is lista2[0])   # True, ugyanazok az objektumok vannak benne
    
    lista1[0].pontszam = 27         # Reklamált, változott a pontszáma
    
    print(lista2[0].pontszam == 27) # True, mert ugyanaz a dolgozat objektum
    
    lista1nevszerint = sorted(lista1, key=lambda x: x.nev)
    lista2pontszerint = sorted(lista2, key= lambda x: x.pont)
    
    for i in lista1nevszerint:
        print(i)
    print("#############") 
    print("#############")
    for j in lista2pontszerint:
        print(j)
    
main()