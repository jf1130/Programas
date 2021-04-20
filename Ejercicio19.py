entrar = int(input("para entrar al asensor oprima 1"))


if(entrar == 1):
    for i in range(26):
        boton = int(input("1 para subir 2 para bajar"))
        if(boton == 1):
            i = i + 1
            print(i)
        if(boton == 2):    
            for j in range(i, 1, -1):
                boton = int(input("2 para bajar 1 para subir"))
                if(boton == 2):
                    j = j - 1
                    print(j) 
                if(boton == 1):
                    i = i + 1
                    print(i)     
