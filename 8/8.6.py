class Fagyi:
    def __init__(self, iz, db):
        self.iz = iz
        self.db = db
    
def kereso(lista, mit):
    for i in range(len(lista)):
        if lista[i].iz == mit:
            return i
    return -1
        

def main():
    fagyik = [
        Fagyi("pisztácia", 0),
        Fagyi("vanília", 6),
        Fagyi("tutti-frutti",9),
        Fagyi("karamell",1),
        Fagyi("rumos dió", 5),
        Fagyi("kávé", 7),
        ]
    
    iz = input()
    while iz != "":
        talalat = kereso(fagyik, iz)
        if talalat != -1:
            if fagyik[talalat].db > 0:
                print("Kösz öcsi! ")
                fagyik[talalat].db -= 1
                iz = input()
            else:
                print(iz, "kifogyott")
                break
        else:
            print(iz, "Nem is volt")
            break
    
    
main()