from datetime import date,time,datetime
from typing import NamedTuple, List, Set, Dict, Tuple
import csv

Gasto = NamedTuple("gasto",[('num_gasto',int),('usuario',str),('concepto',str),('destinatario',str),('cantidad',float),('fecha',date)])

def lee_gastos(ruta:str)->List[Gasto]:
    res = []
    with open(ruta,'rt',encoding='utf-8') as f:
        lector = csv.reader(f,delimiter=',')
        next(lector)
        for Num_gasto,Usuario,Concepto,Destinatario,Cantidad,Fecha in lector:
            Num_gasto = int(Num_gasto)
            Cantidad = float(Cantidad)
            Fecha = datetime.strptime(Fecha,'%d/%m/%Y').date()
            res.append(Gasto(Num_gasto,Usuario,Concepto,Destinatario,Cantidad,Fecha))
    return res

#2.  pagadores_y_conceptos:  recibe  una  lista  de  tuplas  de  tipo  Gasto  y  devuelve  una  lista  con  todos  los 
#pagadores  y  otra  con  todos  los  conceptos.  Ambas  listas  deben  estar  ordenadas  alfabéticamente  y  sin 
#duplicados. (1 punto)  

def pagadores_y_conceptos(lista:List[Gasto])->List[Tuple[List[str],List[str]]]:
    pagadores = set()
    conceptos = set()
    for n in lista:
        pagadores.add(n.usuario)
        conceptos.add(n.concepto)
    pagadores = sorted(list(pagadores))
    conceptos = sorted(list(conceptos))
    return (pagadores,conceptos)

#3.  total_importe: recibe una lista de tuplas de tipo Gasto y dos fechas, una inicial y otra final, y devuelve el 
#importe total gastado entre esas dos fechas. Si alguna de las fechas recibidas es None no se acotarán las 
#fechas  por  el  extremo  correspondiente.  Tenga  en  cuenta  que  las  fechas  recibidas  serán  cadenas  con  el 
#mismo formato de las contenidas en el fichero CSV. (1,5 puntos) 
    
def total_importe(lista:List[Gasto],f1:date=None,f2:date=None):
    res = list()
    for n in lista:
        if (f1 == None or f1 <= n.fecha) and (f2 == None or f2 >= n.fecha):
            res.append(n.cantidad)
    return sum(res)

#4. conceptos_menos_gastos: recibe una lista de tuplas de tipo Gasto y devuelve una lista con los conceptos 
#en  los  que  se  ha  realizado  un  menor  número  de  gastos.  Tenga  en  cuenta  que  se  buscan  los  conceptos 
#para  los  que  hay  registrados  menos  transacciones,  no  los  que  acumulan  una  cantidad  menor  de  dinero 
#gastado.  Si  hay  más  de  un concepto  con  el mínimo  número  de  gastos,  todos  ellos  deben  aparecer  en  la 
#lista devuelta. (1,5 puntos)  
    
def conceptos_menos_gastos(lista:List[Gasto])->List[str]:
    dic_aux = dict()
    for n in lista:
        if n.concepto not in dic_aux:
            dic_aux[n.concepto] = 0
        dic_aux[n.concepto] += 1
    
    num_menor = min(dic_aux.items(),key=lambda e:e[1])[1]
    res = [c for c,v in dic_aux.items() if v == num_menor]
    return res

#5. pagadores_mayor_importe_medio:  recibe  una  lista  de  tuplas  de  tipo  Gasto  y  un  número  entero  n,  y 
#devuelve una lista de tuplas con los n pagadores con mayor importe medio por gasto, junto con el valor 
#de este importe medio. (2 puntos)
    
def pagadores_mayor_importe_medio(lista:List[Gasto],entero:int):
    dic_aux = dict()
    for n in lista:
        if n.usuario not in dic_aux:
            dic_aux[n.usuario] = list()
        dic_aux[n.usuario].append(n.cantidad)

        res = dict()
        for c,v in dic_aux.items():
            res[c] = sum(v)/len(v)

    return sorted(res.items(),key=lambda e:e[1],reverse=True)[:entero]

#balance: recibe una lista de tuplas de tipo Gasto y devuelve un diccionario con el balance por pagador. El 
#balance  de  un  pagador  consiste  en  una  cantidad  que  indica  el  dinero  que  debe  recibir  (si  el  número  es 
#positivo) o pagar (si el número es negativo) para saldar todos los gastos registrados.  

#Comience  con  un  diccionario  en  el  que  todos  los  pagadores  tengan  un  balance  igual  a  0,  y  vaya 
#actualizando  el  balance  gasto  a  gasto.  Para  cada  gasto,  debe  sumarse  el  importe  total  al  balance  del 
#pagador. Además, debe restarse al balance de todos los beneficiarios de ese gasto el importe por persona 
#correspondiente. Tenga en cuenta que los beneficiarios de un gasto pueden ser o bien todos los usuarios 
#(si aparece "Todos" en el campo destinatario), o bien el usuario que realiza el pago y el que figura como 
#destinatario.  Redondee  los  balances  de  cada  usuario  antes  de  devolver  el  diccionario  para  que  las 
#cantidades tengan dos decimales. (2 puntos)

def balance(lista:List[Gasto])->Dict[str,float]:
    pagadores = pagadores_y_conceptos(lista)[0]
    dic_aux = dict()
    for p in pagadores:
        dic_aux[p] = 0

    for n in lista:
        dic_aux[n.usuario] += n.cantidad
        if n.destinatario == 'Todos':
            cantidad_por_persona = round(n.cantidad / len(pagadores), 2)
            for p in pagadores:
                dic_aux[p] -= cantidad_por_persona
        else:
            dic_aux[n.destinatario] -= n.cantidad

    res = dict()
    for c,v in dic_aux.items():
        res[c] = round(v,2)

    return res
