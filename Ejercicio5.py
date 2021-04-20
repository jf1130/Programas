pb =  int(input('Ingrese su calificacion del primer bimestre'))
sb =  int(input('Ingrese su calificacion del segundo bimestre'))

t = pb + sb
P = t / 2

if (P >= 3.5):
    print("tu nota es " + str(P) + " felicidades pasaste")              

if (P < 3.5):           
    print("lo siento no pasaste")
