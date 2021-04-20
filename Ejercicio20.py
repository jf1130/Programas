print("--------calculadora de divisas--------")
print("pesos mexicanos y colombianos")

E = int(input("ingresa 1 si quieres pesos COL a MEX y 2 de MEX a COL"))

if(E == 1):
    pcol = int(input("dime la cantidad de pesos colombianos")) 
    resultado = pcol * 0.0057
    print("el resultado de tu calculo es " + str(resultado))
if(E == 2):
    pmew = float(input("dime la cantidad de pesos mexicanos"))
    resultado = pmew * 176.54 
    print("el resultado de tu calculo es " + str(resultado))
