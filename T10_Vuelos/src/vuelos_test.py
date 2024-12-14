from vuelos import *

# 0)
def test_lee_vuelos(lista:list[Vuelo])->None:
    print(f'Se han leido {len(lista)} registros')

    separador()
    print('Los tres primeros registros:')
    for n in lista[:3]:
        print("-->", n)
    separador()

    print('Los tres últimos registros:')
    for n in lista[-3:]:
        print("-->", n)
    separador()

# 1)
def test_filtra_vuelos_a(lista:list[Vuelo],destino:str)->None:
    vuelos_a = filtra_vuelos_a(lista,destino)
    print(f"Lista de vuelos con el destino recibido: {destino}")
    for n in vuelos_a:
        print(n)
    separador()

# 2)
def test_vuelos_mas_velocidad_que(lista:list[Vuelo],velocidad:str)->None:
    vuelos_mas_velocidad = vuelos_mas_velocidad_que(lista,velocidad)
    print(f"Lista de vuelos con una velocidad media mayor que {velocidad} km/h: ")
    for n in vuelos_mas_velocidad:
        print(n)
    separador()

# 3)
def test_todos_vuelos_mas_velocidad_que(lista:list[Vuelo],velocidad:str)->None:
    res = todos_vuelos_mas_velocidad_que(lista,velocidad)
    if res:
        print(f"Todos los vuelos van a una velocidad de al menos {velocidad} km/h")
    else:
        print(f"NO todos los vuelos van a una velocidad de al menos {velocidad} km/h")
    separador()

# 4)
def test_vuelos_mas_velocidad(lista:list[Vuelo])->None:
    mas_rapido = vuelos_mas_velocidad(lista)
    print("El vuelo más rápido es: ")
    print(mas_rapido)
    separador()

# 5)
def test_vuelos_por_horario(lista:list[Vuelo],mes)->None:
    print(f"Vuelos que salen el mes {mes} ordenados por fecha")
    vuelos = vuelos_por_horario(lista,mes)
    # for destino,precio,fecha_salida,hora_salida in vuelos:
    #     print(destino,precio,fecha_salida,hora_salida)
    for n in vuelos:
        print(n)
    separador()

# 6)
def test_distintas_escalas(lista:list[Vuelo])->None:
    print("Distintas escalas totales que se hacen")
    escalas = distintas_escalas(lista)
    for n in escalas:
        print(n)
    separador()


# 7)
def test_vuelos_con_escalas_en(lista:list[Vuelo],ciudad:str)->None:
    print(f"Los vuelos con escalas en {ciudad} son:")
    for n in vuelos_con_escalas_en(lista,ciudad):
        print(n)
    separador()

# 8)
def test_numero_de_vuelo_por_destino(lista:list[Vuelo])->None:
    print("Destinos a los que se hacen vuelos: ")
    dic_vuelo_destino = numero_de_vuelos_por_destino(lista)

    # a) Se visualice el diccionario directamente con un print.
    print("Diccionario de una vez:",dic_vuelo_destino,"\n")

    # b) Se visualice cada clave-valor una debajo de otra.
    for p in dic_vuelo_destino:
        print(p,dic_vuelo_destino[p])

    # c) Pida por teclado un destino y devuelva "Hay vuelo" o "No hay vuelo"
    # según el destino esté o no en el diccionario.
    destino = input("\nIntroduce un destino: ")
    if destino in dic_vuelo_destino:
        print("Hay vuelo")
    else:
        print("No hay vuelo")
    separador()

