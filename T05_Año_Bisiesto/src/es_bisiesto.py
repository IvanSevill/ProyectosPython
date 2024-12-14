def esbisiesto(año:int)->bool:
    res = False
    if año%400 == 0 or (año%4== 0 and año%100!=0):
        res = True
    return res