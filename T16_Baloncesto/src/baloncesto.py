from typing import NamedTuple, Tuple, List, Set, Counter
from datetime import date, time, datetime
import csv

Equipo = NamedTuple("Equipo",
    [("nombre", str),
     ("puntos", int),
     ("faltas", int)
    ]
)

PartidoBasket = NamedTuple(
    "PartidoBasket",
    [("fecha", date), 
     ("competicion", str), 
     ("equipo1", Equipo), 
     ("equipo2", Equipo)
    ]
)

def parsea_y_suma_resultados(resultados:str)->(int,int):
    eq1 = []
    eq2 = [] 
    for partido in resultados.split("*"):
        eq1.append(int(partido.split("-")[0]))
        eq2.append(int(partido.split("-")[1]))
    return (sum(eq1),sum(eq2))

def lee_partidos(ruta:str)->List[PartidoBasket]:
    res = []
    with open(ruta,'rt',encoding='utf-8') as f:
        lector = csv.reader(f,delimiter=';')
        next(lector)
        for fecha,equipo_1,equipo_2,torneo,cuartos,faltas_1,faltas_2 in lector:
            fecha = datetime.strptime(fecha,"%d/%m/%Y").date()
            competicion = torneo
            resultado = parsea_y_suma_resultados(cuartos)
            equipo1 = Equipo(equipo_1,resultado[0],int(faltas_1))
            equipo2 = Equipo(equipo_2,resultado[1],int(faltas_2))
            res.append(PartidoBasket(fecha,competicion,equipo1,equipo2))
    return res

def equipo_con_mas_faltas(lista:List[PartidoBasket],conjunto:Set[str]=None)->(str,str):
    dic_aux = dict()
    for n in lista:

        if conjunto == None or n.equipo1.nombre in conjunto:
            if n.equipo1.nombre not in dic_aux:
                dic_aux[n.equipo1.nombre] = 0
            dic_aux[n.equipo1.nombre] += n.equipo1.faltas

        if conjunto == None or n.equipo2.nombre in conjunto:
            if n.equipo2.nombre not in dic_aux:
                dic_aux[n.equipo2.nombre] = 0
            dic_aux[n.equipo2.nombre] += n.equipo2.faltas

    return max(list(dic_aux.items()),key=lambda e:e[1])

def media_puntos_por_equipo(lista:List[PartidoBasket],competicion:str)->dict:
    res = dict()
    for n in lista:
        if n.competicion == competicion:

            if n.equipo1.nombre not in res:
                res[n.equipo1.nombre] = []
            res[n.equipo1.nombre].append(n.equipo1.puntos)

            if n.equipo2.nombre not in res:
                res[n.equipo2.nombre] = []
            res[n.equipo2.nombre].append(n.equipo2.puntos)
    
    res2 = dict()
    for c,v in res.items():
        res2[c] = sum(v)/len(v)
    return res2

def diferencia_puntos_anotados(lista:List[PartidoBasket],equipo:str)->List[int]:
    res = []
    for n in sorted(lista,key=lambda e: e.fecha):
        if equipo == n.equipo1.nombre:
            res.append(n.equipo1.puntos)
        if equipo == n.equipo2.nombre:
            res.append(n.equipo2.puntos)
    res2 = []
    for anterior,actual in zip(res,res[1:]):
        res2.append(actual-anterior)
    return res2

def victorias_por_equipo(lista:List[PartidoBasket])->dict:
    list_aux = []
    for n in lista:
        if n.equipo1.puntos > n.equipo2.puntos:
            list_aux.append(n.equipo1.nombre)

        if n.equipo1.puntos < n.equipo2.puntos:
            list_aux.append(n.equipo2.nombre)

    res = Counter(list_aux)
    return res

def equipo_minimo_victorias(lista:List[PartidoBasket],entero:int)->List[str]:
    res = []
    dic_victorias = victorias_por_equipo(lista)
    
    for equipo,victorias in sorted(dic_victorias.items(),key=lambda e:e[1],reverse=True):
        if victorias >= entero:
            res.append(equipo)
    return res 

def equipos_mas_victorias_por_año(lista:List[PartidoBasket],entero:int)->dict:
    dic_aux = dict()

    # En primer lugar creo un diccionario en el que los separo por cada año y como valores el resto de tuplas del tipo PartidoBasket.
    for n in lista:
        if n.fecha.year not in dic_aux:
            dic_aux[n.fecha.year] = []
        dic_aux[n.fecha.year].append(n)

    # Recorro el diccionario anterior pero esta vez quedandome con los ganadores por año.
    dic_por_años = dict()
    ganadores_por_año = list()
    for c,v in dic_aux.items():
        if c not in dic_por_años:
            dic_por_años[c] = []

        # Recorro los elementos de la lista de cada año y me quedo con los ganadores.
        for partido in v:
            if partido.equipo1.puntos > partido.equipo2.puntos:
                ganadores_por_año.append(partido.equipo1.nombre)
            if partido.equipo1.puntos < partido.equipo2.puntos:
                ganadores_por_año.append(partido.equipo2.nombre)

        # Uso el método Counter para contar el número de veces que gana cada equipo para porsteriormente quedarme tan solo con los que superan el entero dado.
        dic_por_años[c] = sorted(Counter(ganadores_por_año).items(),key = lambda e:e[1], reverse = True)
        ganadores_por_año.clear()

    # Por años compruebo los valores y, en caso de que superen el umbral mínimo, los añado a la lista que se mostrará finalmente.
    res = dict()
    for c,v in dic_por_años.items():
        lista_cribada = list()
        for equipo, victorias in v:
            if victorias >= entero:
                lista_cribada.append(equipo)
        res[c] = lista_cribada
    return res