import turtle as t

def beolvas(fnev):
    
    lista = []
    with open(fnev) as f:
        for sor in f:
            lista.append(int(sor))
    return lista


def stat(pontszamok):
    
    db = [0] * 11
    for pont in pontszamok:
        db[pont] += 1
    return db


def oszlop(mag):
    t.color("red")
    t.begin_fill()
    t.forward(10)
    t.left(90)
    t.forward(mag)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(mag)
    t.left(90)
    t.end_fill()

def rajz(db):
    t.hideturtle()
    t.down
    for hany in db:
        oszlop(hany*7)
        t.forward(20)
        
        
def main():
    
    pontszamok = beolvas('kzh_pontszam.txt')
    
    rajz(stat(pontszamok))
    
    t.mainloop()
    
main()