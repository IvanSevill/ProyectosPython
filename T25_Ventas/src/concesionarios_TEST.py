from concesionarios import *

def test_lee_ventas(lista:List[Venta])->None:
    print(f"Se han leido {len(lista)} registros")
    print("Los 3 primeros registros son:")
    for n in lista[:3]:
        print(n)
    print("\nLos 3 ultimos registros son:")
    for n in lista[-3:]:
        print(n)
    print()

def test_unidades_vendidas(lista:List[Venta],conj_modelos:Set[str],f1:date,f2:date)->None:
    print(f"Entre las fechas {f1} y {f2} se han vendido de los modelos: {conj_modelos} un total de {unidades_vendidas(lista,conj_modelos,f1,f2)} unidades")
    print()

def test_dicc_beneficios_por_modelo_año(lista:List[Venta],año:int)->None:
    print(f"Los beneficiones divididos por unidades vendidas en el año {año} es de:")
    for n in dicc_beneficios_por_modelo_año(lista,año).items():
        print(n)
    print()

def test_dias_de_mas_unidades(lista:List[Venta])->None:
    print("Los días con más ventas de una unica vez son:")
    print(dias_de_mas_unidades(lista))
    print()

def test_lista_dif_unidades_mes(lista:List[Venta])->None:
    print("La lista de diferencias de unidades vendidas por mes es:")
    print(lista_dif_unidades_mes(lista))
    print()

def test_modelos_vendidos_mas_n_en_año(lista:List[Venta],año:int,entero:int)->None:
    print(f"Los modelos vendidos en el año {año} en más de {entero} ciudades son:")
    print(modelos_vendidos_mas_n_en_año(lista,año,entero))

if __name__ == '__main__':
    ruta_ventas = 'T25_Ventas/data/ventas.csv'
    datos_ventas = lee_ventas(ruta_ventas)
    conj_modelos = {'MODELO-A','MODELO-C'}
    f1 = date(2017,1,1) 
    f2 = date(2017,3,1) 
    año = 2012
    entero = 2

    test_lee_ventas(datos_ventas)
    test_unidades_vendidas(datos_ventas,conj_modelos,f1,f2)
    test_dicc_beneficios_por_modelo_año(datos_ventas,año)
    test_dias_de_mas_unidades(datos_ventas)
    test_lista_dif_unidades_mes(datos_ventas)
    test_modelos_vendidos_mas_n_en_año(datos_ventas,año,entero)
