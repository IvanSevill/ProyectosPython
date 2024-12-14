from typing import NamedTuple,Tuple,List
import csv 
from datetime import date,time,datetime

Compras = NamedTuple("compras",[("dni",str),
                                ("supermercado",str),
                                ("provincia",str),
                                ("fecha_llegada",datetime),
                                ("fecha_salida",datetime),
                                ("total_compra",float)])

# 1)
def lee_compras(ruta:str)->List[Compras]:
    res = []
    with open(ruta,'rt',encoding='utf-8') as f:
        lector = csv.reader(f,delimiter=",")
        next(lector)
        for dni,supermercado,provincia,fecha_llegada,fecha_salida,total_compra in lector:
            # 01/01/2019 04:43,
            fecha_llegada = datetime.strptime(fecha_llegada,"%d/%m/%Y %H:%M")
            fecha_salida = datetime.strptime(fecha_salida,"%d/%m/%Y %H:%M")
            total_compra = float(total_compra)
            res.append(Compras(dni,supermercado,provincia,fecha_llegada,fecha_salida,total_compra))
    return res

# 2)
def compra_maxima_minima_provincia(lista_compras:List[Compras],provincia:str):
    res = list()
    for n in lista_compras:
        if provincia == n.provincia or provincia == None:
            res.append(n.total_compra)
    return (max(res),min(res))

# 3)
def hora_menos_afluencia(lista_compras:List[Compras]):
    dic_aux = dict()
    for n in lista_compras:
        if n.fecha_llegada.hour not in dic_aux:
            dic_aux[n.fecha_llegada.hour] = 0
        dic_aux[n.fecha_llegada.hour] += 1
    return min(dic_aux.items(),key= lambda e:e[1])

# 4)
def supermercados_mas_facturacion(lista_compras:List[Compras],entero:int)->List:
    dic_aux = dict()
    for n in lista_compras:
        if n.supermercado not in dic_aux:
            dic_aux[n.supermercado] = 0
        dic_aux[n.supermercado] += n.total_compra
    
    res = sorted(dic_aux.items(),key=lambda e:e[1],reverse=True)[:entero]  
    return res

# 5)
def clientes_itinerantes(lista_compras:List[Compras],entero:int)->List:
    dic_aux = dict()
    for n in lista_compras:
        if n.dni not in dic_aux:
            dic_aux[n.dni] = set()
        dic_aux[n.dni].add(n.provincia)

    lista_dni_provincias = sorted(list(dic_aux.items()),key= lambda e:e[0])
    res = list()

    for n in lista_dni_provincias:
        if len(n[1]) > entero:
            res.append(n)
    return res

# 6)
def dias_estrella(lista_compras:List[Compras],provincia:str,supermercado:str):
    dic_aux = dict()
    res = []
    for n in lista_compras:
        fecha = n.fecha_llegada.date()
        if n.provincia == provincia and n.supermercado == supermercado:
            if fecha not in dic_aux.keys():
                dic_aux[fecha] = 0
            dic_aux[fecha] += n.total_compra
    
    lista_dias_compras = list(dic_aux.items())

    for ayer, hoy, mañana in zip(lista_dias_compras[0:],lista_dias_compras[1:],lista_dias_compras[2:]):
        if ayer[1] < hoy[1] and hoy [1] > mañana[1]:
            res.append(hoy[0])
    return sorted(res)