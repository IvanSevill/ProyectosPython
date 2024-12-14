from collections import namedtuple
from datetime import date,time,datetime
from typing import List,Set,Tuple
import csv

Ruta = namedtuple('Ruta', 'ciudad_inicio, coordenada, fecha_ruta, km, gasolineras, dificultad, zona_descanso, vel_max, vel_min')
Coordenada = namedtuple('Coordenada', 'latitud, longitud')

def lee_rutas(ruta:str)->List[Ruta]:
    res = []
    with open(ruta,'rt',encoding='utf-8') as f:
        lector = csv.reader(f,delimiter=';')
        next(lector)
        for ciudad_inicio,latitud_longitud,fecha_ruta,km,gasolineras,dificultad,zona_descanso,vel_max,vel_min in lector:
            ciudad_inicio = ciudad_inicio.rstrip()
            latitud_longitud = Coordenada(float(latitud_longitud.split('/')[0]),float(latitud_longitud.split('/')[1]))
            fecha_ruta = det_fecha_ruta(fecha_ruta)
            km = float(km)
            gasolineras = int(gasolineras)
            zona_descanso = (zona_descanso == 'True')
            vel_max = int(vel_max)
            vel_min = int(vel_min)
            res.append(Ruta(ciudad_inicio,latitud_longitud,fecha_ruta,km,gasolineras,dificultad,zona_descanso,vel_max,vel_min))
    return res

def det_fecha_ruta(fecha:str)->datetime:
    if fecha == "":
        fecha = datetime.today().date()
    else:
        fecha = datetime.strptime(fecha,'%m/%d/%Y').date()
    return fecha

def acumular_kms_por_meses(lista:List[Ruta])->dict:
    dic_aux = dict()
    for ruta in lista:
        año = ruta.fecha_ruta.year
        mes = ruta.fecha_ruta.month
        if año not in dic_aux:
            dic_aux[año] = {mes: 0 for mes in range(1, 13)}
        dic_aux[año][mes] += ruta.km

    res = dict()
    for c,v in dic_aux.items():
        res[c] = list(v.values())

    return res
        
def diferencias_kms_meses_anyo(lista:List[Ruta])->dict:
    kms_por_año = acumular_kms_por_meses(lista)
    dic_aux = dict()

    for año, kms in kms_por_año.items():
        diferencias = [actual - anterior for anterior, actual in zip(kms[:-1], kms[1:])]
        dic_aux[año] = diferencias

    return dic_aux
    
def top_rutas_lejanas(lista:List[Ruta],n:int,c:Coordenada,km_min:int=None)->List[Ruta]:
    lista_aux = list()
    for ruta in lista:
        if km_min == None or ruta.km > km_min:
            lista_aux.append((ruta,abs(ruta.coordenada.latitud - c.latitud)+abs(ruta.coordenada.longitud-c.longitud)))
    return [ruta for ruta,distancia in sorted(lista_aux,key=lambda e:e[1],reverse=True)[:n]]

def ciudades_top_tiempo_dificultad(lista:List[Ruta],n:int)->dict:
    dic_aux = dict()
    for ruta in lista:
        if ruta.zona_descanso:
            if ruta.dificultad not in dic_aux:
                dic_aux[ruta.dificultad] = list()
            duracion = ruta.km / ruta.vel_min
            dic_aux[ruta.dificultad].append((ruta.ciudad_inicio,duracion))

    res = dict()
    for c,v in dic_aux.items():
        res[c] = [i[0] for i in sorted(v,key=lambda e:e[1],reverse=True)][:n]
    return res
