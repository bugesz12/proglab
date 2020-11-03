import math

a =int(input("Adja meg az a-t:"))
b =int(input("Adja meg az b-t:"))
c =int(input("Adja meg az c-t:"))


d =  b**2-(4*a*c)

if d < 1:
    print("Hiba!")

if d > 1:
    x1 = (-b + math.sqrt(d))/(2*a)

    x2 = (-b - math.sqrt(d))/(2*a)


    print("x1:",x1,"x2:", x2)     
    

