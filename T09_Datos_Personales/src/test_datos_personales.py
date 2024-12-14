from datos_personales import * 

def test_lee_datos_personales(personas:list[Persona]):
    print("\nNúmero de registros leídos:",len(personas))
    print("\nEl tercer registro es:",personas[2])
    print("\nLos tres primeros registros son:",personas[:2])
    print("\nLos tres últimos registros son:",personas[-3:])
    print("-"*100)

def test_lee_datos_personales2(personas:list[Persona2]):
    print("\nNúmero de registros leídos:",len(personas))
    print("\nEl tercer registro es:", personas[2])
    print("\nLos tres primeros registros son:",personas[:2])
    print("\nLos tres últimos registros son:",personas[-3:])
    print("-"*100)

def test_lee_datos_personales3(personas:list[Persona3]):
    print("\nNúmero de registros leídos:",len(personas))
    print("\nEl tercer registro es:", personas[2])
    print("\nLos tres primeros registros son:",personas[:2])
    print("\nLos tres ultimos registros son:",personas[-3:])
    print("-"*100)
    
def test_lee_datos_personales4(personas:list[Persona4]):
    print("Número de registros leídos:",len(personas))
    print("\nEl tercer registro es:", personas[2])
    print("\nLos tres primeros registros son:",personas[:2])
    print("\nLos tres ultimos registros son:",personas[-3:])
    print("-"*100)

def test_compruebe_años_hora(personas:list[Persona4]):
    año1 = int(input("Introduzca el año inicial: "))
    año2 = int(input("Introduzca el año final: "))
    print("¿Están todas las personas entre {} y {}?".format(año1,año2))
    print(todos_entran_entre_años(personas,año1,año2))
    hora = int(input("Introduzla la hora inicial: "))    
    print("¿Alguno ha madrugado antes de las {}?".format(hora))
    print(alguien_ha_madrugado(personas,hora))

def test_persona_mas_alta(personas:list[Persona4]):
    print(f'La persona más alta es {persona_mas_alta(personas)}')

def test_relacion_alfabetica_personas(personas:list[Persona4]):
    personas = relacion_alfabetica_personas(personas)
    print("\nLista de las personas ordenadas por apellido alfabéticamente y su edad")
    
    # for n in personas:
    #     print("{:25s} {:<15s} {}".format(n[0],n[1],n[2]))

    for n in personas:
        print(n)

def test_n_personas_mayor_edad(personas:list[Persona4]):
    personas = relacion_alfabetica_personas(personas)
    for n in personas:
        print(n)


if __name__ == '__main__':
    datos = lee_datos_personales("T09_Datos_Personales/data/datos_personales.csv")
    datos2 = lee_datos_personales2("T09_Datos_Personales/data/datos_personales2.csv")
    datos3 = lee_datos_personales3("T09_Datos_Personales/data/datos_personales3.csv")
    datos4 = lee_datos_personales4("T09_Datos_Personales/data/datos_personales4.csv")
    print("-"*100)
    # test_lee_datos_personales(datos)
    # test_lee_datos_personales2(datos2)
    # test_lee_datos_personales3(datos3)
    # test_lee_datos_personales4(datos4)
    # test_compruebe_años_hora(datos4)
    # test_persona_mas_alta(datos4)
    # test_relacion_alfabetica_personas(datos4)
