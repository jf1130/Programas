p =  int(input('Ingrese su peso en kilos'))
a =  int(input('Ingrese su altura en centimetros'))
A = a / 100
AF= A * A
imc = p / AF

if (imc < 18.5):
    print("usted esta tan flaco que parece baretero")

if (imc > 18.5):
    if (imc < 24.9):
        print("usted esta normal")

if (imc > 25):
    if (imc < 29.9):
        print("un poquito de Gym no te caeria nada mal para bajar los kilos de mas")

if (imc > 30):
    print("eres mas grasa que persona")      
