class Vendeg:
    def __init__(self, nev, szobaszam):
        self.nev = nev
        self.szobaszam = szobaszam
        
def melyik_emelet(v):
    return "{} a(z) {}. emeleten van".format(v.nev, v.szobaszam//100)

def foglalas(vendegek, vn):
    for i in range(len(vendegek)):
        if vendegek[i].nev == vn:
            return "{} nevű foglaláshoz a(z) {}. számú szoba tartozik.".format(vendegek[i].nev, vendegek[i].szobaszam)
    return None

def emeletek(vendegek):
    emeletek = [0] * 8
    for i in vendegek:
        emeletek[(i.szobaszam // 100 )] += 1
    return emeletek
    
def legzsufoltabb_emelet(vendegek):
    return "A(z) {}. emelet a legzsúfoltabb".format(emeletek(vendegek).index(max(emeletek(vendegek))))

def main():
    
    v = (Vendeg("Hot Elek", 712))
    
    print(melyik_emelet(v))
    
    vn = "Para Zita"
    
    vendegek = [Vendeg("Nyomo Réka", 669), Vendeg("Para Zita", 420), Vendeg("Pop Simon", 421)]
    
    print( foglalas(vendegek, vn) )
    
    print( emeletek(vendegek) )
    
    print( legzsufoltabb_emelet(vendegek) )
    
main()
        