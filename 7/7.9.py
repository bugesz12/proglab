def tagolo(szam):
    if szam//1000 <= 0:
        return szam
    else:
        return "{} {:0^3}".format(tagolo(szam//1000),str(szam%1000))


print(tagolo(21000))