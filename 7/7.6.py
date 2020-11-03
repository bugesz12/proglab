def szamtani(a,d,i):
    if i == 0:
        return a
    else:
        return szamtani(a+d,d,i-1)
    

print(szamtani(1,1,10))


def main():
    for i in range(10):
        print(szamtani(1,1,i+1))
    
    
main()
