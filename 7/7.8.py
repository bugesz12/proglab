def atvalto(szam,szamrend):
    if szam <= 1:
        return szam
    else:
        return str(atvalto(szam//szamrend,szamrend))+ str(szam%szamrend)





print(atvalto(10,2))
