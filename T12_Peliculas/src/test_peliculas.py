from peliculas import *

# 1)
def test_lee_peliculas(lista:list[Peliculas])->None:
    for n in lista:
        print(n)

# 2)
def test_genero_mas_frecuente(dict_generos:dict)->None:
    tupla = genero_mas_frecuente(dict_generos)
    cabecera_ejercicio(2)
    print(f"El género más frecuente es el de {tupla[0]} con {tupla[1]} peliculas ")

# 3)
def test_mejor_valorada_por_idioma(lista:list[Peliculas])->None:
    cabecera_ejercicio(3)
    for n in mejor_valorada_por_idioma(lista):
        print(n)

# 4)
def test_media_calificaciones(lista:list[Peliculas],generos_dados:list[str])->None:
    cabecera_ejercicio(4)
    print(f"El promedio de las peliculas que tienen exactamente los generos {generos_dados} es de {media_calificaciones(lista,generos_dados)}")

# 5)
def test_top_n_por_genero(lista:list[Peliculas],limite:int):
    cabecera_ejercicio(5)
    print("-"*160)
    for clave,valor in top_n_por_genero(lista,limite).items():
        print(f"Top {limite} {clave}:")
        for n in valor:
            print(n)
        print("-"*160)

    
if __name__ == '__main__':
    ruta_peliculas = 'T12_Peliculas\data\movies_fp.csv'
    ruta_generos = 'T12_Peliculas\data\movies_fp_genres.csv'
    datos_peliculas = lee_peliculas(ruta_peliculas,ruta_generos)
    datos_generos = lee_generos(ruta_generos)
    generos_dados = ['Drama', 'Adventure']
    limite = 1

    # test_lee_peliculas(datos_peliculas)
    test_genero_mas_frecuente(datos_generos)
    test_mejor_valorada_por_idioma(datos_peliculas)
    test_media_calificaciones(datos_peliculas,generos_dados)
    test_top_n_por_genero(datos_peliculas,limite)
