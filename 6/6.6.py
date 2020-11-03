def cserelo(szo,pozicio,betu):
    return szo[:pozicio] + betu + szo[pozicio+1:]




def main():
    szo = "papa"
    pozicio = 1
    betu = "i"
    
    if len(szo) < pozicio:
        raise ValueError("Érvénytelen pozíció:",pozicio)
            
   
    print(cserelo(szo,pozicio,betu))

    
    
main()