# 9)
def test_suma_de_pasajeros_por_fechas(lista:list[Vuelo])->None:
    print("Pasajeros totales por fechas: ")
    dict = suma_de_pasajeros_por_fechas(lista)
    # a) Se visualice el diccionario directamente con un print.
    print("Diccionario de una vez:",dict,"\n")

    # b) Se visualice cada clave-valor una debajo de otra.
    print("Diccionario pareja a pareja:")
    for p in dict:
        print(p,"-->",dict[p])

    # c) Pida por teclado una fecha y devuelva el número de pasajeros o cero (0)
    # según haya o no vuelos en esa fecha.
    fecha = input("\nIntroduce una fecha del modelo: \"12-02-2005\" : ")
    fecha = datetime.strptime(fecha,"%d-%m-%Y").date()
    if fecha not in dict:
        print(f"No se encuentran vuelos en la fecha deseada: {fecha}")
    else:
        print(f"Se ha encontrado un vuelo para el {fecha} con {dict[fecha]} pasajeros")
    separador()

# 10)
def test_lista_destinos_por_compañia(lista:list[Vuelo])->None:
    print("Lista de destinos a los que va cada compañía: ")
    print(lista_destinos_por_compañia(lista))
    separador()

# 11)
def test_vuelos_entre_fechas(lista:list[Vuelo],fecha_inicial=None,fecha_final=None)->None:
    print(f"Los vuelos desde {fecha_inicial}:")
    for n in vuelos_entre_fechas(lista,fecha_inicial):
        print("-->",n)

    print(f"\nVuelos hasta {fecha_final}:")
    for n in vuelos_entre_fechas(lista,fecha_final=fecha_final):
        print("-->",n)

    print(f"\nLos datos entre las fechas {fecha_inicial} y {fecha_final} son:")
    for n in vuelos_entre_fechas(lista,fecha_inicial,fecha_final):
        print("-->",n)
    separador()

# 12)
def test_destinos_distintos_por_compañia(lista:list[Vuelo])->None:
    print("Lista de los distintos destinos a los que va cada compañía: ")
    for n in destinos_distintos_por_compañia(lista).items():
        print(n)
    separador()

# 13)
def test_codigos_vuelos_mas_plazas_que_por_numero_de_escalas(lista:list[Vuelo],numero_limite:int)->None:
    print(f"Listado de vuelos separados por el número de escalas que realizan con más de {numero_limite} plazas: ")
    for n in sorted(codigos_vuelos_mas_plazas_que_por_numero_de_escalas(lista,numero_limite).items()):
        print(n)
    separador()

# 14)
def test_vuelos_menor_duracion_por_destino(lista:list[Vuelo])->None:
    print("Destinos y su vuelo con menor duración: ")
    for n in sorted(vuelos_menor_duracion_por_destino(lista).items()):
        print(n)
    separador()

# 15)
def test_promedio_de_precios_por_compañia(lista:list[Vuelo],economico:bool)->None:
    precios = "baratos" if economico else "caros"
    print(f"Promedio de los precios {precios} de cada compañia: ")
    for n in sorted(promedio_de_precios_por_compañia(lista,economico).items()):
        print(n)
    separador()

#16)
def test_n_vuelos_mayor_velocidad_por_meses(lista:list[Vuelo],numero:int)->None:
    for n in n_vuelos_mayor_velocidad_por_meses(lista,numero).items():
        print(n)
    separador()

# 17)
def test_escala_por_la_que_pasan_mas_vuelos_entre_fechas(lista:list[Vuelo],fecha_inicial:date,fecha_final:date)->None:
    print(f"El lugar en el que pasan más escalas desde la fecha {fecha_inicial} es {escala_por_la_que_pasan_mas_vuelos_entre_fechas(lista,fecha_inicial)}")
    print(f"El lugar en el que pasan más escalas hasta la fecha {fecha_final} es {escala_por_la_que_pasan_mas_vuelos_entre_fechas(lista,fecha_final=fecha_final)}")
    print(f"El lugar en el que pasan más escalas entre las fechas {fecha_inicial} y {fecha_final} es {escala_por_la_que_pasan_mas_vuelos_entre_fechas(lista,fecha_inicial,fecha_final)}")
    separador()

# 18)
def test_vuelo_con_mayor_porcentaje_de_ocupación_por_destino(lista:list[Vuelo])->None:
    for n in vuelo_con_mayor_porcentaje_de_ocupación_por_destino(lista).items():
        print(n)
    separador()

