from consumos import *

def test_lee_consumos(lista:list[Consumo])->None:
    print(f'Se han leido {len(lista)} registros')
    print('Los 3 primeros registros son:')
    for n in lista[:3]:
        print(n)
    print('\nLos 3 ultimos registros son:')
    for n in lista[-3:]:
        print(n)
    print()

def test_barrios_top_consumo(lista:list[Consumo],año:int,clase:str,entero:int=3)->None:
    print(f"Los {entero} barrios que consumen más {clase} en el año {año} son:")
    for n in barrios_top_consumo(lista,año,clase,entero):
        print(n)

    print(f"\nLos {3} barrios que consumen más {clase} en el año {año} son:")
    for n in barrios_top_consumo(lista,año,clase):
        print(n)
    print()

def test_media_consumo_edificios(lista:list[Consumo],clase:str)->None:
    print(f"La media de consumos de la clase {clase} es de {media_consumo_edificios(lista,clase)}")
    print()

def test_media_consumos_de_edificio_por_tipo_edificio(lista:list[Consumo],año:int,clase:str)->None:
    print(f"La media de consumo por tipo de eficicio en el año {año} y la clase {clase} es:")
    for n in media_consumos_de_edificio_por_tipo_edificio(lista,año,clase).items():
        print(n)
    print()

def test_incremento_anual_de_consumo_por_unidad(lista:list[Consumo],unidad:str)->None:
    for n in incremento_anual_de_consumo_por_unidad(lista,unidad):
        print(n)
    print()


if __name__ == '__main__':
    ruta_consumo = 'T24_Consumo_Energia_edificios/data/consumo_energia_edificios.csv'
    datos_consumo = lee_consumos(ruta_consumo)
    año = 2020
    clase = 'energia reactiva'
    entero = 10
    unidad = 'kVAr'

    # test_lee_consumos(datos_consumo)
    # test_barrios_top_consumo(datos_consumo,año,clase,entero)
    # test_media_consumo_edificios(datos_consumo,clase)
    # test_media_consumos_de_edificio_por_tipo_edificio(datos_consumo,año,clase)
    test_incremento_anual_de_consumo_por_unidad(datos_consumo,unidad)