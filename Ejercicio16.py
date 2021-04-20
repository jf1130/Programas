x =  int(input('ingrese el primer numero'))
y =  int(input('ingrese el segundo numero'))
seleccionOp =  int(input('ingrese 1 para sumar 2 para multiplicar 3 para dividir'))

if (seleccionOp == 1):
   r = x + y
   print(r)

if (seleccionOp == 2):
   r = x * y
   print(r)

if (seleccionOp == 3):
   r = x / y 
   print(r)
