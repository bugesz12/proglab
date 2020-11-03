def padlozo(n):
    if n >= 2:
        return padlozo(n-1) + padlozo(n-2)
    return 1

print(padlozo(3))