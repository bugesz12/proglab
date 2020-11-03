szoveg = input("Irj be egy palindrom mondatot ")
szoveg_forditva = ""

szoveg = str.casefold(szoveg)
szoveg = szoveg.replace(" ","")



for i in (szoveg):
    szoveg_forditva = i + szoveg_forditva 



if szoveg == szoveg_forditva:
    print("ez egy palindrom")