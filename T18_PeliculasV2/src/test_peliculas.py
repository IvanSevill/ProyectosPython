from peliculas import *

def test_lee_peliculas(lista:Pelicula)->None:
    for n in lista:
        print(n)

def test_pelicula_mas_ganancias(lista:Pelicula,genero)->None:
    res1 = pelicula_mas_ganancias(lista,genero)
    res2 = pelicula_mas_ganancias(lista)
    print(f"\nLa película con más ganancias del género {genero} es {res1[0]} con una ganancia de {res1[1]}")
    print(f"La película con más ganancias si género es {res2[0]} con una ganancia de {res2[1]}")
    print()

def test_media_presupuesto_por_genero(lista:Pelicula)->None:
    print("Media de presupuestos por generos:")
    for n in media_presupuesto_por_genero(lista).items():
        print(n)
    print()

def test_peliculas_por_actor(lista:Pelicula,año_inicial:datetime=None,año_final:datetime=None)->None:
    print("Todos los registros:")
    print(peliculas_por_actor(lista))
    print(f"\nDesde {año_inicial.year} hasta {año_final.year}:")
    print(peliculas_por_actor(lista,año_inicial,año_final))
    print()

def test_actores_mas_frecuentes(lista:Pelicula,entero:int,año_inicial:datetime=None,año_final:datetime=None):
    print(f"Los {entero} actores o actrices más frecuentes entre los años {año_inicial.year} y {año_final.year} son:")
    print(actores_mas_frecuentes(lista,entero,año_inicial,año_final))
    print()

def test_recaudacion_total_por_año(lista:Pelicula,generos:set)->None:
    print("Recaudación en todos los géneros:")
    print(recaudacion_total_por_año(lista))
    print(f"\nRecaudación en los géneros -> {generos}:")
    print(recaudacion_total_por_año(lista,generos))
    print()

def test_incrementos_recaudacion_por_año(lista:Pelicula,generos:set)->None:
    print("Incremento de la recaudación en todos los géneros:")
    print(incrementos_recaudacion_por_año(lista))
    print(f"\nIncremento de la recaudación en los géneros -> {generos}:")
    print(incrementos_recaudacion_por_año(lista,generos))
    print()

if __name__ == '__main__':
    ruta_peliculas = 'T18_PeliculasV2/data/peliculas.csv'
    datos_peliculas = lee_peliculas(ruta_peliculas)
    genero = 'Ciencia ficción'
    año_inicial = date(2005,1,1)
    año_final = date(2015,1,1)
    entero = 3
    conjunto_generos = {'Drama', 'Acción'}

    test_lee_peliculas(datos_peliculas)
    test_pelicula_mas_ganancias(datos_peliculas,genero)
    test_media_presupuesto_por_genero(datos_peliculas)
    test_peliculas_por_actor(datos_peliculas,año_inicial,año_final)
    test_actores_mas_frecuentes(datos_peliculas,entero,año_inicial,año_final)
    test_recaudacion_total_por_año(datos_peliculas,conjunto_generos)
    test_incrementos_recaudacion_por_año(datos_peliculas,conjunto_generos)