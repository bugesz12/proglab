def hatvany(a,k):
    if k == 0:
        return 1
    elif k % 2 == 0:
        return hatvany(a**2,k/2)
    return a * hatvany(a,k-1)

print(hatvany(2,2))
        