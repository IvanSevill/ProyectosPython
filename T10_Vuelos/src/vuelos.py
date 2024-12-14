from collections import namedtuple
import csv
from datetime import datetime, date, time
from typing import NamedTuple, Tuple, List, Set, Dict

Vuelo = namedtuple("vuelo","destino,precio,num_plazas,num_pasajeros,codigo,fecha_salida,duracion,hora_salida,vel_media,escalas,economico")
Vuelo = NamedTuple("vuelo",[("destino",int),("precio",float),("num_plazas",int),("num_pasajeros",int),("codigo",str),("fecha_salida",date),("duracion",int),
                            ("hora_salida",time),("vel_media",float),("escalas",str),("economico",bool)])

def separador():
    print("\n"+"******"*28+"\n")

def cabecera():
    separador() 
    val = 72  
    print("-"*val,"Test del archivo VUELOS","-"*val)
    separador()

# 0)
def lee_vuelos(fichero:str)->list[Vuelo]:
    res = []
    with open(fichero,'rt',encoding='utf-8') as f:
        lector = csv.reader(f,delimiter=';')
        next(lector)
        for destino,precio,num_plazas,num_pasajeros,codigo,fecha_salida,duracion,hora_salida,vel_media,escalas,economico in lector:
            destino = destino.strip()
            precio = precio.replace(',','.').strip()
            precio = float(precio)
            num_plazas = int(num_plazas.strip())
            num_pasajeros = int(num_pasajeros.strip())
            codigo = codigo.strip()
            fecha_salida = datetime.strptime(fecha_salida.strip(),'%d/%m/%Y').date()
            duracion = int(duracion.strip())
            hora_salida = datetime.strptime(hora_salida.strip(),'%H:%M:%S').time()
            vel_media = float(vel_media.strip())
            escalas = parsea_escalas(escalas.replace(' ',''))
            economico = es_economico(economico)

            res.append(Vuelo(destino,precio,num_plazas,num_pasajeros,codigo,fecha_salida,duracion,hora_salida,vel_media,escalas,economico))
    return res

# 0) Función auxiliar de lee_vuelos
def es_economico(precio:str):
    res = False
    if precio.strip() == 'S':
        res=True
    return res

# 0)
def parsea_escalas(escalas:str)->list:
    res = []
    for n in escalas.split("-"):
        res.append(n)
    return res

# 1)
def filtra_vuelos_a(lista:list[Vuelo], destino:str)->list[Vuelo]:
    res = []
    for n in lista:
        if n.destino == destino:
            res.append(n)
    return res

# 2)
def vuelos_mas_velocidad_que(lista:list[Vuelo],velocidad:int)->list[(str,date,float)]:
    res = []
    for n in lista:
        if n.vel_media > velocidad:
            res.append((n.destino,n.fecha_salida,n.vel_media))
    return res

# 3)
def todos_vuelos_mas_velocidad_que(lista:list[Vuelo],velocidad:int)->bool:
    res = True
    for n in lista:
        if n.vel_media < velocidad:
            res = False
    return res

# 4)
def vuelos_mas_velocidad(lista:list[Vuelo])->list:
    lista_ordenada = sorted(lista, key = lambda e:e.vel_media, reverse=True)
    return lista_ordenada[0]

# 5)
def vuelos_por_horario(lista:list[Vuelo],mes:int)->list[(str,float,date,time)]:
    res = []
    lista_ordenada = sorted(lista, key = lambda e:e.hora_salida)
    for n in lista_ordenada:
        if n.fecha_salida.month == mes:
            res.append((n.destino,n.precio,n.fecha_salida,n.hora_salida))
    return res

# 6)
def distintas_escalas(lista:list[Vuelo])->set:
    res = set()
    for n in lista:
        if n.escalas != "":
            res.add(n.escalas+"-"+n.destino)
    return sorted(res)

# 7)
def vuelos_con_escalas_en(lista:list[Vuelo],ciudad:str)->list:
    res = []
    for n in lista:
        if ciudad in n.escalas:
            res.append((n.escalas,n.destino,n.precio,n.num_plazas-n.num_pasajeros))
    res.sort(key = lambda e:e[2])
    return res

# 8)
def numero_de_vuelos_por_destino(lista:list[Vuelo])->dict:
    dic = {}
    for n in lista:
        if n.destino not in dic:
            dic[n.destino] = 0
        dic[n.destino] += 1
    return dic

# 9)
def suma_de_pasajeros_por_fechas(lista:list[Vuelo])->dict:
    dic = {}
    for n in lista:
        if n.fecha_salida not in dic:
            dic[n.fecha_salida] = n.num_pasajeros
        dic[n.fecha_salida] += n.num_pasajeros
    return dic

# 10)
def lista_destinos_por_compañia(lista:list[Vuelo])->dict:
    dic = {}
    for n in lista:
        if n.codigo[:3] not in dic:
            dic[n.codigo[:3]] = list()
        dic[n.codigo[:3]].append(n.destino)
    return dic

