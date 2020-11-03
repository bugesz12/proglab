def betoltes(szoveg):
    lista = []
    with open(szoveg, "rt") as f:
        for sor in f:
            megvagott = sor.strip("\n")
            lista.append(megvagott)
    return lista

def mentes(k_lista,fnev):
       
    with open(fnev, "wt") as f:
        for szo in k_lista:
            f.write(szo + "\n")
            
def main():
    
    szoveg = "szavak_50.txt"
    
    print(betoltes(szoveg))
    
    betoltes(szoveg).sort()
    
    lista = betoltes(szoveg)
    
    k_lista = []
    for szo in lista:
        if szo[0] == "k":
            k_lista.append(szo)
    
    fnev = "szavak_kbetus.txt"
    
        
    mentes(k_lista,fnev)
    
main()