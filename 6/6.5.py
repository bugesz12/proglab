def a_betu(lista):
    for szo in lista:
        if szo != "":
            if szo[0] == "a":
                return True 
    return False
    

def main():
    lista = ["dinnye", "papaja", "", "zeller"]
    if a_betu(lista):
        print("van benne a betű")
    else:
        print("nincs benne")
    
main()
