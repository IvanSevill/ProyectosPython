from math import sqrt

def raices(a,b,c):
    raiz1 = None
    raiz2 = None
    discriminante = b**2-4*a*c

    if a!=0 and discriminante >=0:
        raiz1 = (-b+sqrt(discriminante))/(2*a)
        raiz2 = (-b-sqrt(discriminante))/(2*a)

    return(raiz1,raiz2)
