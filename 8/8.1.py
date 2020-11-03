class Datum:
    def __init__(self, ev, honap, nap):
        self.ev = ev
        self.honap = honap
        self.nap = nap
 
class Versenyzo:
    def __init__(self, nev, szuletes, helyezes):
        self.nev = nev
        self.szuletes = szuletes
        self.helyezes = helyezes
 
def datum_str(d):
    
    return("{}-{}-{}".format(d.ev, d.honap, d.nap))
    

    
def versenyzo_str(v):
    
    return("Név: {}, Születési dátum: {}, Helyezés: {}".format(v.nev, datum_str(v.szuletes), v.helyezes))
    
 
def main():
    versenyzok = [
        Versenyzo("Am Erika", Datum(1994, 5, 6), 1),
        Versenyzo("Break Elek", Datum(2001, 9, 30), 3),
        Versenyzo("Dil Emma", Datum(1998, 8, 25), 2),
        Versenyzo("Kasza Blanka", Datum(1989, 6, 10), 5),
        Versenyzo("Reset Elek", Datum(2001, 4, 5), 4),
    ];
 
    print(versenyzok[0].nev)                  # 0-s versenyző neve
    
    print(versenyzok[2].helyezes)             # 2-es versenyző helyezése
    
    print(datum_str(versenyzok[4].szuletes))  # 4-es versenyző születési dátuma (írd meg a datum_str függvényt!)
    
    
    print(versenyzok[1].nev[0])               # 1-es versenyző nevének kezdőbetűje
    
    if versenyzok[1].helyezes <= 3:           # az 1-es versenyző dobogós-e? igen/nem

        print("Dobogós")
    else:
        print("Nem dobogós")
        
    if versenyzok[4].helyezes < versenyzok[3].helyezes:         # az 4-es versenyző gyorsabb-e, mint a 3-as versenyző?
        print("Gyorsabb")
    else:
        print("Nem gyorsabb")
    
    if versenyzok[1].szuletes.ev == versenyzok[2].szuletes.ev:  # az 1-es versenyző ugyanabban az évben született-e, mint a 2-es?
        print("Ugyanabban az évben születtek")
    else:
        print("Nem ugyanabban az évben születtek")
        
    print(versenyzo_str(versenyzok[1]))                         # egészítsd ki a versenyzo_str() függvényt, és írd ki az 1-es versenyző adatait
  
    print("######################")
  
    for i in range(len(versenyzok)):
        print(i,versenyzo_str(versenyzok[i]))
                                                                # végül listázd ki az összes versenyzőt sorszámozva, összes adatukkal.
 
main()