from cadena import *

print("¿Es tu número un palíndromo?")
print("Nota: Una cadena es un palíndromo si se lee igual de derecha a izquierda como de izquierda aderecha")
cadena = str(input("Introduce tu cadena: "))

if es_palindromo(cadena):
    print("¡Enhorabuena!, \'{}\' es un palíndromo".format(cadena))
else:
    print("Tu número NO es un palíndromo")

print("Se ha teminado el programa")