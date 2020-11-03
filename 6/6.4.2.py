def szokoev_e(ev):
        if ev % 400 ==0:
            return True
        elif ev % 100 == 0:
            return False
        elif ev % 4 == 0:
            return True
        return False


def napszamolo(ev,honap,nap):
    eredeti = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31 ,30 ,31]
    szoko = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31 ,30 ,31]
    
    if szokoev_e(ev) == True:
        return sum(szoko[0:honap-1],nap)
    else:
        return sum(eredeti[0:honap-1],nap)

def main():
    datum = input("Adjon meg egy dátumot, szóközzel elválasztva! ")
    datum_lista = list(datum.split(" "))
    ev = int(datum_lista[0])
    honap = int(datum_lista[1])
    nap = int(datum_lista[2])
    
    print(napszamolo(ev,honap,nap))


main()
    