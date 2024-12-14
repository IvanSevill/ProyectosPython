from gastos import *

def test_lee_gastos(lista:List[Gasto])->None:
    for n in lista:
        print(n)

def test_pagadores_y_conceptos(lista:List[Gasto])->None:
    print("Pagadores:")
    print(pagadores_y_conceptos(lista)[0])
    print("\nConceptos:")
    print(pagadores_y_conceptos(lista)[1])
    print()

def test_total_importe(lista:List[Gasto],f1:date=None,f2:date=None):
    print(f"El importe total entre el 5 y el 8 de abril de 2019 es de:",total_importe(lista,f1,f2))
    print(f"El importe total es de {total_importe(lista)}")
    print()

def test_conceptos_menos_gastos(lista:List[Gasto]):
    print("Los conceptos con menos gastos son:")
    print(conceptos_menos_gastos(lista))
    print()

def test_pagadores_mayor_importe_medio(lista:List[Gasto],entero:int):
    print(f"Los {entero} pagadores con un mayor importe medio son:")
    for n in pagadores_mayor_importe_medio(lista,entero):
        print(n)
    print()

def test_balance(lista:List[Gasto]):
    for n in balance(lista).items():
        print(n)

if __name__ == '__main__':
    ruta_gastos = 'T26_Gastos/data/gastos.csv'
    datos_gastos = lee_gastos(ruta_gastos)
    f1 = date(2019,4,5)
    f2 = date(2019,4,8)
    entero = 5

    # test_lee_gastos(datos_gastos)
    test_pagadores_y_conceptos(datos_gastos)
    test_total_importe(datos_gastos,f1,f2)
    test_conceptos_menos_gastos(datos_gastos)
    test_pagadores_mayor_importe_medio(datos_gastos,entero)
    test_balance(datos_gastos)