szoveg = "TO BE OR NOT TO BE: THAT IS THE QUESTION."
betuk = []
for i in range(ord("A"),ord("Z")):
    betuk.append(chr(i))
for i in szoveg:
    if i not in betuk:
        szoveg = szoveg.replace(i,"")
        
betuk_ossz = [0]*26
for i in szoveg:
    betuk_ossz[int(ord(i)-65)] +=1


for i in range(len(betuk_ossz)-1):
    if betuk_ossz[i] > 0:
        print("{0}:\t{1}db,\t{2:.3}%".format(chr(i+65),betuk_ossz[i],(betuk_ossz[i]/sum(betuk_ossz)*100)))
