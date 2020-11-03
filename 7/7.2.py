def fakt(n):
    if n == 0:
        return 1
    else:
        return n * fakt(n-1)



def main():
    n = 0
    while n <= 10:
        print("{}! = {}".format(n,fakt(n)))
        n = n+ 1
    
    
    
    
main()