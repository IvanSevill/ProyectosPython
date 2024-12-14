from math import sqrt
def perimetro(a:float,b:float,c:float)->float:
    return a+b+c

def area_por_heron(a:float,b:float,c:float)->float:
    s = perimetro(a,b,c)/2
    if a + b < c or a > b + c:
        area = None
    else:
        area = sqrt(s*(s-a)*(s-b)*(s-c))
    return area
