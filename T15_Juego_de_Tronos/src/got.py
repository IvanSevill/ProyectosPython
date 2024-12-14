from typing import NamedTuple, List, Tuple
from parsers import *
import csv

BatallaGOT = NamedTuple('BatallaGOT',
    [('nombre', str), ('rey_atacante', str), ('rey_atacado', str), ('gana_atacante', bool),
     ('muertes_principales', bool), ('comandantes_atacantes', List[str]), ('comandantes_atacados', List[str]),
     ('region', str), ('num_atacantes', int), ('num_atacados', int)])

# 1)
def lee_batallas(ruta:str)->List[BatallaGOT]:
    res = []
    with open(ruta,'rt',encoding='utf-8') as f:
        lector = csv.reader(f,delimiter=',')
        next(lector)

        for nombre, rey_atacante, rey_atacado, gana_atacante, muertes_principales, comandantes_atacantes, comandantes_atacados, region, num_atacantes, num_atacados in lector:
            gana_atacante = parsea_gana_atacante(gana_atacante)
            muertes_principales = parsea_muertes_principales(muertes_principales)
            comandantes_atacantes = comandantes_atacantes_y_comandantes_atacados(comandantes_atacantes)
            comandantes_atacados = comandantes_atacantes_y_comandantes_atacados(comandantes_atacados)
            num_atacantes = número_de_atacantes_y_atacados(num_atacantes)
            num_atacados = número_de_atacantes_y_atacados(num_atacados)
            res.append(BatallaGOT(nombre, rey_atacante, rey_atacado, gana_atacante, muertes_principales, comandantes_atacantes, comandantes_atacados, region, num_atacantes, num_atacados))
    return res

# 2)
def reyes_mayor_menor_ejercito(lista:List[BatallaGOT])->Tuple:
    dict_aux = dict()
    for n in lista:
        if n.rey_atacado not in dict_aux:
            dict_aux[n.rey_atacado] = 0
        if n.num_atacados != None:
            dict_aux[n.rey_atacado] += n.num_atacados
        if n.rey_atacante not in dict_aux:
            dict_aux[n.rey_atacante] = 0
        if n.num_atacantes != None:
            dict_aux[n.rey_atacante] += n.num_atacantes
        
    return sorted(dict_aux.items(),key=lambda e:e[1],reverse=True)

# 3)
def batallas_mas_comandantes(lista:List[BatallaGOT],regiones:List[str]=None,limite:int=None)->List[Tuple]:
    # Creo un diccionario auxiliar en el que a cada región va a corresponder un conjunto de comandantes (str).
    dic_aux = dict()
    for n in lista:
        if n.region in regiones:
            if n.nombre not in dic_aux:
                dic_aux[n.nombre] = set()

            for comandantes in n.comandantes_atacados:
                dic_aux[n.nombre].add(comandantes)
            for comandantes in n.comandantes_atacantes:
                dic_aux[n.nombre].add(comandantes)

    res = dict()
    for c,v in dic_aux.items():
        res[c]=len(v)
    return sorted(res.items(),key=lambda e:e[1],reverse=True)[:limite]

# 4)
def rey_mas_victorias(lista:List[BatallaGOT],rol:str="ambos")->str:
    dict_aux = dict()
    for n in lista:
        if rol == "atacante":
            if n.gana_atacante == True:
                if n.rey_atacante not in dict_aux:
                    dict_aux[n.rey_atacante] = list()
                dict_aux[n.rey_atacante].append(1)
        if rol == "defensor":
            if n.gana_atacante == False:
                if n.rey_atacado not in dict_aux:
                    dict_aux[n.rey_atacado] = list()
                dict_aux[n.rey_atacado].append(1)
        if rol == "ambos":
            if n.gana_atacante == True:
                if n.rey_atacante not in dict_aux:
                    dict_aux[n.rey_atacante] = list()
                dict_aux[n.rey_atacante].append(1)
                if n.rey_atacado not in dict_aux:
                    dict_aux[n.rey_atacado] = list()
                dict_aux[n.rey_atacado].append(0)
            else:
                if n.rey_atacante not in dict_aux:
                    dict_aux[n.rey_atacante] = list()
                dict_aux[n.rey_atacante].append(0)

                if n.rey_atacado not in dict_aux:
                    dict_aux[n.rey_atacado] = list()
                dict_aux[n.rey_atacado].append(1)

    dict_aux_2 = dict()
    for c,v in dict_aux.items():
        dict_aux_2[c] = sum(v)

    if not dict_aux_2:  # Si el diccionario está vacío
        return None
    else:
        res = max(dict_aux_2.items(), key=lambda e: e[1])[0]
        return res

# 5)
def rey_mas_victorias_por_region(lista:List[BatallaGOT],rol:str="ambos"):
    dic_aux = dict()
    for n in lista:
        # Consideramos todas las opciones de "rol", siendo en caso nulo igual a "ambos".
        if rol == "atacante":
        # Si el atacante ganó la pelea y no está en el diccionario, añadelo como clave inicianizandolo como una lista y sumale a la lista su nombre,
        # en el caso de que exista simplemente añade el nombre a la lista de la región correspondiente.
            if n.gana_atacante:
                if n.region not in dic_aux:
                    dic_aux[n.region] = list()
                dic_aux[n.region].append(n.rey_atacante)

        if rol == "defensor":
        # Si el defensor ganó la pelea y no está en el diccionario, añadelo como clave inicianizandolo como una lista y sumale a la lista su nombre,
        # en el caso de que exista simplemente añade el nombre a la lista de la región correspondiente.
            if n.gana_atacante == False:
                if n.region not in dic_aux:
                    dic_aux[n.region] = list()
                dic_aux[n.region].append(n.rey_atacado)

        if rol == "ambos":
        # Mismo caso anterior pero en el caso de que "gana atacante" no sea True, suma a la lista de la región el rey atacado.
            if n.gana_atacante:
                if n.region not in dic_aux:
                    dic_aux[n.region] = list()
                dic_aux[n.region].append(n.rey_atacante)
            else:
                if n.region not in dic_aux:
                    dic_aux[n.region] = list()
                dic_aux[n.region].append(n.rey_atacado)

    res = dict()
    for c,v in dic_aux.items():
    # A cada región que funciona como clave le hago asignar el valor que más se repite en la lista con la función "maximo_lista"
        res[c] = maximo_lista(v)
    return res.items()

def maximo_lista(lista:list)->str:
    aux = dict()
    for n in lista:
    # Si no está como clave el rey ganador la inicializa en 0 y luego suma 1 a cada vez que aparezca 
        if n not in aux:
            aux[n] = 0
        aux[n] += 1
    # Devuelve el nombre del rey que más aparezca pero sin el número de veces, en tal caso quitaríamos el [0].
    return max(aux.items(),key=lambda e:e[1])[0]
