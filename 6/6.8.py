def szorzo(a):
    return 2 * a

def elojelezo(a):
    return -1 * a

def hozzaado(a):
    return a + 1

def visszaallito(a):
    a = 1
    return a 

def main():
    
    a = 1
        
    program = True
    while program:
        
        print("0. Alapertek visszaallitasa (a = 1)",
      "1. Hozzaad 1-et",
      "2. Megforditja az elojelet",
      "3. Szorozza 2-vel",
      "9. Kilepes",
      sep="\n")
        
        i = int(input())
            
        if i == 0:
            a = visszaallito(a)
            print("Új érték: ", a)
            
        elif i == 1:
            a = hozzaado(a)
            print("Új érték: ", a)
            
        elif i == 2:
            a = elojelezo(a)
            print("Új érték: ", a)
            
        elif i == 3:
            a = szorzo(a)
            print("Új érték: ", a)
        
        elif i == 9:
            program = False
            
main()
