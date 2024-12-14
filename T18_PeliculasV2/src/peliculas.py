from datetime import date, time, datetime
from typing import List, Counter, Set, Tuple
from collections import namedtuple
import csv

Pelicula  =  namedtuple("pelicula",  "fecha_estreno,  titulo,  director,  generos,  duracion, presupuesto, recaudacion, reparto")

def lee_peliculas(ruta:str)->List[Pelicula]:
    res = []
    with open(ruta,'rt',encoding='utf-8') as f:
        lector = csv.reader(f,delimiter=';')
        next(lector)
        for fecha_estreno,título,director,género,duración,presupuesto,recaudación,reparto in lector:
            fecha_estreno = datetime.strptime(fecha_estreno,"%d/%m/%Y").date()
            género = género.split(', ')
            duración = int(duración)
            presupuesto = int(presupuesto)
            recaudación = int(recaudación)
            reparto = reparto.split(', ')
            res.append(Pelicula(fecha_estreno,título,director,género,duración,presupuesto,recaudación,reparto))
    return res

def pelicula_mas_ganancias(lista:List[Pelicula],genero:str=None)->str:
    res = []
    for n in lista:
        if genero == None or genero in n.generos:
            res.append((n.titulo,n.recaudacion - n.presupuesto))
    return max(res,key=lambda e:e[1])

def media_presupuesto_por_genero(lista:List[Pelicula])->dict:
    dic_aux = dict()
    for n in lista:
        for i in n.generos:
            if i not in dic_aux:
                dic_aux[i] = [] 
            dic_aux[i].append(n.presupuesto)
    
    res = dict()
    for c,v in dic_aux.items():
        res[c] = sum(v)/len(v)

    return res

def peliculas_por_actor(lista:List[Pelicula],año_inicial:datetime=None,año_final:datetime=None)->dict:
    dic_aux = dict()
    for n in lista:
        if (año_inicial == None or año_inicial <= n.fecha_estreno) and (año_final == None or año_final >= n.fecha_estreno):
            for i in n.reparto:
                if i not in dic_aux:
                    dic_aux[i] = 0
                dic_aux[i] += 1
    
    return dic_aux


def actores_mas_frecuentes(lista:List[Pelicula],entero:int,año_inicial:datetime=None,año_final:datetime=None)->List:
    peliculas_actor = peliculas_por_actor(lista,año_inicial,año_final)
    lista_peliculas_actor = sorted(peliculas_actor.items(),key=lambda e:e[1],reverse=True)
    res = [c for c,v in lista_peliculas_actor]
    return res[:entero]

def recaudacion_total_por_año(lista:List[Pelicula],generos:set=None)->dict:
    dic_aux = dict()
    for n in lista:
        if generos == None or len(set(n.generos) & generos) > 0:
                if n.fecha_estreno.year not in dic_aux:
                    dic_aux[n.fecha_estreno.year] = 0
                dic_aux[n.fecha_estreno.year] += n.recaudacion
    return dic_aux

def incrementos_recaudacion_por_año(lista:List[Pelicula],generos:set=None)->List[int]:
    res = []
    lista_años = sorted(recaudacion_total_por_año(lista,generos).items(),key=lambda e:e[0])
    res  = [actual[1] - anterior[1] for anterior,actual in zip(lista_años[0:],lista_años[1:])]
    return res 