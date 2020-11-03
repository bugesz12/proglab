def vizsgalo(vmi):
    try:
        vmi = int(vmi)
        if type(vmi) == int:
            return True
    except:
        return False

    
def main():

    print(vizsgalo("123"))
    
main()