from datetime import datetime,date,time
from typing import NamedTuple, Tuple, List, Set 
import csv 

Videos = NamedTuple("videos",
    [("id", str),
     ("fecha_trending", datetime),
     ("titulo", str),
     ("canal", str),
     ("categoria", str),
     ("visitas", int),
     ("likes", int),
     ("dislikes", int)]
)


def lee_trending_videos(ruta:str)->List[Videos]:
    res = []
    with open(ruta,'rt',encoding='utf-8') as f:
        lector = csv.reader(f,delimiter=';')
        next(lector)
        for id,fecha_trending,titulo,canal,categoria,visitas,likes,dislikes in lector:
            fecha_trending = datetime.strptime(fecha_trending,'%d/%m/%Y').date()
            visitas = int(visitas)
            likes = int(likes)
            dislikes = int(dislikes)
            res.append(Videos(id,fecha_trending,titulo,canal,categoria,visitas,likes,dislikes))
    return res

def media_visitas(lista:List[Videos],fecha):
    res = []
    for n in lista:
        if n.fecha_trending == fecha:
            res.append(n.visitas)

    if len(res) > 0:
        val = sum(res)/len(res)
    else:
        val = 0
    return val

def video_mayor_ratio_likes_dislikes(lista:List[Videos],categoria:str=None)->Videos:
    res = []
    for n in lista:
        if n.dislikes > 0 and (categoria == None or n.categoria == categoria):
                res.append((n,n.likes/n.dislikes))
    
    return max(res,key=lambda e:e[1])

def canales_top(lista:List[Videos],entero:int=3)->List:
    dic_aux = dict()
    for n in lista:
        if n.canal not in dic_aux:
            dic_aux[n.canal] = 0
        dic_aux[n.canal] += 1

    return sorted(dic_aux.items(),key=lambda e:e[1],reverse=True)[:entero]

def video_mas_likeability_por_categoria(lista:List[Videos],k:int=20)->List:
    dic_aux = dict()
    for n in lista:
        likeability = (k*n.likes-n.dislikes)/(k*n.visitas)
        if n.categoria not in dic_aux:
            dic_aux[n.categoria] = []
        dic_aux[n.categoria].append((n.id,likeability))
    
    res = dict()
    for c,v in dic_aux.items():
        res[c] = max(v,key= lambda e:e[1])[0]
    return list(res.items())

def incrementos_visitas(lista:List[Videos], canal)->List:
    dic_aux = dict()
    for n in lista:
        if n.fecha_trending not in dic_aux:
            dic_aux[n.fecha_trending] = 0
        if canal == n.canal:
            dic_aux[n.fecha_trending]+=n.visitas

    list_dic = list(dic_aux.items())
    lista_visitas = [v for c,v in list_dic]
    res = [actual-anterior for anterior,actual in zip(lista_visitas,lista_visitas[1:])]
    return res