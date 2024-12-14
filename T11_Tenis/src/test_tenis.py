from tenis import *

def test_lee_partidos_tenis(lista_tenis:List[PartidoTenis])->None:
    cabecera_ejercicio(1)
    print(f"Se han leido un total de {len(lista_tenis)} registros")
    print("Mostrando los 3 primeros registros:")
    contador = 1
    for n in lista_tenis[:3]:
        print(f"{contador} ==>",n)
        contador += 1

# 2)
def test_partidos_menos_errores(lista_tenis:List[PartidoTenis])->None:
    cabecera_ejercicio(2)
    print("El partido con menos errores forzados es:")
    print(partido_menos_errores(lista_tenis))

# 3)
def test_jugador_mas_partidos(lista_tenis:List[PartidoTenis])->None:
    cabecera_ejercicio(3)
    jugador = jugador_mas_partidos(lista_tenis)
    print(f"El jugador con más partidos jugados es {jugador[0]} con un total de {jugador[1]} partidos.")

# 4)
def test_tenista_mas_victorias(lista_tenis:List[PartidoTenis])->None:
    cabecera_ejercicio(4)
    ninguna = None
    f_desde = date(2013, 1, 1)
    f_hasta = date(2020, 1, 1)
    print(f"El tenista con más victorias entre las fechas {ninguna} y {ninguna} es {tenista_mas_victorias(lista_tenis,ninguna,ninguna)}")
    print(f"El tenista con más victorias entre las fechas {ninguna} y {f_hasta} es {tenista_mas_victorias(lista_tenis,ninguna,f_hasta)}")
    print(f"El tenista con más victorias entre las fechas {f_desde} y {ninguna} es {tenista_mas_victorias(lista_tenis,f_hasta,ninguna)}")
    print(f"El tenista con más victorias entre las fechas {f_desde} y {f_hasta} es {tenista_mas_victorias(lista_tenis,f_desde,f_hasta)}")

# 5)
def test_media_errores_por_jugador(lista_tenis:List[PartidoTenis])->None:
    cabecera_ejercicio(5)
    contador = 1
    print("Media de errores por jugador de menor a mayor es:")
    for n in media_errores_por_jugador(lista_tenis):
        print(contador,"-",n)
        contador += 1

# 6)
def test_jugadores_mayor_porcentaje_victorias(lista_tenis:List[PartidoTenis])->None:
    cabecera_ejercicio(6)
    print("Jugadores con mayor porcentaje de victorias: ")
    for n in jugadores_mayor_porcentaje_victorias(lista_tenis):
        print(n)

# 7)
def test_n_tenistas_con_mas_errores(lista_tenis:List[PartidoTenis],parametro:int)->None:
    cabecera_ejercicio(7)
    print(f"Los {parametro} tenistas con mayor número de errores no forzados son: ")
    for n in n_tenistas_con_mas_errores(lista_tenis,parametro):
        print(n)

# 8)
def test_fechas_ordenadas_por_jugador(lista_tenis:List[PartidoTenis]):
    cabecera_ejercicio(8)
    for n in fechas_ordenadas_por_jugador(lista_tenis).items():
        print(n)
    # for jugador,partidos in fechas_ordenadas_por_jugador(lista_tenis).items():
    #     print(jugador,len(partidos))

# 9)
def test_num_partidos_nombre(lista_tenis:List[PartidoTenis],tenista)->None:
    cabecera_ejercicio(9)
    print(f"Partidos jugados por {tenista} en cada tipo de pista: ")
    for pista,resultado in num_partidos_nombre(lista_tenis,tenista).items():
        print(pista,"-->",resultado)

# 10)
def test_num_tenistas_distintos_por_superficie(lista_tenis:List[PartidoTenis])->None:
    cabecera_ejercicio(10)
    print("El número de tenistas distintos segun cada superficie es:")
    for superficie,valor in num_tenistas_distintos_por_superficie(lista_tenis).items():
        print(superficie,"-->",valor)

# 11)
def test_superficie_con_mas_tenistas_distintos(lista_tenis:List[PartidoTenis])->None:
    cabecera_ejercicio(11)
    tupla = superficie_con_mas_tenistas_distintos(lista_tenis)
    print(f"La superficie con más tenistas distintos es {tupla[0]} con {tupla[1]} tenistas.")

# 12)
def test_mas_errores_por_jugador(lista_tenis:List[PartidoTenis])->None:
    cabecera_ejercicio(12)
    for nombre,n in mas_errores_por_jugador(lista_tenis).items():
        print(nombre,"-->",n,"\n")

# 13)
def test_partido_mas_errores_por_mes(lista_tenis:List[PartidoTenis],superficies:List=None)->None:
    cabecera_ejercicio(13)
    print(f"Los partidos con más errores en las superficies {superficies} son:")
    for mes,datos in sorted(partido_mas_errores_por_mes(lista_tenis,superficies).items()):
        print(mes,"-->",datos)

# 14)
def test_n_partidos_mas_errores_por_jugador(lista_tenis:List[PartidoTenis],entero:int)->None:
    cabecera_ejercicio(14)
    print(f"Lista de los {entero} partidos que ha cometido más errores por tenista: ")
    for tenista,partido in n_partidos_mas_errores_por_jugador(lista_tenis,entero).items():
        print(f"\n{tenista}:")
        for n in partido:
            print("=>",n[0])

# 15)
def test_mayor_numero_dias_sin_jugar(lista_tenis:List[PartidoTenis],tenista:str)->None:
    cabecera_ejercicio(15)
    mayor_dias = mayor_numero_dias_sin_jugar(lista_tenis,tenista)
    print(f"El mayor número de días sin que el jugador {tenista} ha estado sin jugar es {mayor_dias.days}.")
    
if __name__ == "__main__":
    cabecera("EJERCICIO SOBRE TENIS") 
    ruta_tenis = "T11_Tenis/data/tenis.csv"
    datos_tenis = lee_partidos_tenis(ruta_tenis)
    parametro = 3
    tenista = "Carlos Alcaraz"
    superficies = ["Sintética","Tierra"]

    # test_lee_partidos_tenis(datos_tenis)
    # test_partidos_menos_errores(datos_tenis)
    # test_jugador_mas_partidos(datos_tenis)
    # test_tenista_mas_victorias(datos_tenis)
    # test_media_errores_por_jugador(datos_tenis)
    # test_jugadores_mayor_porcentaje_victorias(datos_tenis)
    # test_n_tenistas_con_mas_errores(datos_tenis,parametro)
    # test_fechas_ordenadas_por_jugador(datos_tenis)
    # test_num_partidos_nombre(datos_tenis,tenista)
    # test_num_tenistas_distintos_por_superficie(datos_tenis)
    # test_superficie_con_mas_tenistas_distintos(datos_tenis)
    # test_mas_errores_por_jugador(datos_tenis)
    test_partido_mas_errores_por_mes(datos_tenis,superficies)
    # test_n_partidos_mas_errores_por_jugador(datos_tenis,parametro)
    test_mayor_numero_dias_sin_jugar(datos_tenis,tenista)