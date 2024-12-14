## Fundamentos de Programación
# Ejercicio de laboratorio: Juego de Tronos
### Autor: Fermín L. Cruz
### Revisores: José C. Riquelme, Mariano González, Toñi Reina
### Adaptación para laboratorio: Toñi Reina

Este proyecto es una adaptación del primer parcial del curso 2021/22. 

## Estructura de las carpetas del proyecto

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
    * **got.py**: Contiene funciones para explotar los datos de juego de tronos.
    * **got_test.py**: Contiene funciones de test para probar las funciones del módulo `got.py`. En este módulo está el main.
    * **parsers.py**: Contiene funciones de conversión de tipos.
* **/data**: Contiene el dataset o datasets del proyecto
    * **battles.csv**: Archivo con los datos de batallas de Juego de tronos.

## Ejercicios a realizar

Disponemos de datos sobre las batallas libradas en la serie de libros de Game of Thrones. Para cada batalla, tenemos en un fichero CSV la siguiente información (los campos aparecen separados por punto y coma):
-	**nombre**: nombre de la batalla, de tipo ``str``.
-	**rey atacante**: nombre del rey que inicia la batalla, de tipo ``str``.
-	**rey atacado**: nombre del rey que es atacado, de tipo ``str``.
-	**gana atacante**: indica si los atacantes ganaron la batalla, de tipo ``bool`` (en el fichero consta "win" si ganaron, "loss" si ganaron los atacados).
-	**muertes principales**: indica si murieron personajes principales de la trama, de tipo ``bool`` (en el fichero consta "1" si murieron, "0" si no).
-	**comandantes atacantes y comandantes atacados**: lista de nombres de los personajes que lideraron el ataque y la defensa, respectivamente, ambos de tipo ``list`` de ``str``. Los nombres aparecen separados por comas, si hay más de uno. Estos campos pueden estar vacíos, en cuyo caso se deben inicializar con una lista vacía.
-	**region**: nombre de la región donde se llevó a cabo la batalla, de tipo ``str``.
-	**número de atacantes y número de atacados**: indica el número aproximado de integrantes de los ejércitos atacante y atacado, respectivamente, ambos de tipo ``int``. Estos campos pueden estar vacíos, en cuyo caso se deben inicializar con el valor ``None``.
Por ejemplo, la siguiente línea del fichero:

```
Battle of Torrhen's Square; Robb Stark; Greyjoy; win; 0; Rodrik Cassel, Cley Cerwyn; Dagmer Cleftjaw; The North; 244; 900 
```

indica que la batalla conocida como "Battle of Torrhen’s Square" fue iniciada por el rey "Robb Stark", contra el rey "Greyjoy"; la batalla fue ganada por el rey atacante, y no se produjeron muertes entre los personajes principales que participaron en la misma; los comandantes que lideraron el ataque fueron "Rodrik Cassel" y "Cley Cerwyn", mientras que hubo un único comandante liderando la defensa, "Dagmer Cleftjaw"; por último, la batalla transcurrió en la región "The North", y en ella participaron 244 atacantes y 900 defensores.

Para almacenar los datos de un entrenamiento se usará obligatoriamente la siguiente ``NamedTuple``:
```python 
BatallaGOT = NamedTuple('BatallaGOT',
    [('nombre', str), ('rey_atacante', str), ('rey_atacado', str), ('gana_atacante', bool),
     ('muertes_principales', bool), ('comandantes_atacantes', List[str]), ('comandantes_atacados', List[str]),
     ('region', str), ('num_atacantes', Optional[int]), ('num_atacados', Optional[int])])
```

Cree un módulo **got.py** e implemente en él las funciones que se piden. Utilice *typing* para definir el tipo de los parámetros y el tipo de devolución de cada función. Implemente los tests correspondientes en el módulo **got_test.py**; las puntuaciones indicadas para cada ejercicio incluyen la realización de dicho test.

1.	**lee_batallas**: lee un fichero de entrada en formato CSV codificado en utf-8 y devuelve una lista de tuplas de tipo ``BatallaGOT`` conteniendo todos los datos almacenados en el fichero. Use el método de cadenas ``split`` para separar los comandantes atacantes y atacados, y el método de cadenas ``strip`` para eliminar los espacios al inicio o final de los nombres de los comandantes. 
Por ejemplo, el último elemento de la lista devuelta debe ser:
```
BatallaGOT(nombre='Siege of Raventree', rey_atacante='Joffrey Baratheon', rey_atacado='Robb Stark', gana_atacante=True, muertes_principales=False, comandantes_atacantes=['Jonos Bracken', 'Jaime Lannister'], comandantes_atacados=['Tytos Blackwood'], region='The Riverlands', num_atacantes=1500, num_atacados=None).
```
_(1,25 puntos)_

