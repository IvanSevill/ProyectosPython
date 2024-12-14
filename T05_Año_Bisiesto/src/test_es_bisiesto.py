from es_bisiesto import *

print("\nPrograma para comprobar si un año es bisiesto")

año = int(input("Dime un año y te diré si es bisiesto o no: "))

while año > 0: 
    if esbisiesto(año):
        print("El año es bisiesto")
    else:
        print("El año NO es bisiesto")
    año = int(input("Dime un año y te diré si es bisiesto o no: "))
print("El programa ha finalizado")