# 11)
def vuelos_entre_fechas(lista:list[Vuelo],fecha_inicial=None,fecha_final=None)->list:
    res = []
    for n in lista:
        if (fecha_inicial == None or fecha_inicial <= n.fecha_salida) and (fecha_final == None or n.fecha_salida<=fecha_final):
            res.append((n.fecha_salida,n.destino,n.precio,n.escalas))
    return sorted(res)

# 12)
def destinos_distintos_por_compañia(lista:List[Vuelo])->dict:
    dic = {}
    for n in lista:
        compañia = n.codigo[:3]
        if compañia not in dic:
            dic[compañia] = set()
        dic[compañia].add(n.destino)
    return dic

# 13)
def codigos_vuelos_mas_plazas_que_por_numero_de_escalas(lista:list[Vuelo],numero_limite:int)->dict:
    dic = {}
    for n in lista:
        if n.num_plazas>numero_limite:
            num_escalas = len(n.escalas)
            if num_escalas not in dic:
                dic[num_escalas] = list()
            dic[num_escalas].append(n.codigo)
    return dic

# 14)
def vuelos_menor_duracion_por_destino(lista:list[Vuelo])->dict:
    dic_aux = {}
    for n in lista:
        if n.destino not in dic_aux:
            dic_aux[n.destino] = list()
        dic_aux[n.destino].append((n.codigo,n.duracion))

    res = {}
    for clave, valor in dic_aux.items():
        res[clave] = min(valor,key=lambda e:e[1])
    return  res


# 15)
def promedio_de_precios_por_compañia(lista:list[Vuelo],economico:bool)->dict:
    dic_aux = {}
    for n in lista:
        compañia = n.codigo[:3]
        if n.economico == economico:
            if compañia not in dic_aux:
                dic_aux[compañia] = list()
            dic_aux[compañia].append(n.precio)

    res = {}
    for clave, valor in dic_aux.items():
        res[clave] = round(sum(valor)/len(valor),2)
    return  res

# 16)
def n_vuelos_mayor_velocidad_por_meses(lista:list[Vuelo],numero:int)->dict:
    dic_aux = dict()
    for n in lista:
        if n.fecha_salida.month not in dic_aux:
            dic_aux[n.fecha_salida.month] = list()
        dic_aux[n.fecha_salida.month].append((n.codigo,n.fecha_salida,n.vel_media))

    res = dict()
    for clave,valor in dic_aux.items():
        res[clave] = sorted(valor,key=lambda e:e[2], reverse=True)[:numero]
    return res

# 17)
def escala_por_la_que_pasan_mas_vuelos_entre_fechas(lista:list[Vuelo],fecha_inicial:date=None,fecha_final:date=None)->str:
    dic_aux = dict()
    res = None
    for n in lista:
        if (fecha_inicial == None or fecha_inicial<=n.fecha_salida) and (fecha_final == None or n.fecha_salida<=n.fecha_salida):
            for v in n.escalas:
                if v not in dic_aux:
                    dic_aux[v] = 0
                dic_aux[v] +=  1

    if len(dic_aux)>0:
        res = max(dic_aux.items(), key=lambda e:e[1])[0]
    return res

# 18)
def vuelo_con_mayor_porcentaje_de_ocupación_por_destino(lista:list[Vuelo]):
    dic_aux = dict()
    for n in lista:
        if n.destino not in dic_aux:
            dic_aux[n.destino] = list()
        dic_aux[n.destino].append((n.codigo,n.num_plazas,n.num_pasajeros,n.num_pasajeros/n.num_plazas*100))

    res = dict()
    for clave,valor in dic_aux.items():
        res[clave] = max(valor,key=lambda e:e[3])
    return res

# 19) 
def destino_menor_promedio_de_precios_mayor_porcentaje_ocupación(lista:list[Vuelo],limite:int)->str:
    dic_aux = dict()
    for n in lista:
        porcentaje = n.num_pasajeros*100/n.num_plazas
        if porcentaje >= limite:
            if n.destino not in dic_aux:                
                dic_aux[n.destino] = list()
            dic_aux[n.destino].append(n.precio)

    res = dict()
    for clave,valor in dic_aux.items():
        res[clave] = sum(valor)/len(valor)
    return list(res.items())

# 20)
def compañia_con_mas_pasajeros_por_destino(lista:list[Vuelo]):
    dic_aux = dict()
    for n in lista:
        compañia = n.codigo[:3]
        if n.destino not in dic_aux:
            dic_aux[n.destino] = dict()
        if compañia not in dic_aux[n.destino]:
            dic_aux[n.destino][compañia] = 0
        dic_aux[n.destino][compañia] += n.num_pasajeros

    res = dict()
    for clave, valor in dic_aux.items():
        res[clave] = max(valor, key=valor.get) 
    return res


# 21)
def calcular_el_incremento_o_decremento_de_pasajeros(lista:list[Vuelo]):
    dic_aux = dict()
    for n in lista:
        if n.fecha_salida not in dic_aux:
            dic_aux[n.fecha_salida] = 0
        dic_aux[n.fecha_salida] += n.num_pasajeros

    res = dict()
    anterior = 0
    for clave, valor in dic_aux.items():
        res[clave] = valor - anterior
        anterior = valor
    return list(res.items())