2.	**reyes_mayor_menor_ejercito**: recibe una lista de tuplas de tipo ``BatallaGOT`` y devuelve una tupla con dos cadenas correspondientes a los nombres de los reyes con el mayor y el menor ejército, respectivamente, del acumulado de todas las batallas. Para estimar el tamaño del ejército de un rey se deben sumar los números de atacantes o de atacados de todas las batallas en las que ha participado dicho rey como atacante o como atacado. _(2 puntos)_

3.	**batallas_mas_comandantes**: recibe una lista de tuplas de tipo ``BatallaGOT``, un conjunto de cadenas ``regiones``, con valor por defecto ``None``, y un valor entero ``n`` con valor por defecto ``None``, y devuelve una lista de tuplas ``(str, int)`` con los nombres y el total de comandantes participantes de aquellas n batallas con mayor número de comandantes participantes (tanto atacantes como atacados), llevadas a cabo en alguna de las regiones indicadas en el parámetro regiones. Si el parámetro ``regiones`` es ``None`` se considerarán todas las regiones; por su parte, si el parámetro ``n`` es ``None`` se devolverán las tuplas correspondientes a todas las batallas de las regiones escogidas. En todos los casos, la lista devuelta estará ordenada de mayor a menor número de comandantes. Por ejemplo, si la función recibe la lista completa de batallas contenida en el CSV, y si ``regiones`` es `{'The North', 'The Riverlands'}` y ``n`` es ``4``, la función devuelve ``[('Battle of the Green Fork', 9), ('Battle of the Fords', 9), ('Battle of the Camps', 5), ('Sack of Winterfell', 5)]``. _(2 puntos)_

4.	**rey_mas_victorias**: recibe una lista de tuplas de tipo ``BatallaGOT`` y una cadena ``rol``, con valor por defecto ``"ambos"``, y devuelve el nombre del rey que acumula más victorias. Tenga en cuenta que un rey puede ganar una batalla en la que actúa como atacante, en cuyo caso el campo ``gana_atacante`` será ``True``, o una batalla en la que actúa como atacado, en cuyo caso el campo ``gana_atacante`` será ``False``. Si el parámetro ``rol`` es igual a ``"atacante"``, se devolverá el nombre del rey que acumula más victorias como atacante; si ``rol`` es igual a ``"atacado"``, se devolverá el nombre del rey que acumula más victorias como atacado; si ``rol`` es igual a ``"ambos"``, se devolveré el nombre del rey que acumula más victorias en todas las batallas en las que ha participado (sumando sus victorias como atacante y como atacado). Si ningún rey acumula victorias del rol especificado en la lista de batallas recibida, la función devuelve ``None``. Por ejemplo, si el parámetro rol contiene ``"ambos"`` y la función devuelve ``"Stannis Baratheon"``, significa que dicho rey es el que ha ganado más batallas de la lista de batallas recibida, sumando tanto las victorias en batallas en las que fue atacante, como las victorias en batallas en las que fue atacado. _(2,75 puntos)_

5.	**rey_mas_victorias_por_region**: recibe una lista de tuplas de tipo ``BatallaGOT`` y una cadena ``rol``, con valor por defecto ``"ambos"``, y devuelve un diccionario que relaciona cada región con el nombre del rey o reyes que acumula más victorias en batallas ocurridas en esa región. El parámetro ``rol`` tiene el mismo significado que en la función anterior. Si para alguna región no hay ningún rey que haya ganado una batalla con el rol especificado, en el diccionario aparecerá el valor ``None`` asociado a dicha región. Puede usar la función ``rey_mas_victorias`` para resolver este ejercicio. 
Por ejemplo, si pasamos a la función la lista completa de batallas contenida en el CSV, y el parámetro ``rol`` contiene ``"ambos"``, la función devuelve un diccionario que, entre otros ítems, asocia la clave ``"The Stormlands"`` a ``"Joffrey Baratheon"``; esto significa que dicho rey es el que ganó más batallas de entre las batallas ocurridas en "The Stormlands", sumando tanto las victorias en batallas en las que fue atacante, como las victorias en batallas en las que fue atacado. _(2 puntos)_


