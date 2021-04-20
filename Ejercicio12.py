h =  int(input('ingrese el numero de horas'))
vh =  int(input('ingrese el valor de una hora pagada en dolares'))

t = vh * h
T = (t * 10) / 100
Td = t - T

if (Td < 300):
    td2 = (Td * 2) / 100
    print("el sueldo de el empleado es " +str(td2))

else:
    print("el sueldo del empleado es " + td)  
