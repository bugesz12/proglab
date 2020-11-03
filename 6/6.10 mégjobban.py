def szamtani(minimum,maximum,d):
    
    if minimum is None and d is None:
        
        maximum = int(maximum)

        eleje = 0
        while maximum > eleje:
            print(eleje)
            eleje += 1
    
    elif d is None:
        minimum = int(minimum)
        maximum = int(maximum)
    
        while maximum > minimum:
            print(minimum)
            minimum += 1
    
    elif d is not None:
        minimum = int(minimum)
        maximum = int(maximum)
        d = int(d)
                
         
        while maximum > minimum:
            print(minimum)
            minimum += d
        
def main():
    
    minimum = input("Adja meg a range függvény első elemét ")
    maximum = input("Adja meg a range függvény utolsó elemét ")
    d = input("Adja meg a range függvény differenciáját ")
    
    if d == "":
        d = None
    
    if minimum == "":
        minimum = None
        
    if maximum == "":
        minimum = None
  
    
    szamtani(minimum,maximum,d)
   
    
main()