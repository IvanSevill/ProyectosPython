from compras import *

def separador():
    print("\n")

def test_lee_compras(lista_compras:List[Compras])->None:
    print(lista_compras)

def test_compra_maxima_minima_provincia(lista_compras:List[Compras],provincia:str)->None:
    maximo_minimo = compra_maxima_minima_provincia(lista_compras,provincia)
    print(f"En {provincia}, la compra máxima es de {maximo_minimo[0]} euros y la mínima es de {maximo_minimo[1]} euros.")
    separador()

def test_hora_menos_afluencia(lista_compras:List[Compras])->None:
    print(f"La hora a la que hay menos afluencia es a las {hora_menos_afluencia(lista_compras)[0]} con un total de {hora_menos_afluencia(lista_compras)[1]} clientes.")
    separador()

def test_supermercados_mas_facturacion(lista_compras:List[Compras],limite:int):
    print(f"Los {limite} supermercados con mayor facturación son: ")
    for n in supermercados_mas_facturacion(lista_compras,limite):
        print(n)
    separador()

def test_clientes_itinerantes(lista_compras:List[Compras],limite:int)->None:
    for n in clientes_itinerantes(lista_compras,limite):
        print(n)
    separador()

def test_dias_estrella(lista_compras:List[Compras],provincia:str,supermercado:str)->None:
    for n in dias_estrella(datos_compras,provincia,supermercado):
        print(datetime.strftime(n,"%d/%m/%Y"))
    separador()

if __name__ == "__main__":
    ruta_compras = "T13_Gastos\data\compras.csv"
    datos_compras = lee_compras(ruta_compras)
    provincia = "Huelva"
    supermercado = "Aldi"
    limite = 5

    # test_lee_compras(datos_compras)
    # test_compra_maxima_minima_provincia(datos_compras,provincia)
    # test_hora_menos_afluencia(datos_compras)
    # test_supermercados_mas_facturacion(datos_compras,limite)
    # test_clientes_itinerantes(datos_compras,limite)
    test_dias_estrella(datos_compras,provincia,supermercado)
    