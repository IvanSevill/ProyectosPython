from datos_personales import *
def carga_lista()->list[Persona]:
    personas = [Persona('12345678A','JUAN','AFAN POSTIGO',22,'SEVILLA','SEVILLA'),
                Persona('12345678B','NICOLAS','AGUILAR SAUCEDO',20,'DOS HERMANAS','SEVILLA'),
                Persona('12345678C','LUCAS','ACEJO GARCÍA',20,'UTRERA','SEVILLA'),
                Persona('12345678D','CLAUDIA','ÁLVAREZ GARCÍA',21,'VISO DEL ALCOR','SEVILLA'),
                Persona('12345678E','PAULA','ALBENDÍN CAMINO',19,'TOMARES','SEVILLA'),
                Persona('12345678F','ANA','LOBATO ÁLVAREZ',18,'PUNTA UMBRÍA','HUELVA'),
                Persona('12345678G','ANTONIO','DÍAZ NARANJO',18,'CHIPIONA','CADIZ'),
                Persona('12345678H','SOFÍA','GUERRERO CANTARERO',20,'CHIPIONA','CADIZ')]
    return personas

def test_filtra_por_edad(personas:list[Persona]):
    edad_limite = 21
    print("\nLos menores de",edad_limite,"son:")
    for p in filtra_por_edad(personas,edad_limite):
        print(p)

def test_obtiene_dni_nombres(personas:list[Persona]):
    print("\nLa vista con el nombre y el dni es:")
    for l in obtiene_dni_nombres(personas):
        print(l)

def test_obtiene_numero_edades_distintas(personas:list[Persona]):
    d = obtiene_numero_edades_distintas(personas)
    print("\nHay {} edades distintas que hay en la lista".format(d))

def test_calcula_suma_edades(personas:list[Persona]):
    n = calcula_suma_edades(personas)
    print("\nLa suma de edades es de {} años".format(n))

def test_calcula_promedio_edades(personas:list[Persona])->str:
    print("Edades de Jaén:",calcula_promedio_edades(personas,"JAÉN"))
    print("Edades de Cádiz:",calcula_promedio_edades(personas,"CADIZ"))
    print("Edades de ???:",calcula_promedio_edades(personas))

if __name__=='__main__':
    lista_personas = carga_lista()
    # test_filtra_por_edad(lista_personas)
    # test_obtiene_dni_nombres(lista_personas)
    # test_obtiene_numero_edades_distintas(lista_personas)
    # test_calcula_suma_edades(lista_personas)
    test_calcula_promedio_edades(lista_personas)