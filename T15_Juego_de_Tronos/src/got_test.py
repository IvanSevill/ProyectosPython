from got import *

def test_lee_batallas(lista:list[BatallaGOT])->None:
    print("(1)\t Test de la función lee batallas")
    print("\t Los 3 primeros registros son:")
    for n in lista[:3]:
        print(n)
    print("Los 3 últimos registros son:")
    for n in lista[-3:]:
        print(n)
    print()

def test_reyes_mayor_menor_ejercito(lista:list[BatallaGOT])->None:
    contador = 1
    print("(2)\t El reyes y sus ejercitos ordenados de mayor a menor:")
    for rey, ejercito in reyes_mayor_menor_ejercito(lista):
        print(f"\t {contador}º",rey,"==>",ejercito)
        contador += 1
    print()

def test_batallas_mas_comandantes(lista:List[BatallaGOT],regiones:List[str],limite:int=None)->None:
    print(f"(3)\t Las {limite} batalla con más comandantes en {regiones} son:")
    for n in batallas_mas_comandantes(lista,regiones,limite):
        print("\t",n)
    print()

def test_rey_mas_victorias(lista:List[BatallaGOT],rol:str="ambos")->None:
    print(f"(4)\t El rey con más victorias como rol \"{rol}\" es {rey_mas_victorias(lista,rol)}")
    print()

def test_rey_mas_victorias_por_region(lista:List[BatallaGOT],rol:str="ambos")->None:
    print(f"(5)\t Los reyes con más victorias como rol \"{rol}\" son:")
    for n in rey_mas_victorias_por_region(lista,rol):
        print("\t",n)

if __name__ == "__main__":
    ruta_batallas = "T15_Juego_de_Tronos/data/battles.csv"
    datos_batallas = lee_batallas(ruta_batallas)
    regiones = ['The North', 'The Riverlands']
    num_limite = 5
    rol = "ambos"

    # test_lee_batallas(datos_batallas)
    test_reyes_mayor_menor_ejercito(datos_batallas)
    test_batallas_mas_comandantes(datos_batallas,regiones,num_limite)
    test_rey_mas_victorias(datos_batallas,rol)
    test_rey_mas_victorias_por_region(datos_batallas,rol)