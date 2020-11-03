import math

print("Tartály festése")
print()

m = int(input("Milyen magas?"))
a = float(input("Mekkora az átmérője?"))
r = a/2


felszin = 2*r**2*math.pi + 2*r*math.pi*m
festek = felszin/2

print(festek,"doboz festék kell")