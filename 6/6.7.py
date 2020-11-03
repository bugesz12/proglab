def atlagolo(szamok):
    
    szum = sum(szamok)
    db = len(szamok)
    atlag = szum / db
    return atlag

def szuro(a,szamok):
    
    szurt = []
    for x in szamok:
        if x < a:
            szurt.append(x)           
    return szurt

def main():
    
    szamok = [24, 31, 22, 43, 10, 84, 38, 44, 84, 56, 67, 51, 56, 84, 31, 65, 69, 83, 39]
    
    a = atlagolo(szamok)
    print(szuro(a,szamok))
 
main()