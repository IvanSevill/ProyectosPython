from partidas import *

def test_lee_partidas(lista:List[Partida])->None:
    print("\nLos 3 primeros registros:")
    for n in lista[:3]:
        print(n)
    print("\nLos 3 últimos registros:")
    for n in lista[-3:]:
        print(n)
    print()

def test_victoria_mas_rapida(lista:List[Partida])->None:
    res = victoria_mas_rapida(lista)
    print(f"La partida más rápida fue entre {res[0]} y {res[1]} y duró {res[2]} segundos.")
    print()

def test_top_ratio_medio_personajes(lista:List[Partida],entero:int)->None:
    print(f"Los {entero} ratios medios más bajos puntuación/tiempo son: ")
    print(top_ratio_medio_personajes(lista,entero))
    print()

def test_enemigos_mas_debiles(lista:List[Partida],personaje:str):
    print(f"Los enemigos más debiles contra {personaje} son: {enemigos_mas_debiles(lista,personaje)}")
    print()

def test_movimientos_comunes(lista:List[Partida],personaje1:str,personaje2:str)->None:
    mov_comunes =movimientos_comunes(lista,personaje1,personaje2)
    if len(mov_comunes)>0:
        print(f"Los movimientos que tienen en común {personaje1} y {personaje2} son: {mov_comunes}")
    else:
        print(f"{personaje1} y {personaje2} no tienen movimientos comunes.")
    print()

def test_dias_mas_combos_finish(lista:List[Partida])->None:
    print(f"El día que más combos finish ha habido es el {dias_mas_combos_finish(lista)}.")
    print()

if __name__ == "__main__":
    ruta_partidas = "T17_Street_Fighters/data/games.csv"
    datos_partidas = lee_partidas(ruta_partidas)
    personaje1 = "Ken"
    personaje2 = "Ryu"
    entero = 3

    test_lee_partidas(datos_partidas)
    test_victoria_mas_rapida(datos_partidas)
    test_top_ratio_medio_personajes(datos_partidas,entero)
    test_enemigos_mas_debiles(datos_partidas,personaje1)
    test_movimientos_comunes(datos_partidas,personaje1,personaje2)
    test_dias_mas_combos_finish(datos_partidas)