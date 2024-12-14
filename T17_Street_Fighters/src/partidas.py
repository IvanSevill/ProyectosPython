from typing import NamedTuple, List, Set, Tuple, Counter
from datetime import date, time, datetime
import csv 

Partida = NamedTuple("Partida", [
    ("pj1", str),
    ("pj2", str),
    ("puntuacion", int),
    ("tiempo", float),
    ("fecha_hora", datetime),
    ("golpes_pj1", List[str]),
    ("golpes_pj2", List[str]),
    ("movimiento_final", str),
    ("combo_finish", bool),
    ("ganador", str),
    ])

def lee_partidas(ruta:str)->List[Partida]:
    res = []
    with open(ruta,'rt',encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=',')
        next(lector)
        for pj1,pj2,puntuacion,tiempo,fecha_hora,golpes_pj1,golpes_pj2,movimiento_final,combo_finish,ganador in lector:
            puntuacion = int(puntuacion)
            tiempo = float(tiempo)
            fecha_hora = datetime.strptime(fecha_hora,"%Y-%m-%d %H:%M:%S")
            golpes_pj1 = golpes_pj1.strip("[]").split(", ")
            golpes_pj2 = golpes_pj2.strip("[]").split(", ")
            combo_finish = (combo_finish == "1")
            res.append(Partida(pj1,pj2,puntuacion,tiempo,fecha_hora,golpes_pj1,golpes_pj2,movimiento_final,combo_finish,ganador))
    return res

def victoria_mas_rapida(lista:List[Partida])->Tuple[str,str,float]:
    anterior = (lista[0].pj1,lista[0].pj2,lista[0].tiempo)
    for n in lista:
        if anterior[2] > n.tiempo:
            anterior = (n.pj1,n.pj2,n.tiempo)
    return(anterior)

def top_ratio_medio_personajes(lista:List[Partida],entero:int)->List[str]:
    dic_aux = dict()
    for n in lista:
        if n.ganador == n.pj1:
            if n.pj1 not in dic_aux:
                dic_aux[n.pj1] = list()
            dic_aux[n.pj1].append(n.puntuacion/n.tiempo)

        if n.ganador == n.pj2:
            if n.pj1 not in dic_aux:
                dic_aux[n.pj2] = list()
            dic_aux[n.pj2].append(n.puntuacion/n.tiempo)

    res = dict()
    for c,v in dic_aux.items():
        res[c] = sum(v)/len(v)

    return [n[0] for n in sorted(res.items(),key = lambda e:e[1])[:entero]]

def enemigos_mas_debiles(lista:List[Partida],personaje:str)->Tuple[List[str],int]:
    list_aux = list()
    for n in lista:
        if n.ganador == personaje:
            if personaje == n.pj1:
                list_aux.append(n.pj2)
            if personaje == n.pj2:
                list_aux.append(n.pj1)

    cont = Counter(list_aux)
    res = dict()
    for c,v in cont.items():
        if v not in res:
            res[v]=[]
        res[v].append(c)
    resultado = max(list(res.items()),key=lambda e:e[1])

    return (resultado[1],resultado[0])

def movimientos_comunes(lista:List[Partida],personaje1:str,personaje2:str)->Set[str]:
    mov1 = set()
    mov2 = set()
    for n in lista:
        if n.pj1 == personaje1:
            for mov in n.golpes_pj1:
                mov1.add(mov)

        if n.pj2 == personaje1:
            for mov in n.golpes_pj2:
                mov1.add(mov)
        
        if n.pj1 == personaje2:
            for mov in n.golpes_pj1:
                mov2.add(mov)

        if n.pj2 == personaje2:
            for mov in n.golpes_pj2:
                mov2.add(mov)            
                
    res = mov1 & mov2
    return res

def dias_mas_combos_finish(lista:List[Partida])->str:
    dic_aux = dict()
    for n in lista:
        if n.combo_finish:
            if n.fecha_hora.weekday() not in dic_aux:
                dic_aux[n.fecha_hora.weekday()] = 0
            dic_aux[n.fecha_hora.weekday()] += 1

    dic_ord = max(dic_aux.items(),key=lambda e:e[1])[0]
    semana = ["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
    return semana[dic_ord]
