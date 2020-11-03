class Ido:
    def __init__(self, ora, perc):
        atvalto = ora * 60 + perc
        self.ora = atvalto // 60 
        self.perc = atvalto % 60
        
def ido_kiir(i):
    return "{}:{}".format(i.ora, i.perc)

def ido_hozzaad(i, p):
    return Ido(i.ora, i.perc + p)

def ido_eltelt(i1, i2):
    return Ido(i1.ora - i2.ora, i1.perc - i2.perc)

def ido_kivon(i, p):
    return Ido(i.ora, i.perc - p)


def main():
    
    i = Ido(12, 15)
    p = 15
    i1 = Ido(17, 15)
    i2 = Ido(15, 30)
    
    print("A pontos idő:", ido_kiir(i))
    print("A pontos idő +", p, "perc:", ido_kiir(ido_hozzaad(i, p)))
    print("Az eltelt idő a két időpont között:", ido_kiir(ido_eltelt(i1, i2)))
    print("A pontos idő -", p, "perc:", ido_kiir(ido_kivon(i, p)))
    
    
main()