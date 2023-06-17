from typing import List
from typing import Tuple

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista y Tupla, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# t: Tuple[str,str]  <--Este es un ejemplo para una tupla de strings.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.

"""
Entendiendo el problema..
requiere: 
0.5) El origen no puede ser igual que el destino.

1) SoloParteUnVueloDeCadaCiudad: Si i y j son distintos implica que los vuelos no puede estar el mismo en distintas posiciones.
Por ejemplo, esto no puede suceder:
[('Buenos Aires', 'Madrid'), ('Buenos Aires', 'Barcelona')]
Pues solo puede partir un solo vuelo de cada ciudad.

2) SoloLlegaUnVueloACadaCiudad -> no puede suceder que desde dos ciudades distintas, lleguen al mismo lugar.
[('New York', 'Madrid'), ('Buenos Aires', 'Madrid')]

3) No puede haber vuelos repetidos, ej:
[('New York', 'Madrid'), ('New York', 'Madrid')]

asegura: Tengo que buscar si hay una ruta en los vuelos que vaya desde el origen hasta el destino.
hayRuta: Recibe los vuelos disponibles, el origen y el destino, si hay ruta, entonces tengo que devolver cuantos recorridos debe hacer.
Para empezar, hayRuta habla de un EXISTE por lo tanto, por defecto hay que encontrar 1 sola ruta para que baste con ser V.
hayRuta si: 
la longitud de la ruta es mayor o igual a 1 (cant vuelos a tomar)
si de nuestra ruta, en la primera tupla, la primera posicion está el origen.
si de nuestra ruta, de la ultima tupla en la ultima posicion esté el destino.
si de nuestra ruta, cada camino (escala) tiene uno correspondiente antes, es decir:
Si queremos ir de BSAS a New York: 
[('BSAS', 'Arrecife'), ('Rosario', 'Cancun'), ('Cancun', 'New York')]
En este caso, la ruta es incorrecta pues vemos que la ruta actual (Rosario) no coincide con el ultimo vuelo tomado (estabamos
en Arrecife) Si esto estaría bien formado sería:
[('BSAS', 'Arrecife'), ('Arrecife', 'Cancun'), ('Cancun', 'New York')] pues vemos que donde empieza el otro, es el ultimo del anterior.
"""
def sePuedeLlegar(origen: str, destino: str, vuelos: List[Tuple[str, str]]) -> int :
  return hay_ruta(origen, destino, vuelos)
"""
  "Argentina"
  "Canada"
  vuelos: [("Mexico", "Alemania"), ("Alemania", "Canada"),("Argentina", "Mexico")] -> Existe una ruta porque podemos organizarlo de la siguiente forma:
  [("Argentina", "Mexico"), ("Mexico", "Alemania"), ("Alemania", "Canada")] véase que lo que hay que validar es que siempre el ultimo valor de la tupla en la segunda posicion sea igual al que le sigue pero antes colocando el origen y destino al final.

  Si el destino está en la lista pero NO está en el ultimo i
  1) Guardo el valor anterior que tenia ese ultimo indice.
  2) Muevo esta tupla que tengo en i ahora al final.
  3) En la posicion actual de i coloco la que estaba en el ultimo indice.
"""

"""
  ¿Como lo pensé?
  Literalmente de una forma "medio recursiva y media compleja jadskjdsa".
  Ej: "Argentina", "Canada", [("Mexico", "Alemania"), ("Alemania", "Canada"), ("Argentina", "Mexico")]
  Primero busco, en las tuplas donde está Argentina.
  Encuentro que su par es México, por lo tanto ahora el origen del vuelo será México (origen=mexico destino=canada) por lo tanto tengo que buscar a México en la primera posicion (vuelo[0]), si la encuentro entonces, vuelvo a ingresar y agarro a su par (Alemania) (origen=alemania destino=canada), y busco a Alemania en el primer elemento de una tupla, si es igual, vuelvo a entrar y pregunta quien es el segundo elemento, el segundo elemento es Canada y es igual al origen (origen=canada, destino=canada)! Por lo tanto termino el ciclo while.

  Ej: "A", "B", [] -> Ingresa al while pues origen != destino, como no hay vuelos que recorrer, rutaEncontrada es false, por lo tanto retorna -1.

  Ej: "Estados Unidos", "Canada", [("Ontario", "Canada"), ("Mexico", "Estados Unidos"), ("Estados Unidos", "Ontario")]
  Ingreso a buscar a Estados Unidos a primera posicion de tupla (vuelo[0]), si lo encuentro entonces ahora el origen del vuelo es vuelo[1] (origen=Ontario destino=Canada), recorro todos los vuelos hasta que encuentre a Ontario en primera posición, como lo encuentro, entonces ahora veo cual es su par (vuelo[1]) ¡Es Canada! Entonces origen=destino por lo tanto termina el ciclo while.

  ¿Qué pasa si nunca se cumple el if de adentro del for, ¿qué sucede? Si el for iteró la cantidad maxima de veces y rutaEncontrada sigue siendo false, entonces no hay ruta.

  Básicamente, una vez que encontramos el nuevo origen, sale del for, pero como el while todavia no se cumplio, entonces vuelve a entrar al for.

  Ej: "Estados Unidos", "Canada", [("Ontario", "Canada"), ("Mexico", "Estados Unidos"), ("Estados Unidos", "Ontario")]
  origen = EE.UU, destino = Canada.
  origen!=destino? Sí, por lo tanto entra al while.
  Por cada vuelo que hay en vuelos verifico si EE.UU está en alguna primera posicion.
  Como está en primera posición y lo encontramos, ahora me guardo como origen a "Ontario" y hago un break ¿Por qué un break? Porque justamente quiero que termine ahí el for, vuelva al while padre, y ahora compare "Ontario" y se busque en todas las listas como si fuese el origen.



"""

