from datetime import date, time, datetime
from collections import namedtuple
import csv

Partido = namedtuple('Partido', 'fecha, equipoloc, equipovis, ganador, golesloc, golesvis, competicion, espectadores') 

def lee_resultado(ruta:str)->list[Partido]:
    res = []
    with open(ruta,'rt', encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=';')
        next(lector)
        for fecha, equipoloc_vis, ganador, golesloc_vis, competicion, espectadores in lector:
            fecha = datetime.strptime(fecha,'%d/%m/%Y').date()
            equipoloc = equipoloc_vis.split(' v ')[0] 
            equipovis = equipoloc_vis.split(' v ')[1] 
            golesloc = int(golesloc_vis.split('-')[0])
            golesvis = int(golesloc_vis.split('-')[1])
            espectadores = int(espectadores)
            res.append(Partido(fecha, equipoloc, equipovis, ganador, golesloc, golesvis, competicion, espectadores))
        return res
    
def selecciones_enfrentadas_israel(lista:list[Partido],entero:int=3)->list:
    dic_aux = dict()
    for n in lista:
        if n.competicion not in dic_aux:
            dic_aux[n.competicion] = 0
        dic_aux[n.competicion] += 1
    lista_copas = [v[0] for v in sorted(dic_aux.items(),key=lambda e:e[1],reverse=True)][:entero]
    
    conjunto_paises = set()
    for n in lista:
        if n.competicion in lista_copas:
            if n.equipoloc == "Israel":
                conjunto_paises.add(n.equipovis)
            else:
                conjunto_paises.add(n.equipoloc)
    return list(conjunto_paises)
        
def lista_diferencias_goles(lista:list[Partido],fecha_inicio:datetime=None,fecha_final:datetime=None)->list:
    list_aux = []
    for n in lista:
        if (fecha_inicio == None or n.fecha >= fecha_inicio ) and (fecha_final == None or n.fecha <= fecha_final):
            if n.equipoloc == 'Israel':
                list_aux.append((n.fecha,n.golesloc))
            else:
                list_aux.append((n.fecha,n.golesvis))
     
    lista_goles_ordenados = [i[1] for i in sorted(list_aux, key = lambda e:e[0])]
    res = [actual-anterior for anterior,actual in zip(lista_goles_ordenados,lista_goles_ordenados[1:])]
    return res

def partidos_por_mes(lista:list[Partido])->list:
    dic_aux = dict()
    for n in lista:
        mes = n.fecha.month
        if mes not in dic_aux:
            dic_aux[mes] = 0
        dic_aux[mes] += 1
    return sorted(list(dic_aux.items()),key=lambda e:e[0])

def partidos_mensuales_por_anyo(lista:list[Partido])->list:
    dic_aux = dict()
    for n in lista:
        año = n.fecha.year 
        if año not in dic_aux:
            dic_aux[año] = list()
        dic_aux[año].append(n)
        
    res = dict()
    for c,v in dic_aux.items():
        res[c] = partidos_por_mes(v)

    return list(res.items())