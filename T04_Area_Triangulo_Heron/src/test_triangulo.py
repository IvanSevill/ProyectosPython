from triangulo import *

print("\n\nIntroduce los lados de un triángulo para calcular su area")
l1 = float(input("Longitud del primer lado: "))
l2 = float(input("Longitud del segundo lado: "))
l3 = float(input("Longitud del tercer  lado: "))
a = area_por_heron(l1,l2,l3)
p = perimetro(l1,l2,l3)

print("El triángulo tiene un perimetro de {} unidades y de area {} unidades cuadradas.".format (p,a))
