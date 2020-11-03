def hany_napos(honap):
    if honap == 1 or honap == 3 or honap == 5 or honap == 7 or honap == 8 or honap == 10 or honap == 12:
        print("31 napos a hónap")
    elif honap == 2:
        print("28/29 napos az évtől függően")
    else:
        print("30 napos")
    

def main():
    honap = int(input("Adja meg egy hónap számát: "))
    hany_napos(honap)
    
main()
    
    
    