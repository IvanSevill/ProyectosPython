from collections import namedtuple
from datetime import date, time, datetime
from typing import Counter
import csv

Entreno = namedtuple("Entreno", "tipo,fechahora,ubicacion,duracion,calorias,distancia,frecuencia,compartido")

def lee_entrenos(ruta:str)->list[Entreno]:
    res = list()
    with open(ruta,'rt',encoding='utf-8') as f:
        lector =csv.reader(f,delimiter=',')
        next(lector)
        for tipo,fechahora,ubicacion,duracion,calorias,distancia,frecuencia,compartido in lector:
            fechahora = datetime.strptime(fechahora,'%d/%m/%Y %H:%M')
            duracion = int(duracion)
            calorias = int(calorias)
            distancia = float(distancia)
            frecuencia = int(frecuencia)
            compartido = (compartido == 'S')
            res.append(Entreno(tipo,fechahora,ubicacion,duracion,calorias,distancia,frecuencia,compartido))
    return res

def porcentaje_calorias_por_tipo(lista:list[Entreno],conj_entrenos:set)->dict:
    dic_aux = dict()
    suma_calorias = 0
    for n in lista:
        if n.tipo in conj_entrenos:
            if n.tipo not in dic_aux:
                dic_aux[n.tipo] = list()
            dic_aux[n.tipo].append(n.calorias)
        suma_calorias += n.calorias

    res = dict()
    for c,v in dic_aux.items():
        res[c] = sum(v)/suma_calorias*100
    return res

def año_mayor_distancia_media(lista:list[Entreno],d:int,c:bool=None)->int:
    dic_aux = dict()
    for n in lista:
        if c == None or  c == n.compartido:
            if n.distancia > d:
                if n.fechahora.year not in dic_aux:
                    dic_aux[n.fechahora.year] = list()
                dic_aux[n.fechahora.year].append(n.distancia)

    res = dict()
    for c,v in dic_aux.items():
        res[c] = sum(v)/len(v)
    return max(res.items(),key=lambda e:e[1])[0]

def entrenos_mas_repetidos(lista:list[Entreno],f1:date,f2:date)->dict:
    dic_aux = dict()
    for n in lista:
        if n.fechahora.date() >= f1 and n.fechahora.date() <=f2:
            if n.ubicacion not in dic_aux:
                dic_aux[n.ubicacion] = list()
            dic_aux[n.ubicacion].append(n.tipo)
    
    res = dict()
    for c,v in dic_aux.items():
        res[c] = max(Counter(v).items(),key=lambda e:e[1])[0]

    return res

def incrementos_anuales_distancia(lista:list[Entreno])->list:
    dic_aux = dict()
    for n in lista:
        if n.fechahora.year not in dic_aux:
            dic_aux[n.fechahora.year] = 0
        dic_aux[n.fechahora.year] += n.distancia
    
    lista_distancia_años = [v[1] for v in sorted(list(dic_aux.items()),key=lambda e:e[0])]
    return [anterior-actual for actual, anterior in zip(lista_distancia_años,lista_distancia_años[1:])]
