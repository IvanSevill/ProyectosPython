from datetime import date, time, datetime
from typing import List, Set, Tuple, Counter
from collections import namedtuple
import csv

Carrera = namedtuple("carrera","nombre,escuderia,fecha_carrera,temperatura_min,vel_max,duracion,posicion_final,ciudad, top_6_vueltas,tiempo_boxes,nivel_liquido")

def lee_carreras(ruta:str)->List[Carrera]:
    res = []
    with open(ruta,'rt',encoding='utf-8') as f:
        lector = csv.reader(f,delimiter=';')
        next(lector)
        for nombre,escuderia,fecha_carrera,temperatura_min,vel_max,duracion,posicion_final,ciudad, top_6_vueltas,tiempo_boxes,nivel_liquido in lector:
            fecha_carrera = datetime.strptime(fecha_carrera,'%d-%m-%y').date()
            temperatura_min = int(temperatura_min)
            vel_max = float(vel_max)
            duracion = float(duracion)
            posicion_final = int(posicion_final)
            top_6_vueltas = parea_vueltas(top_6_vueltas)
            tiempo_boxes = float(tiempo_boxes)
            nivel_liquido = (nivel_liquido == '1')
            res.append(Carrera(nombre,escuderia,fecha_carrera,temperatura_min,vel_max,duracion,posicion_final,ciudad, top_6_vueltas,tiempo_boxes,nivel_liquido))
    return res

def parea_vueltas(nombre_lista:str)->list:
    res = []
    for n in nombre_lista.replace('[','').replace(']','').split('/ '):
        if n == "-":
            res.append(0)
        else:
            res.append(float(n))
    return res

def media_tiempo_boxes(lista:List[Carrera],ciudad:str,fecha:datetime=None)->float:
    res = []
    for n in lista:
        if ciudad == n.ciudad and (fecha == None or fecha == n.fecha_carrera):
            res.append(n.tiempo_boxes)

    return sum(res)/len(res)

def pilotos_menor_tiempo_medio_vueltas_top(lista:List[Carrera],n:int)->List[Tuple[str,datetime]]:
    res = []
    for i in lista:
        cero = {0}
        if not cero.issubset(i.top_6_vueltas):
            res.append(((i.nombre,i.fecha_carrera),sum(i.top_6_vueltas)/len(i.top_6_vueltas)))
    return sorted([e[0] for e in res],key=lambda e:e[1])[:n]

def ratio_tiempo_boxes_total(lista:List[Carrera])->List[Tuple[str,datetime,float]]:
    dic_aux = dict()
    for n in lista:
        if n.fecha_carrera not in dic_aux:
            dic_aux[n.fecha_carrera] = list()
        dic_aux[n.fecha_carrera].append(n.tiempo_boxes)
    
    dic_medias_boxes = dict()
    for c,v in dic_aux.items():
        dic_medias_boxes[c] = sum(v)
    
    res = []
    for n in lista:
        res.append((n.nombre,n.fecha_carrera,n.tiempo_boxes/dic_medias_boxes[n.fecha_carrera]))
    return sorted(res,key=lambda e:e[2],reverse=True)

def puntos_piloto_anyos(lista:List[Carrera])->dict:
    dic_aux = dict()
    for n in lista:
        if n.nombre not in dic_aux:
            dic_aux[n.nombre] = list()
        dic_aux[n.nombre].append(puntos_carrera(n.posicion_final))
    return dic_aux

def puntos_carrera(posicion:int)->int:
    if posicion == 1:
        res = 50
    elif posicion == 2:
        res = 25
    elif posicion == 3:
        res = 10
    else:
        res = 0
    return res

def puntos_piloto_anyos(lista:List[Carrera])->dict:
    dic_aux = dict()
    for e in lista:
        año = e.fecha_carrera.year
        if e.nombre not in dic_aux:
            dic_aux[e.nombre] = dict()
        if año not in dic_aux[e.nombre]:
            dic_aux[e.nombre][año] = 0
        dic_aux[e.nombre][año] += puntos_carrera(e.posicion_final)

    res = dict()
    for c,v in dic_aux.items():
        res[c] = [e[1] for e in v.items()]

    return res

def mejor_escuderia_anyo(lista:List[Carrera],año:int):
    lista_victorias_año = list()
    for n in lista:
        if n.fecha_carrera.year == año and n.posicion_final == 1:
                lista_victorias_año.append(n.escuderia)
                
    cont = Counter(lista_victorias_año)
    return max(list(cont.items()),key=lambda e:e[1])[0]