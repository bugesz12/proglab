import turtle
turtle.speed(10)

def fraktal(h,n):
    if n ==0:
        turtle.forward(h)
    else:
        fraktal(h/3,n-1)
        turtle.left(60)
        fraktal(h/3,n-1)
        turtle.right(120)
        fraktal(h/3,n-1)
        turtle.left(60)
        fraktal(h/3,n-1)
        
def main():
    h = int(input("Hossz? "))
    n = int(input("Bonyolultság? "))
    fraktal(h,n)

main()

