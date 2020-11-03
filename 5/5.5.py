from random import randint

t = ["k", "p", "o","v"]
gep = t[randint(0,2)]
jatekos = False

jatekos_pont = []
gep_pont = []

while jatekos == False:

    jatekos = input("Kő (k), papír (p), olló (o) vagy vége (v)? ")
    
    if jatekos == gep:
        print("Senki sem kap pontot!")
        
    elif jatekos == "k":
        if gep == "p":
            print("Szerinted: ",jatekos)
            print("Szerintem: ",gep)
            print("Vesztettél!", gep, "<", jatekos)
            gep_pont.append(1)
        else:
            print("Szerinted: ",jatekos)
            print("Szerintem: ",gep)
            print("Nyertél!", jatekos, ">", gep)
            jatekos_pont.append(1)
            
    elif jatekos == "p":
        if gep == "o":
            print("Szerinted: ",jatekos)
            print("Szerintem: ",gep)
            print("Vesztettél!", gep, ">", jatekos)
            gep_pont.append(1)
        else:
            print("Szerinted: ",jatekos)
            print("Szerintem: ",gep)
            print("Nyertél!", jatekos, ">", gep)
            jatekos_pont.append(1)
            
            
    elif jatekos == "o":
        if gep == "k":
            print("Szerinted: ",jatekos)
            print("Szerintem: ",gep)
            print("Vesztettél", gep, "<", jatekos)
            gep_pont.append(1)
        else:
            print("Szerinted: ",jatekos)
            print("Szerintem: ",gep)
            print("Nyertél!", jatekos, ">", gep)
            jatekos_pont.append(1)
            
    elif jatekos == "v":
        print("Szerinted: ",jatekos)
        if sum(jatekos_pont) > sum(gep_pont):
            print("Te nyertél", sum(jatekos_pont),">",sum(gep_pont),"ponttal.")
        elif sum(jatekos_pont) < sum(gep_pont):
            print("Én nyertem", sum(jatekos_pont),"<",sum(gep_pont),"ponttal.")
  
    jatekos = False
    gep = t[randint(0,2)]
