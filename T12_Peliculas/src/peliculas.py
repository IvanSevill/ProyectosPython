from collections import namedtuple
import csv
from datetime import date, time, datetime

Peliculas = namedtuple("peliculas","id,title,original_language,release_date,vote_average,popularity,adult,genres")

def cabecera(msg:str)->None:
    separador()
    print("--"*35,f"{msg}","--"*35)

def cabecera_ejercicio(numero:int)->None:
    print(f"\n==== Ejercicio {numero}","=="*73,"\n")

def separador()->None:
    print("\n","=="*81,"\n")

# 1)
def lee_peliculas(fichero_peliculas:str,fichero_generos:str)->list[Peliculas]:
    res = []
    diccionario_generos = lee_generos(fichero_generos)
    with open(fichero_peliculas,'rt',encoding='utf-8') as f:
        lector = csv.reader(f,delimiter=',')
        next(lector)
        for id,title,original_language,release_date,vote_average,popularity,adult in lector:
            id = str(id)
            title = str(title)
            original_language = str(original_language)
            release_date = datetime.strptime(release_date.strip(),'%Y-%m-%d').date()
            vote_average = float(vote_average)
            popularity = int(popularity)
            adult = parsea_bool(adult)
            genres = diccionario_generos[id]
            res.append(Peliculas(id,title,original_language,release_date,vote_average,popularity,adult,genres))
    return res

def parsea_bool(booleano:str):
    res = False
    if booleano == "True":
        res = True
    return res

def lee_generos(fichero_generos:str)->dict:
    res = dict()
    with open(fichero_generos,'rt',encoding='utf-8') as f:
        lector = csv.reader(f,delimiter=':')
        next(lector)
        for clave,valor in lector:
            if clave not in res:
                res[clave] = set()
            for n in valor.strip().split(", "):
                res[clave].add(n)
        return res
    
# 2) 
def genero_mas_frecuente(dic_aux:dict)->tuple:
    res = dict()
    for id,conjunto in dic_aux.items():
        for n in conjunto:
            if n not in res:
                res[n] = 0
            res[n] += 1
    return max(list(res.items()),key = lambda e:e[1])

# 3)
def mejor_valorada_por_idioma(lista:list[Peliculas])->list:
    dic_aux = dict()
    for n in lista:
        if n.original_language not in dic_aux:
            dic_aux[n.original_language] = list()
        dic_aux[n.original_language].append((n.title,n.vote_average))

    res = dict()
    for c,v in dic_aux.items():
        res[c] = max(v,key=lambda e:e[1])
    return list(res.items())

# 4)
def media_calificaciones(lista:list[Peliculas],generos_dados:list)->list:
    lista_nota_media = list()
    for n in lista:
        if n.genres == set(generos_dados):
            lista_nota_media.append(n.vote_average)

    res = 0
    if len(lista_nota_media) > 0:
        res = sum(lista_nota_media)/len(lista_nota_media)

    return res

# 5)
def top_n_por_genero(lista:list[Peliculas],limite:int)->dict:
    dic_aux = dict()
    for n in lista:
        for g in n.genres:
            if g not in dic_aux:
                dic_aux[g] = list()
            dic_aux[g].append(n)
        
    res = dict()
    for c,v in dic_aux.items():
        res[c] = sorted(v,key=lambda e:e.vote_average, reverse=True)[:limite]
    return res