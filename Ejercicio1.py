nA =  float(input('Nota del primer parcial'))
nB =  float(input('Nota del segundo parcial'))
nC =  float(input('Nota del tercer parcial'))
IN =  float(input('Poner el numero de insistencias'))

A = nA * 0.35
B = nB * 0.35
C = nC * 0.30

R = A + B + C

if (R >= 3.0):
    if (IN < 12):
        print("felicidades su nota final fue de " + str(R))
if (R < 3.0):
    print("usted no paso")

if (IN > 12):   
    print("usted perdio por inasistencias")
