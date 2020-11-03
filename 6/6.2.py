import math

def kob(x):
    return x**3

print(kob(3))

def abszolut(x):
    if x < 0:
        return x*-1
    else:
        return x

print(abszolut(-5))

def lepkedo():
    a = -1
    while a <= 1:
        print("{:.4f} {:.4f} |{:.4f}| {:.4f}".format(a,a**3,abs(a),math.sin(a)))
        a += 0.1

lepkedo()
        
    