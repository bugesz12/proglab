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
    p1 = input()
    return p1

def main():
    p1 = Pont(3, 6)
    p2 = Pont(6, 9)
    
    print("A p1 és p2 pont távolsága:", tav(p1, p2))
    
    if egyenlo(p1, p2):
        print("Egybeesnek")
    else:
        print("Nem esnek egybe")
        
    print(beolvas())   
    
main()