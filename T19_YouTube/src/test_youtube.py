from youtube import *

def test_lee_trending_videos(lista:List[Videos])->None:
    print(f"Se han leido {len(lista)} registros")
    print("Los 3 primeros registros:")
    for n in lista[:3]:
        print(n)
    print("\nLos 3 últimos registros:")
    for n in lista[-3:]:
        print(n)
    print()

def test_media_visitas(lista:List[Videos],fecha:datetime)->None:
    print(f"La media de el día {datetime.strftime(fecha,'%d/%m/%Y')} es {media_visitas(lista,fecha)}")
    print()

def test_video_mayor_ratio_likes_dislikes(lista:List[Videos],categoria:str=None):
    print(f"El video con mayor ratio de likes frente a dislikes en la categoría {categoria} es:")
    print(video_mayor_ratio_likes_dislikes(lista,categoria))
    print(f"\nEl video con mayor ratio de likes frente a dislikes entre todos los registros es:")
    print(video_mayor_ratio_likes_dislikes(lista))
    print()

def test_canales_top(lista:List[Videos],entero:int)->None:
    print(f"Los 3 canales top son: ")
    for n in canales_top(lista):
        print(n)
    print()

    print(f"Los {entero} canales top son: ")
    for n in canales_top(lista,entero):
        print(n)
    print()

def test_video_mas_likeability_por_categoria(lista:List[Videos],k:int)->None:
    print(f"Videos con más likeability con constante {k}")
    for n in video_mas_likeability_por_categoria(lista,k):
        print(n)
    print()

def test_incrementos_visitas(lista:List[Videos],canal:str)->None:
    print(f"De los {len(incrementos_visitas(lista,canal))} días registrados, estos son los resultados de incrementos en el canal {canal}:")
    print(incrementos_visitas(lista,canal))

if __name__ == "__main__":
    ruta_videos = "T19_YouTube/data/YouTube.csv"
    datos_videos = lee_trending_videos(ruta_videos)
    fecha = date(2017,11,14)
    categoria = 'Education'
    # canal = 'Exatlón'
    canal = 'Mr. Tops'
    entero = 5

    test_lee_trending_videos(datos_videos)
    test_media_visitas(datos_videos,fecha)
    test_video_mayor_ratio_likes_dislikes(datos_videos,categoria)
    test_canales_top(datos_videos,entero)
    test_video_mas_likeability_por_categoria(datos_videos,entero)
    test_incrementos_visitas(datos_videos,canal)