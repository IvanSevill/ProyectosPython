from datetime import date, time, datetime
from collections import namedtuple
import csv

Consumo = namedtuple('Consumo','fecha, id, tipo_edificio, edificio, barrio, clase, grupo, unidad, consumo')

def lee_consumos(ruta:str)->list[Consumo]:
    res = []
    with open (ruta,'rt', encoding='utf-8') as f:
        lector = csv.reader(f,delimiter=';')
        next(lector)
        #AÑO";"MES";"ID";"TIPOEDIFICIO";"EDIFICIO";"BARRIO";"CLASE";"GRUPO";"UNIDADES";"CONSUMO"
        for año, mes, id, tipo_edificio, edificio, barrio, clase, grupo, unidad, consumo in lector:
            fecha = date(int(año),int(mes),1)
            consumo = parsea_consumo(consumo)
            res.append(Consumo(fecha, id, tipo_edificio, edificio, barrio, clase, grupo, unidad, consumo))
    return res

def parsea_consumo(consumo:str):
    if consumo == '' or consumo == 'NO DATA':
        consumo = None
    else:
        consumo = float(consumo.replace(',','.'))
    return consumo

def barrios_top_consumo(lista:list[Consumo],año:int,clase:str,entero:int=3)->list:
    dic_aux = dict()
    for n in lista:
        if año == n.fecha.year and clase.upper() == n.clase.upper():
            if n.barrio not in dic_aux:
                # Inicializamos el diccionario como una lista con 12 ceros
                dic_aux[n.barrio] = [0 for n in range(1,13)]
            if n.consumo != None:
                # En caso de que quede algún cero en la lista lo quita, en el caso contrario simplemente añade el nuevo dato de consumo
                if 0 in dic_aux[n.barrio]:       
                    dic_aux[n.barrio].remove(0)
                dic_aux[n.barrio].append(n.consumo)

    res = dict()
    for c,v in dic_aux.items():
        res[c] = sum(v)/12
    return sorted(res.items(),key=lambda e:e[1],reverse=True)[:entero]

def media_consumo_edificios(lista:list[Consumo],clase:str)->float:
    dic_aux = dict()
    for n in lista:
        if clase.upper() == n.clase.upper() and n.consumo is not None:
            if n.id not in dic_aux:
                dic_aux[n.id] = list()
            dic_aux[n.id].append(n.consumo)
    
    res = dict()
    for c,v in dic_aux.items():
        res[c] = sum(v)

    if len(res) == 0:
        sol = 0
    else:
        sol = sum(res.values())/len(res)
    
    return sol
    
def media_consumos_de_edificio_por_tipo_edificio(lista:list[Consumo],año:int,clase:str)->dict:
    dic_aux = dict()
    for n in lista:
        if clase.upper() == n.clase.upper() and año == n.fecha.year:
            if n.tipo_edificio not in dic_aux:
                dic_aux[n.tipo_edificio] = list()
            dic_aux[n.tipo_edificio].append(n)
    
    res = dict()
    for c,v in dic_aux.items():
        res[c] = media_consumo_edificios(v,clase)
    return res

def incremento_anual_de_consumo_por_unidad(lista:list[Consumo],unidad:str)->list:
    unidad = unidad.upper()
    dic_aux = dict()
    for n in lista:
        if unidad == n.unidad.upper() and n.consumo != None:
            if n.fecha.year not in dic_aux:
                dic_aux[n.fecha.year] = 0
            dic_aux[n.fecha.year] += n.consumo

    lista_diferencias = []
    for anterior,actual in zip(list(dic_aux.items()),list(dic_aux.items())[1:]):
        variacion = (actual[1]-anterior[1])/anterior[1]*100
        lista_diferencias.append(((str(actual[0])+"-"+str(anterior[0])),variacion))

    return lista_diferencias