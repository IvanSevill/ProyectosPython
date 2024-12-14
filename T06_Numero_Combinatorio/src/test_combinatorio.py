from combinatoria import *

print("\nNumero Combinatorio")
n1 = int(input("Dime el primer número: "))
n2 = int(input("Dime el segundo número: "))

if n1 < n2:
    print("El numerador es más pequeño que el denominador")
else:
    sol = numero_combinatorio(n1,n2)
    print("{} sobre {} es {}".format(n1,n2,sol))