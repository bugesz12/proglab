import math

x1 = int(input("Add meg az a első koordinátáját:"))
y1 = int(input("Add meg az a második koordinátáját:"))
x2 = int(input("Add meg az b első koordinátáját:"))
y2 = int(input("Add meg az b második koordinátáját:"))

h_nyers = (x2-x1)**2 + (y2-y1)**2
h = math.sqrt(h_nyers)
print("Hossz:",h)