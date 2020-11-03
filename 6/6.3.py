def szokoev_e(sz):
    if sz % 400 ==0:
        return True
    elif sz % 100 == 0:
        return False
    elif sz % 4 == 0:
        return True
    return False

  
def main():
    
    sz = int(input("Adjon meg egy számot:"))
    print(sz)
    if szokoev_e(sz):
        print("Szökőév")
    else:
        print("Nem szökőév")
    
    
    
main()