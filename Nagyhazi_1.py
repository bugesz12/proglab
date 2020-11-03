class Kviz:
    def __init__(self, nehezseg, kerdes, a, b, c, d, valasz, kategoria):
        self.nehezseg = nehezseg
        self.kerdes = kerdes
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.valasz = valasz
        self.kategoria = kategoria
    def __str__(self):
        return "\n{}.Nehézség Kategória: {}Kérdés: {} \nVálaszok: \nA: {} \nB: {} \nC: {} \nD: {} ".format(self.nehezseg, self.kategoria, self.kerdes, self.a, self.b, self.c, self.d, self.valasz)
                 

def beolvas(fnev):
    lista = []
    with open(fnev, "rt", encoding = "UTF-8") as f:
        for sor in f:
            db = sor.split(";")
            lista.append(Kviz(db[0], db[1], db[2], db[3], db[4], db[5], db[6], db[7]))
    return lista


    

def main():
    
    fnev = "loim_teszt.csv"
    lista1 = beolvas(fnev)
    
    i = 1
    ft = 0
    for kerdesek in lista1:
        print(lista1[i])
        jatekos_v = input("Adja meg válaszát: ")
        jatekos_v = jatekos_v.upper()
        print()
        if jatekos_v == lista1[i].valasz:
            print("Helyes!")
            i += 1
            ft += 10000
            print("Jelenlegi összeg:{}".format(ft))
        else:
            print("Sajnos nem jó válasz, a játék véget ért!")
            break
    
main()