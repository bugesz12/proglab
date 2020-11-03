hatar1 =int(input("Adja meg a sorozat alsó határát:"))
hatar2 =int(input("Adja meg a sorozat felső határát:"))


if hatar1 > hatar2:
    print("Hiba!")
    

if hatar1 < hatar2:   

    d = int(input("Adja meg a sorozat differenciáját:"))

    n = hatar1

    while n <= hatar2:
        print(n,end=" ")
        n += d