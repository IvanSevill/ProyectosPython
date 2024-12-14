def es_palindromo(a:str)->bool:
    longitud = len(a)
    res = True

    for posicion in range(0,round(longitud/2)):
        if a[posicion] != a[-1-posicion]:
            res = False
            break
        
    return res