def beolvas(fnev):
    lista = []
    with open(fnev) as f:
        for sor in f:
            try:
                lista.append(int(sor))
            except ValueError as e:
                pass
    return lista

def stat(eredmenyek):
    db = [0] * 11
    for pont in eredmenyek:
        db[pont] += 1
    return db
    
def stat_kiir(db):
    for pont in range(0, 10 + 1):
         print("{:2} db {:2} pontos".format(db[pont], pont))

    osszes = sum(db)

    atment = sum(db[4:])
    print("Átment: {} fő, {:.4}%".format(atment, atment / osszes * 100))

def main():
    
    fnev = "kzh_pontszam_hibas.txt"
    
    eredmenyek = beolvas(fnev)
    db = stat(eredmenyek)
    stat_kiir(db)
main()
