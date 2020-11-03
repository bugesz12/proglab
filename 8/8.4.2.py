import math
class Pont:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
    
    
def tav(p1, p2):
    return math.sqrt((p1.x-p2.x)**2+(p1.y-p2.y)**2)
   
def egyenlo(p1, p2):
    if p1.x == p2.x and p1.y == p2.y:
        return True
    return False

def beolvas():
    return Pont(input("Adja meg az x-et"), input("Adja meg az y-ont"))

def main():
   
  kezdo = beolvas()
  aktualis = kezdo
  tavolsag = 0
  
  while True:
      
      ujadat = beolvas()
      if egyenlo(ujadat, kezdo):
          tavolsag += tav(aktualis,kezdo)
          break
      tavolsag += tav(aktualis,ujadat)
      aktualis = ujadat

  print(tavolsag) 
        
   
    
main()
