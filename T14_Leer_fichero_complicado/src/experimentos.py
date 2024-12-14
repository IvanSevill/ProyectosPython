from typing import NamedTuple,List,Tuple
from datetime import date, time, datetime
import csv 

def lee_fichero(ruta:str)->List[Tuple[str,datetime]]:
    res = []
    with open(ruta,'rt',encoding="utf-8") as f:
        lector = csv.reader(f, delimiter=";")
        next(lector)
        for id,fecha,nombre,mediciones,nota,valor in lector:
            fecha = datetime.strptime(fecha.strip(),'%d/%m/%Y').date()
            nombre = nombre.strip()
            mediciones = [int(n) for n in mediciones.strip().split("| ")]
            nota = float(nota.strip().replace(",","."))
            valor = True if valor == "cierto" else False
            # valor = (valor == "cierto")
            res.append((id,fecha,nombre,mediciones,nota,valor))
        return res

def test_lee_fichero(ruta:str):
    for n in lee_fichero(ruta):
        print(n)

if __name__ == "__main__":
    ruta = "T14_Leer_fichero_complicado\data\prueba4.txt"

    test_lee_fichero(ruta)
    