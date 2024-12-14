from typing import NamedTuple, List, Tuple
from datetime import date,time,datetime
import csv


Parcial = NamedTuple('Parcial', 
                [('juegos_j1',int),
                 ('juegos_j2',int)])
PartidoTenis = NamedTuple('PartidoTenis', 
                [('fecha',datetime.date), 
                 ('jugador1',str), 
                 ('jugador2',str), 
                 ('superficie',str), 
                 ('resultado', List[Parcial]), 
                 ('errores_nf1',int), 
                 ('errores_nf2',int)])
def cabecera(msg:str)->None:
    separador()
    print("--"*35,f"{msg}","--"*35)

def cabecera_ejercicio(numero:int)->None:
    print(f"\n==== Ejercicio {numero}","=="*73,"\n")

def separador()->None:
    print("\n","=="*81,"\n")

def lee_partidos_tenis(fichero:str)->List[PartidoTenis]:
    res = []
    with open(fichero,'rt',encoding='utf-8') as f:
        lector = csv.reader(f,delimiter=";")
        for fecha,jugador1, jugador2, superficie, parcial1, parcial2, parcial3, errores_nf1, errores_nf2 in lector:
            fecha = datetime.strptime(fecha, '%d/%m/%Y').date()
            resultado = [parsea_set(parcial1),parsea_set(parcial2),parsea_set(parcial3)]
            errores_nf1 = int(errores_nf1)
            errores_nf2 = int(errores_nf2)
            res.append(PartidoTenis(fecha,jugador1, jugador2, superficie, resultado, errores_nf1, errores_nf2))
    return res

def parsea_set(parcial:str)->list[Parcial]:
    parcial = parcial.split("-")
    res = Parcial(int(parcial[0]),int(parcial[1]))
    return res

# 2)
def partido_menos_errores(lista:List[PartidoTenis])->Tuple:
    res = []
    for n in lista:
        res.append((n,n.errores_nf1+n.errores_nf2))
    return min(res,key=lambda e:e[1])

# 3)
def jugador_mas_partidos(lista:List[PartidoTenis])->Tuple:
    dic = dict()
    for n in lista:
        jugadores_partido = [n.jugador1,n.jugador2]
        for n in jugadores_partido:
            if n not in dic:
                dic[n] = 0
            dic[n] += 1

    res = max(dic.items(),key=lambda e:e[1])
    return res

# 4)
def tenista_mas_victorias(lista:List[PartidoTenis],f_desde:datetime=None,f_hasta:datetime=None)->None:
    dic = dict()
    for n in lista:
        if (f_desde == None or n.fecha >= f_desde) and (f_hasta == None or n.fecha <= f_hasta):
            ganador_partido = ganador(n)
            if ganador_partido not in dic:
                dic[ganador_partido] = 0 
            dic[ganador_partido] += 1
    return max(list(dic.items()),key=lambda e:e[1])

def ganador(partido:PartidoTenis)->str:
    contador_1 = 0
    contador_2 = 0
    
    for n in partido.resultado:
        if n.juegos_j1 > n.juegos_j2:
            contador_1 += 1
        if n.juegos_j1 < n.juegos_j2:
            contador_2 += 1

    return partido.jugador1 if contador_1 > contador_2 else partido.jugador2

# 5)
def media_errores_por_jugador(lista:List[PartidoTenis])->List:
    dic_aux = dict()
    for n in lista:
        if n.jugador1 not in dic_aux:
            dic_aux[n.jugador1] = list()
        dic_aux[n.jugador1].append(n.errores_nf1)

        if n.jugador2 not in dic_aux:
            dic_aux[n.jugador2] = list()
        dic_aux[n.jugador2].append(n.errores_nf2)

    res = dict()
    for clave, valor in dic_aux.items():
        res[clave] = sum(valor)/len(valor)
    return sorted(res.items(),key= lambda e:e[1])

# 6)
def jugadores_mayor_porcentaje_victorias(lista:List[PartidoTenis]):
    dic_aux = dict()
    for n in lista:
        ganador_partido = ganador(n)
        if n.jugador1 not in dic_aux:
            dic_aux[n.jugador1] = list()
        if n.jugador2 not in dic_aux:
            dic_aux[n.jugador2] = list()

        if n.jugador1 == ganador_partido:
            dic_aux[n.jugador1].append(1)
            dic_aux[n.jugador2].append(0)
        else:
            dic_aux[n.jugador1].append(0)
            dic_aux[n.jugador2].append(1)

    res = dict()
    for clave,valor in dic_aux.items():
        res[clave] = sum(valor)/len(valor)

    return sorted(res.items(),key=lambda e:e[1],reverse=True)

