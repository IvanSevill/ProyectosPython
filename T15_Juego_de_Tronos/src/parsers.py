def parsea_gana_atacante(dato:str)->bool:
    res = False
    if dato == "win":
        res = True
    return res

def parsea_muertes_principales(dato:str)->bool:
    res = False
    if dato == "1":
        res = True
    return res

def comandantes_atacantes_y_comandantes_atacados(dato:str)->list:
    res = []
    if dato != "":
        for comandantes in dato.split(","):
            res.append(comandantes.strip())
    return res

def número_de_atacantes_y_atacados(dato:str)->int:
    res = None
    if dato != "":
        res = int(dato)
    return res