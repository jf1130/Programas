boton = int(input("1 para subir 2 para bajar"))


if(boton == 1):
    for i in range(26):
        subir = int(input("1 para subir"))
        if(subir == 1):
            i = i + 1
            print(i)

if(boton == 2):    
    for j in range(25, 1, -1):
        subir = int(input("2 para bajar"))
        if(boton == 2):
            j = j - 1
            print(j)          
