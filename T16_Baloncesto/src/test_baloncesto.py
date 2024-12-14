from baloncesto import * 
# Marca: Me han sobrado 6 minutos y 21 segundos de 120 minutos.


def test_lee_partidos(lista:List[PartidoBasket])->None:
    for n in lista:
        print(n)
    print()

def test_equipo_con_mas_faltas(lista:List,conj:Set[str]=None)->None:
    print("El equipo con más faltas de los que están en el conjunto:")

    if conj != None:
        print(conj)
    else:
         print('{TODOS}')
    print("Es el",equipo_con_mas_faltas(lista,conj)[0],"con",equipo_con_mas_faltas(lista,conj)[1],"faltas")
    print()

def test_media_puntos_por_equipo(lista:List[PartidoBasket],competicion)->None:
    print("Equipos y sus medias de puntuación en la competición ",competicion,"son:")
    for n in media_puntos_por_equipo(lista,competicion).items():
        print(n)
    print()

def test_diferencia_puntos_anotados(lista:List[PartidoBasket],eq:str)->None:
    lista_resultados = diferencia_puntos_anotados(lista,eq)
    print("Equipo:",eq)
    print(lista_resultados)
    print()

def test_victorias_por_equipo(lista:List[PartidoBasket])->None:
    print("Victorias por equipos en todos los registros")
    print(victorias_por_equipo(lista))
    print()

def test_equipo_minimo_victorias(lista:List[PartidoBasket],entero:int)->None:
    print(f"Equipos con al menos {entero} victorias: ")
    for n in equipo_minimo_victorias(lista,entero):
        print(n)
    print()

def test_equipos_mas_victorias_por_año(lista:List[PartidoBasket],entero:int)->None:
    print(f"Equipos que superan {entero} victorias por año:")
    for n in equipos_mas_victorias_por_año(lista,entero).items():
        print(n)
    print()

if __name__ == "__main__":
    ruta = 'data/resultados_baloncesto.csv'
    datos_baloncesto = lee_partidos(ruta)
    conjunto = {'Barcelona','Unicaja','Real Madrid','Valencia Basket'}
    competicion = 'Copa del Rey'
    equipo_a_mirar = 'Barcelona'
    entero = 8

    # test_lee_partidos(datos_baloncesto)
    test_equipo_con_mas_faltas(datos_baloncesto,conjunto)
    test_media_puntos_por_equipo(datos_baloncesto,competicion)
    test_diferencia_puntos_anotados(datos_baloncesto,equipo_a_mirar)
    test_victorias_por_equipo(datos_baloncesto)
    test_equipo_minimo_victorias(datos_baloncesto,entero)
    test_equipos_mas_victorias_por_año(datos_baloncesto,entero)
