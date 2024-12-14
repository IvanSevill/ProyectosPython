from typing import List, Set, Dict, NamedTuple,Tuple,Counter
from datetime import date, time, datetime 
import csv 

Venta = NamedTuple('venta',[('fecha',date),('ciudad',str),('modelo',str),('precio',float),('unidades',int),('financiado',bool)])

def lee_ventas(ruta:str)->List[Venta]:
    res = []
    with open(ruta,'rt',encoding='utf-8') as f:
        lector = csv.reader(f,delimiter=',')
        next(lector)
        for Fecha,Ciudad,Modelo,Precio,Unidades,Financiado in lector:
            Fecha = datetime.strptime(Fecha,'%d/%m/%Y').date()
            Precio = float(Precio)
            Unidades = int(Unidades)
            Financiado = (Financiado == "SI")
            res.append(Venta(Fecha,Ciudad,Modelo,Precio,Unidades,Financiado))
    return res 

#unidades_vendidas:  recibe  una  lista  de  tuplas  de  tipo  Venta,  un  conjunto  de  modelos  y  dos  fechas,  y 
#devuelve el total de unidades vendidas de los modelos de automóvil que figuran en el conjunto entre las 
#dos  fechas,  ambas  incluidas.  Si  fecha_inicial  es  None,  entonces  el  periodo  es  desde  el  principio,  y  si 
#fecha_final es None, el periodo es hasta el final.

def unidades_vendidas(lista:List[Venta],conj_modelos:Set[str],f1:date,f2:date)->int:
    dic_aux = dict()
    for n in lista:
        if n.fecha >= f1 and n.fecha <=f2:
            if n.modelo in conj_modelos:
                if n.modelo not in dic_aux:
                    dic_aux[n.modelo] = 0
                dic_aux[n.modelo] += n.unidades
    res = sum(dic_aux.values())
    return res

#dicc_beneficios_por_modelo_año:  recibe  una  lista  de  tuplas  de  tipo  Venta  y  un  año,  y  devuelve  un 
#diccionario  que  relaciona  cada  modelo  de  automóvil  con  el  beneficio  de  las  ventas  del  modelo  en  ese 
#año. Tenga en cuenta la forma en que se calcula el beneficio de cada venta, descrita al principio de este 
#documento. (1 punto) 

#el  beneficio  de  cada  venta  se  calcula  según  la  venta  haya  sido 
#financiada  o  no.  Si  ha  sido  financiada,  el  beneficio  es  el  15%  del  importe  total  de  la  venta,  y  si  no  ha  sido 
#financiada el beneficio es el 10%. 

def dicc_beneficios_por_modelo_año(lista:List[Venta],año:int)->Dict[str,float]:
    dic_aux = dict()
    for n in lista: 
        if n.fecha.year == año:
            if n.modelo not in dic_aux:
                dic_aux[n.modelo] = 0
            if n.financiado:
                dic_aux[n.modelo] += 0.15*n.precio*n.unidades
            else:
                dic_aux[n.modelo] += 0.10*n.precio*n.unidades
    return dic_aux

#dias_de_mas_unidades: recibe una lista de tuplas de tipo Venta y devuelve una lista con los días en los 
#que se realizó la venta con mayor número de unidades. Tenga en cuenta que se buscan las fechas para las 
#que hubo un máximo número de unidades vendidas en una sola venta.  (1,5 puntos)

def dias_de_mas_unidades(lista:List[Venta])->List[Tuple[date,int]]:
    dic_aux = dict()
    for n in lista:
        if n.fecha not in dic_aux:
            dic_aux[n.fecha] = list()
        dic_aux[n.fecha].append(n.unidades)
    
    res = dict()
    for c,v in dic_aux.items():
        res[c] = max(v)
    
    venta_maxima = max(res.items(),key= lambda e:e[1])[1]
    sol = list()
    for c,v in res.items():
        if v == venta_maxima:
            sol.append(c)
    return sol

#lista_dif_unidades_mes: recibe una lista de tuplas de tipo Venta y devuelve una lista con las 
#diferencias del número de unidades vendidas acumuladas para todos los años de un mes con respecto al 
#anterior. Por ejemplo, el primer valor sería la diferencia entre el número de unidades vendidas en febrero 
#(para todos los años) con respecto a las de enero (para todos los años). Para facilitar la solución, suponga 
#que existen datos para todos los meses. (2 puntos) 

def lista_dif_unidades_mes(lista:List[Venta]): #->List[int]:
    dic_aux = dict()
    for n in lista:
        mes = n.fecha.month
        if mes not in dic_aux:
            dic_aux[mes] = 0
        dic_aux[mes]+=n.unidades
    lista_ventas = [v[1] for v in sorted(dic_aux.items(),key=lambda e:e[0])]
    return [actual-anterior for anterior,actual in zip(lista_ventas,lista_ventas[1:])]

#modelos_vendidos_mas_n_en_año:  recibe  una  lista  de  tuplas  de  tipo  Venta,  un  año  y  un  número  n,  y 
#devuelve  un  conjunto  con  los  modelos  que  se  han  vendido  durante  ese  año  en  más  de  n  ciudades.  (2 
#puntos)

def modelos_vendidos_mas_n_en_año(lista:List[Venta],año:int,entero:int)->Set[str]:
    dic_aux = dict()
    for n in lista:
        if n.fecha.year == año:
            if n.modelo not in dic_aux:
                dic_aux[n.modelo] = list()
            dic_aux[n.modelo].append(n.ciudad)

    dic_counter = dict()
    for c,v in dic_aux.items():
        dic_counter[c] = Counter(v)
    
    res = set()
    for modelo,cont in dic_counter.items():
        if len(cont) > entero:
            res.add(modelo)
            
    return res