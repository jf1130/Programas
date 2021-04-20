x =  int(input('ingrese el primer numero'))
y =  int(input('ingrese el segundo numero'))
z =  int(input('ingrese 1 para sumar 2 para restar 3 para multiplicar 4 para dividir 5 para potencia'))

if (z == 1):
   r = x + y
   print(r)

if (z == 2):
   r = x - y
   print(r)

if (z == 3):
   r = x * y 
   print(r)

if (z == 4):
   r = x / y
   print(r)

if (z == 5):
   r = x ** y
   print(r)
