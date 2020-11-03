'''
eredeti = [1,2,3,4,5,6,7,8,9,10]
forditott = []

for i in range(len(eredeti)):
    forditott.append(eredeti.pop(-1))

print(forditott)

eredeti = [1,2,3,4,5]
forditott = []

for i in range (len(eredeti)-1,-1,-1):
    forditott.append(eredeti[i])
    
print(forditott)
'''
eredeti = [1,2,3,4,5]
eredeti.reverse()
print(eredeti)