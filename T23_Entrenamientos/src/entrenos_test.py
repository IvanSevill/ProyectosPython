from entrenos import * 

def test_lee_entrenos(lista:list[Entreno])->None:
    for n in lista:
        print(n)

def test_porcentaje_calorias_por_tipo(lista:list[Entreno],conj_entrenos:set):
    for n in porcentaje_calorias_por_tipo(lista,conj_entrenos).items():
        print(n)
    print()

def test_año_mayor_distancia_media(lista:list[Entreno],d:int,c:bool=None):
    print(f"El año con una media mayor con el valor \'d = {d}\' y \'c = {c}\' es {año_mayor_distancia_media(lista,d,c)}")
    print(f"El año con una media mayor con el valor \'d = {d}\' y \'c = {None}\' es {año_mayor_distancia_media(lista,d)}")
    print()

def test_entrenos_mas_repetidos(lista:list[Entreno],f1:date,f2:date)->None:
    for n in entrenos_mas_repetidos(lista,f1,f2).items():
        print(n)
    print()

def test_incrementos_anuales_distancia(lista:list[Entreno]):
    print(incrementos_anuales_distancia(lista))

if __name__ == '__main__':
    ruta_entrenos = 'T23_Entrenamientos/data/entrenos.csv'
    datos_entrenos = lee_entrenos(ruta_entrenos)
    conj_entrenos = {"Andar", "Bici", "Correr"}
    compartido = False
    f2 = date(2022,1,1)
    f1 = date(2019,1,1)
    entero = 5

    # test_lee_entrenos(datos_entrenos)
    test_porcentaje_calorias_por_tipo(datos_entrenos,conj_entrenos)
    test_año_mayor_distancia_media(datos_entrenos,entero,compartido)
    test_entrenos_mas_repetidos(datos_entrenos,f1,f2) 
    test_incrementos_anuales_distancia(datos_entrenos)