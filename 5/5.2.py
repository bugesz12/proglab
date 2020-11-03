
szam = int(input("Adjon meg egy számot: "))

while szam != 1:
    oszto = 2
    while oszto <= szam:
        if szam % oszto ==0:
            print("{:>2}|{}".format(szam,oszto))
            szam = int(szam/oszto)
            oszto = 2
        oszto += 1
print("{:>2}|".format("1"))
    