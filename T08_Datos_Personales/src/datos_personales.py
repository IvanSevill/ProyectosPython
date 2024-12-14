from collections import namedtuple
Persona=namedtuple('persona', 'dni, nombre, apellidos, edad, localidad, provincia')

def filtra_por_edad(personas:list[Persona],edad:int)->list[Persona]:
    res = list()
    for persona in personas:
        if persona.edad<edad:
            res.append(persona)
    return res

def obtiene_dni_nombres(personas:list[Persona])->list:
    res = []
    for p in personas:
        res.append((p.nombre,p.apellidos,p.dni))
    return res

def obtiene_numero_edades_distintas(personas:list[Persona]):
    res = set()
    for n in personas:
        res.add(n.edad)
    return len(res)

def calcula_suma_edades(personas:list[Persona])->int:
    contador = 0
    for n in personas:
        contador += n.edad
    return contador

def calcula_promedio_edades(personas:list[Persona],prov:str='SEVILLA')->float:
    res = None
    suma=0
    contador = 0
    for p in personas:
        if p.provincia == prov:
            suma+=p.edad
            contador +=1
    if contador>0:
        res = suma/contador
    return res
