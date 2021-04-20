a = int(input("dime el año"))
m = int(input("dime el mes"))
d = int(input("dime el dia"))

def comprobar_fecha(a, m, d,):
 
    #Array que almacenara los dias que tiene cada mes (si el ano es bisiesto, sumaremos +1 al febrero)
    dias_mes = [31, 28, 31, 30,31, 30, 31, 31, 30, 31, 30, 31]
 
 
    if((a%4 == 0 and a%100 != 0) or a%400 == 0):
        dias_mes[1] += 1
 
    if(m < 1 or m > 12):
        return False

    m -= 1
    if(d <= 0 or d > dias_mes[m]):
        return False
 
    return True
 
 
 
 
 
correcta = comprobar_fecha(a, m, d,)
 
#Mostrar el resultado:
if(correcta):
    print("\n\nLa fecha entrada es CORRECTA\n")
 
else:
    print("\n\nLa fecha entrada es FALSA\n")
