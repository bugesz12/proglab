def fakt(n):
    if n == 1:
        return 1
    else:
        return n * fakt(n-1)
    
def main():
    print(fakt(6))

main()
        