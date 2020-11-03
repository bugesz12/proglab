def szamtani(minimum,maximum,d):
    
    if minimum is None and d is None:
        
        eleje = 0
        while maximum > eleje:
            print(eleje)
            eleje += 1
    
    elif d is None:
    
        while maximum > minimum:
            print(minimum)
            minimum += 1
    
    elif d is not None:
                
         
         while maximum > minimum:
            print(minimum)
            minimum += d
        
def main():
    
    minimum = 1
    maximum = 5
    d = None
    
  
    szamtani(minimum,maximum,d)
   
    
main()
