from partido import *

def test_lee_resultado(lista:list[Partido])->None:
    print(f"Se han leido {len(lista)} registros")
    print(f"Los 3 primeros registros: ")
    for n in lista[:3]:
        print(n)
    
    print(f"\nLos 3 ultimos registros: ")
    for n in lista[-3:]:
        print(n)
    print()

def test_selecciones_enfrentadas_israel(lista:list[Partido],entero:int=3)->None:
    print(selecciones_enfrentadas_israel(lista,entero))
    print(len(selecciones_enfrentadas_israel(lista,entero)),"\n")

def test_lista_diferencias_goles(lista:list[Partido],fecha_inicio:datetime=None,fecha_final:datetime=None)->None:
    print("Lista con None y None")
    print(lista_diferencias_goles(lista))
    print(f"\nLista entre {fecha_inicio} y {fecha_final}")
    print(lista_diferencias_goles(lista,fecha_inicio,fecha_final))

def test_partidos_por_mes(lista:list[Partido])->None:
    print("\nRelación (mes, partidos) en TODOS los registros: ")
    print(partidos_por_mes(lista))

def test_partidos_mensuales_por_anyo(lista:list[Partido])->None:
    print("\nRelación (mes, partidos) separado por año: ")
    for n in partidos_mensuales_por_anyo(lista):
        print(n)

if __name__ == '__main__':
    ruta_partidos = 'T22_Partidos_Israel/data/resultadosIsrael.csv'
    datos_partidos = lee_resultado(ruta_partidos)
    fecha_inicio = date(2005,1,1)
    fecha_final = date(2007,1,1)
    año = 1954
    entero = 1

    test_lee_resultado(datos_partidos)
    test_selecciones_enfrentadas_israel(datos_partidos,entero)
    test_lista_diferencias_goles(datos_partidos,fecha_inicio,fecha_final)
    test_partidos_por_mes(datos_partidos)
    test_partidos_mensuales_por_anyo(datos_partidos)

