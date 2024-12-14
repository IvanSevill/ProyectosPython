from ecuación_segundo_grado import raices

print("Calculo de la solución de una ecuación de segundo grado")
print("Para ello introduce los siguientes parámetros")

c1 = float(input("Dime el coeficiente de x al cuadrado: "))
c2 = float(input("Dime el coeficiente de x: "))
c3 = float(input("Dime el termino independiente: "))

print("Las raices son: ", raices(c1,c2,c3))