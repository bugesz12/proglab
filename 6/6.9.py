def meghatarozo(betu):
    if betu == 'a' or betu == 'á' or betu == 'e' or betu == 'é' or betu == 'i' or betu == 'o' or betu == 'ó' or betu == 'ö' or betu == 'ő' or betu == 'u' or betu == 'ú' or betu == 'ü' or betu == 'ű':
        return True

def madarnyelvesito(szo):
    for c in szo:
        if c == 'a' or c == 'á' or c == 'e' or c == 'é' or c == 'i' or c == 'o' or c == 'ó' or c == 'ö' or c == 'ő' or c == 'u' or c == 'ú' or c == 'ü' or c == 'ű':
            print(c, 'v', c, sep="", end="")
        else:
            print(c, end="")
  
def main():
    
    betu = input("Kérek egy betűt ")
    szo = input("Kérek egy szót ")
    
    if meghatarozo(betu):
        print("Ez egy magánhangzó")
    else:
        print("Nem magánhangzó")
    
    
    madarnyelvesito(szo)

main()