n = 1
while n <= 10:
    print(n, end=" ")     # nem kezd új sort
    n += 1
print(".")                #a vegen mar az n 11,de megnezi ujra a program es false-ra allitja



szorzat = 1
n = 8
while n > 1:
    szorzat *= n
    n -= 1
print(szorzat)               #20160 lesz amikor az n változó 3


a = 11220
b = 2002
while b > 0:
    temp = b
    b = a % b
    a = temp
 
print("lnko =", a)           #44 lesz a b amikor az a 374re áll