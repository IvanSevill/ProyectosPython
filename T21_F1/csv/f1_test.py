from f1 import *

def test_lee_carreras(lista:List[Carrera])->None:
    print(f'Se han leido {len(lista)} registros')
    print('Los 3 primeros registros son:')
    for n in lista[:3]:
        print(n)
    print()

def test_media_tiempo_boxes(lista:List[Carrera],ciudad:str,fecha:datetime)->None:
    print(f"La media de tiempo en {ciudad} el día {fecha} es de {media_tiempo_boxes(lista,ciudad,fecha)} segundos")
    print()

def test_pilotos_menor_tiempo_medio_vueltas_top(lista:List[Carrera],n:int)->None:
    print(f'Los {n} pilotos con menor tiempo por vueltas son:')
    for i in pilotos_menor_tiempo_medio_vueltas_top(lista,n):
        print(i)
    print()

def test_ratio_tiempo_boxes_total(lista:List[Carrera])->None:
    print('El mejor ratio de tiempo en boxes es:')
    for n in ratio_tiempo_boxes_total(lista):
        print(n)
    print()

def test_puntos_piloto_anyos(lista:List[Carrera])->None:
    print('Los puntos de los pilotos por años son:')
    for n in puntos_piloto_anyos(lista).items():
        print(n)
    print()

def test_mejor_escuderia_anyo(lista:List[Carrera],año:int):
    print(f'La mejor escudería en el año {año} es {mejor_escuderia_anyo(lista,año)}')
    print()


if __name__ == '__main__':
    ruta_carrera = 'T21_F1/data/f1.csv'
    datos_carrera = lee_carreras(ruta_carrera)
    fecha=date(2023, 5, 7) 
    año = 2022
    ciudad = 'Barcelona'
    entero = 5

    test_lee_carreras(datos_carrera)
    test_media_tiempo_boxes(datos_carrera,ciudad,fecha)
    test_pilotos_menor_tiempo_medio_vueltas_top(datos_carrera,entero)
    test_ratio_tiempo_boxes_total(datos_carrera)
    test_puntos_piloto_anyos(datos_carrera)
    test_mejor_escuderia_anyo(datos_carrera,año)