# 7)
def n_tenistas_con_mas_errores(lista:List[PartidoTenis],parametro:int=None):
    dic_tenistas_errores = dict()
    for n in lista:
        if n.jugador1 not in dic_tenistas_errores:
            dic_tenistas_errores[n.jugador1] = 0
        dic_tenistas_errores[n.jugador1] += n.errores_nf1

        if n.jugador2 not in dic_tenistas_errores:
            dic_tenistas_errores[n.jugador2] = 0
        dic_tenistas_errores[n.jugador2] += n.errores_nf2
    
    res = sorted(dic_tenistas_errores.items(),key= lambda e:e[1],reverse=True)
    return res if parametro == None else res[:parametro]

# 8)
def fechas_ordenadas_por_jugador(lista:List[PartidoTenis])->dict:
    dic_aux = dict()
    for n in lista:
        if n.jugador1 not in dic_aux:
            dic_aux[n.jugador1] = list()
        dic_aux[n.jugador1].append(n.fecha)

        if n.jugador2 not in dic_aux:
            dic_aux[n.jugador2] = list()
        dic_aux[n.jugador2].append(n.fecha)
    return dic_aux

# 9)        
def num_partidos_nombre(lista:List[PartidoTenis],nombre:str)->dict:
    dic_aux = dict()
    for n in lista:
        if n.jugador1 == nombre or n.jugador2 == nombre:
            ganador_partido = ganador(n)
            if n.superficie not in dic_aux:
                dic_aux[n.superficie] = list()

            if nombre == ganador_partido:
                dic_aux[n.superficie].append(1)
            else:
                dic_aux[n.superficie].append(0)
    res = dict()
    for clave,valor in dic_aux.items():
        res[clave] = (len(valor),sum(valor))
    return res

# 10)
def num_tenistas_distintos_por_superficie(lista:List[PartidoTenis])->dict:
    dic_aux = dict()
    for n in lista:
        if n.superficie not in dic_aux:
            dic_aux[n.superficie] = set()
        dic_aux[n.superficie].add(n.jugador1)        
        dic_aux[n.superficie].add(n.jugador2)
    
    res = dict()
    for clave, valor in dic_aux.items():
        res[clave] = len(valor)
    return res

# 11)
def superficie_con_mas_tenistas_distintos(lista:List[PartidoTenis])->dict():
    dic_aux = dict()
    for n in lista:
        if n.superficie not in dic_aux:
            dic_aux[n.superficie] = set()
        dic_aux[n.superficie].add(n.jugador1)        
        dic_aux[n.superficie].add(n.jugador2)
    
    res = dict()
    for clave, valor in dic_aux.items():
        res[clave] = (len(valor))
    return max(res.items(), key=lambda e:e[1])

# 12)
def mas_errores_por_jugador(lista:List[PartidoTenis])->dict():
    dic_aux = dict()
    for n in lista:
        if n.jugador1 not in dic_aux:
            dic_aux[n.jugador1] = list()
        dic_aux[n.jugador1].append((n,n.errores_nf1))
        if n.jugador2 not in dic_aux:
            dic_aux[n.jugador2] = list()
        dic_aux[n.jugador2].append((n,n.errores_nf2))

    res = dict()
    for clave, valor in dic_aux.items():
        res[clave] = max(valor,key=lambda e:e[1])[0]
    return res

# 13)
def partido_mas_errores_por_mes(lista:List[PartidoTenis],superficies:List=None)->dict():
    dic_aux = dict()
    for n in lista:
        if superficies == None or n.superficie in superficies:
            if n.fecha.month not in dic_aux:
                dic_aux[n.fecha.month] = list()
            dic_aux[n.fecha.month].append((n.fecha,n.jugador1,n.jugador2,n.errores_nf1+n.errores_nf2))
    
    res = dict()
    for clave, valor in dic_aux.items():
        res[clave] = max(valor,key=lambda e:e[-1])[:3]
    return res

# 14)
def n_partidos_mas_errores_por_jugador(lista:List[PartidoTenis],entero:int)->dict():
    dic_aux = dict()
    for n in lista:
        if n.jugador1 not in dic_aux:
            dic_aux[n.jugador1] = list()
        dic_aux[n.jugador1].append((n,n.errores_nf1))
        if n.jugador2 not in dic_aux:
            dic_aux[n.jugador2] = list()
        dic_aux[n.jugador2].append((n,n.errores_nf2))

    res = dict()
    for clave, valor in dic_aux.items():
        res[clave] = sorted(valor,key=lambda e:e[1],reverse=True)[:entero]
    return res

# 15)
def mayor_numero_dias_sin_jugar(lista:List[PartidoTenis],nombre:str):
    lista_aux = list()
    for n in lista:
        if n.jugador1 == nombre or n.jugador2 == nombre:
            lista_aux.append(n.fecha)

    res = list()
    lista_aux = sorted(lista_aux)
    for anterior,proximo in zip(lista_aux[0:],lista_aux[1:]):
        res.append(proximo-anterior)
    return max(res)
