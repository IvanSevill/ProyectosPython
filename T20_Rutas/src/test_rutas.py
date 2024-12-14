from rutas import *

def test_lee_rutas(lista:List[Ruta])->None:
    for n in lista:
        print(n)

def test_acumular_kms_por_meses(lista:List[Ruta])->None:
    for n in acumular_kms_por_meses(lista).items():
        print(n)

def test_diferencias_kms_meses_anyo(lista:List[Ruta])->None:
    for n in diferencias_kms_meses_anyo(lista).items():
        print(n)

def test_top_rutas_lejanas(lista:List[Ruta],n:int,c:Coordenada,km_min:int=None)->None:
    for n in top_rutas_lejanas(lista,n,c,km_min):
        print(n)

def test_ciudades_top_tiempo_dificultad(lista:List[Ruta],n:int)->None:
    for n in ciudades_top_tiempo_dificultad(lista,n).items():
        print(n)

if __name__ == '__main__':
    ruta_ruta = 'T20_Rutas/data/rutas_motos.csv'
    datos_ruta = lee_rutas(ruta_ruta)
    n = 3
    c = Coordenada(35.15,-8.76)
    km_min = 40

    # test_lee_rutas(datos_ruta)
    # test_acumular_kms_por_meses(datos_ruta)
    # test_diferencias_kms_meses_anyo(datos_ruta)
    test_top_rutas_lejanas(datos_ruta,n,c)
    test_ciudades_top_tiempo_dificultad(datos_ruta,n)