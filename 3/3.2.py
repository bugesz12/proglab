szoveg = input("Irj be egy palindromot ")
szoveg_masolat = ""



for i in (szoveg):
    szoveg_masolat = i + szoveg_masolat 


if szoveg == szoveg_masolat:
    print("ez egy palindrom")
