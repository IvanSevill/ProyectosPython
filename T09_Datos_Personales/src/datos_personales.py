from collections import namedtuple
import csv
from datetime import datetime, date, time

Persona=namedtuple('persona', 'dni, nombre, apellidos, edad, estatura, peso, localidad, provincia')
Persona2=namedtuple('persona', 'dni, nombre, apellidos, edad, estatura, peso, localidad, provincia, esmujer')
Persona3=namedtuple('persona', 'dni, nombre, apellidos, edad, estatura, peso, localidad, provincia, esmujer, hobbies')
Persona4=namedtuple('persona', 'dni, nombre, apellidos, edad, estatura, peso, localidad, provincia, esmujer, hobbies, fecha, hora')
 
# Ejercicio 1 del día 03/10
def lee_datos_personales(ruta:str)->list[Persona]:
    res = list()
    with open(ruta,'rt',encoding='utf-8') as f:
        lector = csv.reader(f,delimiter=';')
        next(lector)
        for r in lector:
            tupla = Persona(r[0], r[1], r[2], int(r[3]), float(r[4]), float(r[5]), r[6], r[7])
            res.append(tupla)
    return res

# Ejercicio 2 del día 03/10
def esmujer(entrada:str)->bool:
    if entrada == "SI":
        entrada = True
    else:
        entrada = False
    return entrada

def lee_datos_personales2(ruta:str)->list[Persona2]:
    res = list()
    with open(ruta,'rt',encoding='utf-8') as f:
        lector = csv.reader(f,delimiter=';')
        next(lector)
        for r in lector:
            tupla = Persona2(r[0], r[1], r[2], int(r[3]), float(r[4]), float(r[5].replace(",",".")), r[6], r[7], esmujer(r[8]))
            res.append(tupla)
    return res

# Ejercicio 3 del día 05/10
def parsea_hobbies(cadena:str)->list[str]:
    res = list()
    for elemento in cadena.split("/"):
        res.append(elemento)
    return res

def ponme_en_ruta():
    import os
    ruta=os.path.abspath(__file__) 
    posición=ruta.index("src") 
    os.chdir(ruta[:posición]+"data\\")

def lee_datos_personales3(ruta:str)->list[Persona3]:
    res = list()
    with open(ruta,'rt',encoding='utf-8') as f:
        lector = csv.reader(f,delimiter=';')
        next(lector)
        for r in lector:
            tupla = Persona3(r[0], r[1], r[2], int(r[3]), float(r[4]), float(r[5].replace(",",".")), r[6], r[7], esmujer(r[8]), parsea_hobbies(r[9]))
            res.append(tupla)
    return res

# Ejercicio 4 del día 10/10
def separa_fecha_hora(entrada:str)->tuple:
    res = []
    for n in entrada.split("#"):
        res.append(n)

    date_format = "%d/%m/%Y"
    time_format = "%H:%M:%S"
    res[0] = datetime.strptime(res[0],date_format).date()
    res[1] = datetime.strptime(res[1],time_format).time()
    return res

def lee_datos_personales4(ruta:str)->list[Persona4]:
    res = list()
    with open(ruta,'rt',encoding='utf-8') as f:
        lector = csv.reader(f,delimiter=';')
        next(lector)
        for r in lector:
            L10 = separa_fecha_hora(r[10])
            tupla = Persona4(r[0], r[1], r[2], int(r[3]), float(r[4]), float(r[5].replace(",",".")), 
                             r[6], r[7], esmujer(r[8]), parsea_hobbies(r[9]),L10[0],L10[1])
            res.append(tupla)
    return res

def todos_entran_entre_años(lista:list[Persona],año1:int,año2:int)->bool:
    res = True
    for n in lista:
        if n.fecha.year <= año1 or n.fecha.year >= año2:
            res = False
            break
    return res

def alguien_ha_madrugado(lista:list[Persona],hora:int)->bool:
    res = False
    for n in lista:
        if n.hora.hour < hora:
            res = True
            break
    return res

# Día 24/10
def persona_mas_alta(lista:list[Persona4]):
    lista_ordenada = list()
    lista_ordenada = sorted(lista,key=lambda e:e[4],reverse=True)
    return (lista_ordenada[0][1], lista_ordenada[0][2], lista_ordenada[0][4])

def relacion_alfabetica_personas(lista:list[Persona4])->list:
    lista_ordenada = []
    res = []
    lista_ordenada = sorted(lista,key=lambda e:e[2])
    for n in lista_ordenada:
        res.append((n.apellidos,n.nombre,n.edad))
    return res

def n_personas_mayor_edad(lista:list[Persona4],n:int)->list[tuple]:
    res = list()
    for p in sorted(lista, key=lambda e:e.edad,reverse=True)[:n]:
        res.append((p.edad,p.dni,p.peso,p.estatura))
    return res


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