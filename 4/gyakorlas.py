szamok = [2.5, -69, 5.4, -8, -7.7, 6, 2.9, -10, -3, 9.8]
a = len(szamok)
print("Összesen {} db szám van.".format(a))

min_hely = szamok[0]
min_ertek = 0
negativ = []

for i in range(len(szamok)):
    print("[{}] = {}".format(i,szamok[i]))
    if i > 0:
        if szamok[i] > min_ertek:
            min_hely = i
            min_ertek = szamok[i]
        
        if szamok[i] < 0:
            negativ.append(i)
                
print("Ebből {} szám negatív.".format(len(negativ)))
print("Indexeik:",*negativ)


print()


print("Ebből {} szám negatív.".format(len(negativ)))
for i in range(len(negativ)):
    print("{}. [{}] = {}".format(str(i+1),negativ[i],szamok[negativ[i]]))
    
               
        
    
    