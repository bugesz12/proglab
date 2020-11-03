#sakktábla

m = int(input("Mekkora legyen egy mező?"))

print()

sor1 = (('X' * m + '.' * m) * 4 + '\n' ) * m
sor2 = (('.' * m + 'X' * m) * 4 + '\n') * m
print((sor1 + sor2) * 4)