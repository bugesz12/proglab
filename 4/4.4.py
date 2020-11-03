lista = [1,2,3,4,5,6,7,8,9,10]
        
    
if (all(lista[i] <= lista[i + 1] for i in range(len(lista)-1))):
    print("Növekvő")
    
else:
    print("Nem növekvő")