import random
szoveg = input("Adjon meg valamilyen sort")
szoveghossz = len(szoveg)
for i in range(szoveghossz):
    rand = random.randint(0,1)
    if rand ==1:
        szoveg = szoveg[:i] +szoveg[i].upper()+szoveg[i+1:]
    if rand ==0:
        szoveg = szoveg[:i] + szoveg[i].lower() + szoveg[i + 1:]
print(szoveg)