def hay_ruta(origen: str, destino: str, vuelos: List[Tuple[str, str]]) -> int:
    cantidadDeVuelos: int = 0

    while(origen != destino):
        rutaEncontrada: bool = False

        for vuelo in vuelos:
            if vuelo[0] == origen:
                cantidadDeVuelos += 1
                origen = vuelo[1] 
                rutaEncontrada = True
                break

        if(not rutaEncontrada):
            return -1  

    return cantidadDeVuelos

"""
#Expected True - 3 vuelos, res: 3
print(hay_ruta("Argentina", "Canada", [("Mexico", "Alemania"), ("Alemania", "Canada"), ("Argentina", "Mexico")]))

#Expected True - 4 vuelos, res: 4
print(hay_ruta("Argentina", "Canada", [("Suiza", "Alemania"), ("Alemania", "Canada"), ("Argentina", "Mexico"), ("Mexico", "Suiza")]))

#Expected False, luego de reordenar nos queda [("Argentina", "Mexico"), ("Mexico", "Suiza"), ("Holanda", "Alemania") ("Alemania", "Canada")] pero vemos que Suiza no es igual a Holanda. res: -1
print(hay_ruta("Argentina", "Canada", [("Holanda", "Alemania"), ("Alemania", "Canada"), ("Argentina", "Mexico"), ("Mexico", "Suiza")]))

#Expected False, luego de reordenar nos queda [("Argentina", "Mexico"), ("Mexico", "Suiza"), ("Holanda", "Alemania") ("Alemania", "Canada")] pero vemos que Suiza no es igual a Holanda. res: -1
print(hay_ruta("Argentina", "Canada", [("Mexico", "Suiza"), ("Holanda", "Alemania"), ("Alemania", "Canada"), ("Argentina", "Mexico")]))

#Expected True - res: 1
print(hay_ruta("Argentina", "Canada", [("Argentina", "Canada")]))

#Expected False - res: -1 
print(hay_ruta("Argentina", "Canada", []))

#Expected True - res: 2 pues ("Mexico" y "Estados Unidos") no tiene nada que ver.
print(hay_ruta("Estados Unidos", "Canada", [("Ontario", "Canada"), ("Mexico", "Estados Unidos"), ("Estados Unidos", "Ontario")]))

#Expected - res = 1
print(hay_ruta("A", "B", [("A", "B")])) 

#Expected - res = -1
print(hay_ruta("B", "A", [("A", "B")]))

#Expected - res = 2
print(hay_ruta("A", "B", [("A", "C"), ("C", "B")]))

#Expected - res = -1
print(hay_ruta("A", "B", []))  

#Expected - res = -1
print(hay_ruta("A", "B", [("C", "A"), ("A", "R"), ("G", "E"), ("R", "G"), ("B", "S"), ("S", "Z")]))

##Expected - res = -1
print(hay_ruta("A", "B", [("C", "A"), ("A", "R"), ("G", "E"), ("R", "G"), ("B", "S"), ("S", "B")])) 

##Expected - res = 4
print(hay_ruta("A", "B", [("C", "A"), ("A", "R"), ("G", "E"), ("R", "G"), ("E", "B"), ("Y", "Z")]))
"""

if __name__ == '__main__':
  origen = input()
  destino = input()
  vuelos = input()
  
  print(sePuedeLlegar(origen, destino, [tuple(vuelo.split(',')) for vuelo in vuelos.split()]))