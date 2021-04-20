d =  int(input('ingrese la distancia en km'))
a =  int(input('digite 1 si va a ingresar el tiempo en minutos o 2 en horas'))

if (a == 2):
    t =  int(input('ingrese las horas'))
    v = d / t
    print("la velocidad a la que tienes que ir es " + str(v) +"km/h")
if (a == 1):
    t = int(input('ingrese los minutos'))
    T = t * (1 / 60)
    v = d / T 
    print("la velocidad a la que tienes que ir es " + str(v) +"km/h")