# 19)
def test_destino_menor_promedio_de_precios_mayor_porcentaje_ocupación(lista:list[Vuelo],porcentaje_limite:int):
    destino = min(destino_menor_promedio_de_precios_mayor_porcentaje_ocupación(lista,porcentaje_limite),key=lambda e:e[1])
    print("El destino al que, de promedio, cuesta menos el billete de los vuelos cuyo porcentaje de ocupación sea mayor o igual que {} % es {} con un precio de {:.2f} euros".format(porcentaje_limite,destino[0],destino[1]))    
    separador()

# 20)
def test_compañia_con_mas_pasajeros_por_destino(lista:list[Vuelo]):
    for destino,compañia in compañia_con_mas_pasajeros_por_destino(lista).items():
        print(f"La compañia a {destino} con más pasajeros es {compañia}.")
    separador()

# 21)
def test_calcular_el_incremento_o_decremento_de_pasajeros(lista:list[Vuelo]):
    for fecha,incremento_decremento in calcular_el_incremento_o_decremento_de_pasajeros(lista)[1:]:
        print(f"El día {fecha} varío un {incremento_decremento} respecto al día anterior.")
    separador()


if __name__ == '__main__':

    # ----------------------------- VARIABLES COMUNES AL RESTO DE FUNCIONES -----------------------------

    cabecera()
    datos_vuelos = lee_vuelos('T10_Vuelos/data/vuelos.csv')
    vel_max = 900
    fecha_inicial = date(2023,1,1)
    fecha_final = date(2023,12,31)
    destino = "Santiago"
    mes = 7
    numero_limite = 3
    economico = False
    porcentaje_limite = 90

    # -------------------------------- CONJUNTO DE FUNCIONES TEST DEL PROJECTO VUELOS --------------------------------

    # test_lee_vuelos(datos_vuelos)                                                                             # 0)
    # test_filtra_vuelos_a(datos_vuelos,destino)                                                                # 1)
    # test_vuelos_mas_velocidad_que(datos_vuelos,vel_max)                                                       # 2)
    # test_todos_vuelos_mas_velocidad_que(datos_vuelos,vel_max)                                                 # 3)
    # test_vuelos_mas_velocidad(datos_vuelos)                                                                   # 4)
    # test_vuelos_por_horario(datos_vuelos,mes)                                                                 # 5)
    # test_distintas_escalas(datos_vuelos)                                                                      # 6)
    # test_vuelos_con_escalas_en(datos_vuelos,destino)                                                          # 7)
    # test_numero_de_vuelo_por_destino(datos_vuelos)                                                            # 8)
    # test_suma_de_pasajeros_por_fechas(datos_vuelos)                                                           # 9)
    # test_lista_destinos_por_compañia(datos_vuelos)                                                            # 10)
    # test_vuelos_entre_fechas(datos_vuelos,fecha_inicial,fecha_final)                                          # 11)
    # test_destinos_distintos_por_compañia(datos_vuelos)                                                        # 12)
    # test_codigos_vuelos_mas_plazas_que_por_numero_de_escalas(datos_vuelos,numero_limite)                      # 13)
    # test_vuelos_menor_duracion_por_destino(datos_vuelos)                                                      # 14)
    # test_promedio_de_precios_por_compañia(datos_vuelos,economico)                                             # 15)
    # test_n_vuelos_mayor_velocidad_por_meses(datos_vuelos,numero_limite)                                       # 16)
    # test_escala_por_la_que_pasan_mas_vuelos_entre_fechas(datos_vuelos,fecha_inicial,fecha_final)              # 17)
    # test_vuelo_con_mayor_porcentaje_de_ocupación_por_destino(datos_vuelos)                                    # 18)
    # test_destino_menor_promedio_de_precios_mayor_porcentaje_ocupación(datos_vuelos,porcentaje_limite)         # 19)
    # test_compañia_con_mas_pasajeros_por_destino(datos_vuelos)                                                 # 20)
    test_calcular_el_incremento_o_decremento_de_pasajeros(datos_vuelos)                                       # 21)
