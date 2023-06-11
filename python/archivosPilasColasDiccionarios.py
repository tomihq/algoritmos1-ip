#1.1.1 Implementar una funcion contarlineas que cuenta la cantidad de lineas de texto del archivo dado. nombre_archivo es de tipo str y es in, por lo tanto no hay qu emodificarlo.
def contar_lineas(nombre_archivo: str) -> int:
    file:list[str] = open(nombre_archivo, "r", encoding="utf-8");
    cantidadLineas: int = len(file.readlines())
    file.close()
    return cantidadLineas;

""" print(contar_lineas("test.txt")) """

#1.1.2: una funcion existePalabra(in palabra : str, in nombre archivo : str) → bool que dice si una palabra existe en un archivo de texto o no. No utilizo early return porque prefieren un return solo al final de la funcion.

def pertenece(s: list[int], e: int) -> bool:
    for i in range(0, len(s)):
        if(s[i] == e): return True
    return False

#1.1.2 (forma 1)
def existePalabra1(palabra: str, nombre_archivo: str) -> bool:
    file = open(nombre_archivo, "r", encoding="utf-8");
    existePalabra: bool = False;    
    for i in file.readlines():
        palabrasEnLinea: list[str] = i.split();
        if(pertenece(palabrasEnLinea, palabra)):
            existePalabra = True
            break 
    
    file.close()
    return existePalabra

print(existePalabra1("laboratorio", "test.txt"))

#1.1.3. una función cantidadApariciones(in nombre archivo : str, in palabra : str) → int que devuelve la cantidad de apariciones de una palabra en un archivo de texto
def cantidadApariciones(nombre_archivo: str, palabra: str) -> int:
    file = open(nombre_archivo, "r", encoding="utf-8");
    cantidadAparicionesPalabra: int = 0;    
    for i in file.readlines():
        palabrasEnLinea = i.split();
        for j in range(0, len(palabrasEnLinea)):
            if(palabrasEnLinea[j] == palabra):
                cantidadAparicionesPalabra+=1
       
    
    file.close()
    return cantidadAparicionesPalabra

#expected: 4
print(cantidadApariciones("test.txt", "clases"))

"""
1.2. Dado un archivo de texto con comentarios, implementar una función clonarSinComentarios(innombre archivo : str)
que toma un archivo de entrada y genera un nuevo archivo que tiene el contenido original sin las líneas comentadas. Para este
ejercicio vamos a considerar comentarios como aquellas líneas que tienen un caracter # como primer caracter de la línea, o si no
es el primer caracter, se cumple que todos los anteriores son espacios.
Ejemplo:
    # esto es un comentario
    # esto tambien
    esto no es un comentario # esto tampoco

    Leo cada una de las lineas (las convierto en array para tener todas, accedo a la primera palabra y me fijo si es #)

"""
def clonarSinComentarios(nombre_archivo: str) -> None:
    file = open(nombre_archivo, "r", encoding="utf-8");
    archivoDestino = open("archivoSinComentarios.txt", "w", encoding="utf-8");  
    lineasArchivoNuevo = []; 
    for i in file.readlines():
        if(not(i.strip()[0] == "#")):
            lineasArchivoNuevo.append(i);
    file.close()

    for linea in lineasArchivoNuevo:
        archivoDestino.write(linea)
    
    archivoDestino.close()
    
    

clonarSinComentarios("archivoConComentarios.txt")

"""
1. 3. Dado un archivo de texto, implementar una función que escribe un archivo nuevo (‘reverso.txt‘) que tiene las
    mismas líneas que el original, pero en el orden inverso.
    Ejemplo: si el archivo original es
        Esta es la primer linea.
        Y esta es la segunda.
    debe generar:
        Y esta es la segunda.
        Esta es la primer linea.
"""

def generar_archivo_inverso(nombre_archivo: str) -> None:
    file = open(nombre_archivo, "r", encoding="utf-8");
    archivoDestino = open("reverso.txt", "w", encoding="utf-8");  
    lineasArchivoNuevo = []; 
    lineasEnReverso = file.readlines()[::-1]
    for lineaArchivo in lineasEnReverso:
        lineasArchivoNuevo.append(lineaArchivo);
    file.close()

    for linea in lineasArchivoNuevo:
        archivoDestino.write(linea.strip() +  "\n") #el strip saca los espacios en blanco y por cada linea agrega un salto de linea para separarlas.
    
    archivoDestino.close()
    

generar_archivo_inverso("archivoConComentarios.txt")

"""
    1.4. Dado un archivo de texto y una frase (es decir, texto que puede estar separado por "\n"), implementar una función que la agregue al final del archivo original (sin hacer una copia).

"""

def agregar_frase_al_final(nombre_archivo: str, frase: str) -> None:
    file = open(nombre_archivo, "a", encoding="utf-8");
    file.writelines(frase.strip() +  "\n")
    file.close()
    
agregar_frase_al_final("archivoConComentarios.txt", "Hello, world!\nThis is Frank Sinatra")

"""
    1.5. idem, pero agregando la frase al comienzo del archivo original (de nuevo, sin hacer una copia del archivo).

"""

def agregar_frase_al_inicio(nombre_archivo: str, frase: str) -> None:
    file = open(nombre_archivo, "a", encoding="utf-8");
    file.insert(frase.strip() +  "\n")
    file.close()
    
""" agregar_frase_al_inicio("archivoConComentarios.txt", "Hello, world!\nThis is Frank Sinatra inicio") """

"""
1. 7. Implementar una función que lea un archivo de texto separado por comas (comma-separated values, o .csv) que
contiene las notas de toda la carrera de un grupo de alumnos y calcule el promedio final de un alumno dado. La función
promedioEstudiante(in lu : str) → float. El archivo tiene el siguiente formato:
nro de LU ( str ) , materia ( str ) , fecha ( str ) , nota ( float )
Al no estar bien especificado, controlo que efectivamente si el alumno no tiene ninguna nota, devuelvo 0.
"""

def promedio_estudiante(lu: str) -> float:
    notas = open("./assets/notas2023.csv", "r", encoding = 'utf-8');
    notasAlumno:list[float] = [];

    for i in notas.readlines():
        filas: list[str] = i.split(";");
        if(filas[0] == lu):
            notasAlumno.append(float(filas[3]))

    notas.close();
    if(len(notasAlumno)>0):
        return sum(notasAlumno) / len(notasAlumno)
    else:
        return 0

print(promedio_estudiante("325/23"))

"""
    Ejercicio 2.8: Implementar una función generarNrosAlAzar(in n : int, in desde : int, in hasta : int) → list[int] que genere
    una lista de n numeros enteros al azar en el rango [desde, hasta]. Pueden user la función random.sample()
"""
from random import sample


def generar_nros_al_azar(n : int, desde: int, hasta: int) -> list[int]:
    nrosAzar: list[int] = sample(range(desde, hasta + 1), n)
    listaNrosAzar: list[int] = [];
    for i in range(0, len(nrosAzar)):
        listaNrosAzar.append(nrosAzar[i]);
    return listaNrosAzar;

""" print(generarNrosAlAzar(3, 1, 3)); """


"""
    Ejercicio 2.9. Usando la funciòn del punto anterior, implementar otra función que arme una pila con los numeros generados al azar. Pueden usar la clase LifoQueue() que es un ejemplo de una implementación básica:
"""

from queue import LifoQueue as Pila
def colocar_en_pila_nros_generados_azar(nrosAzar: list[int]) -> Pila:
    pila = Pila();
    for i in range(0, len(nrosAzar)):
        pila.put(nrosAzar[i])

    """ Si se quiere probar que la pila tiene los elementos de la lista de nrosAzar. 
    while(not(pila.empty())):
        print(pila.get()) 
    """

    return pila;

""" print(colocar_en_pila_nros_generados_azar(generar_nros_al_azar(3, 1, 3))) """


""""
    Ejercicio 2.10. Implementar una función cantidadElementos(inout : pila) → int que, dada una pila, cuente la cantidad de elementos que contiene.
    OJO: Acá está mal que sea in, como es una pila(internamente construida con una lista, JAMÁS una lista puede ser in porque es un tipo no primitivo, por lo tanto al ser por referencia siempre pero siempre va a ser inout)
"""

def cantidad_elementos_en_pila(pila: Pila) -> int:
    cantidad_elementos:int = 0;
    while(not(pila.empty())):
        cantidad_elementos += 1;
        pila.get();
    return cantidad_elementos;

""" print(cantidad_elementos_en_pila(colocar_en_pila_nros_generados_azar(generar_nros_al_azar(3, 1, 3)))) """

""""
    Ejercicio 2.11. Dada una pila de enteros, implementar una función buscarElMaximo(inout p : pila) → int que devuelva el máximo elemento.
    OJO: Acá está mal que sea in, como es una pila(internamente construida con una lista, JAMÁS una lista puede ser in porque es un tipo no primitivo, por lo tanto al ser por referencia siempre pero siempre va a ser inout)
    Al no estar especificado, si no tiene elementos devuelvo -1 por defecto.

"""

def buscar_el_maximo(p: Pila) -> int:
    maximoElemento: int = -1;
    while(not(p.empty())):
            valor = p.get()
            if(valor>maximoElemento):
                maximoElemento = valor;
    
    return maximoElemento


""" print(buscar_el_maximo(colocar_en_pila_nros_generados_azar(generar_nros_al_azar(3, 8, 12)))) """

"""
Ejercicio 3. 13. Usando la función generarNrosAlAzar() definida en la sección anterior, implementar una función que arme una
cola de enteros con los numeros generados al azar. Pueden usar la clase Queue() que es un ejemplo de una implementación básica:
"""
from queue import Queue as Cola

def colocar_en_cola_nros_generados_azar(nrosAzar: list[int]) -> Cola:
        cola = Cola();
        for i in range(0, len(nrosAzar)):
            cola.put(nrosAzar[i])
            """ Si se quiere probar que la cola tiene los elementos de la lista de nrosAzar. 
        while(not(cola.empty())):
            print(cola.get()) 
            """

        return cola;

""" print(colocar_en_cola_nros_generados_azar(generar_nros_al_azar(3, 8, 12))) """

"""
    Ejercicio 3. 14. Implementar una función cantidadElementos(in c : cola) → int que, dada una cola, cuente la cantidad de
    elementos que contiene. Comparar con la versión usando pila.
"""

def cantidad_elementos_en_cola(cola: Cola) -> int:
    cantidad_elementos:int = 0;
    while(not(cola.empty())):
        cantidad_elementos += 1;
        cola.get();
    return cantidad_elementos;

""" print(cantidad_elementos_en_cola(colocar_en_pila_nros_generados_azar(generar_nros_al_azar(3, 1, 3)))) """

"""
    Ejercicio 3. 15. Dada una cola de enteros, implementar una función buscarElMaximo(in c : cola) → int que devuelva el máximo
    elemento. Comparar con la versión usando pila.
"""


def buscar_el_maximo_cola(c: Cola) -> int:
    maximoElemento: int = -1;
    while(not(c.empty())):
            valor = c.get()
            if(valor>maximoElemento):
                maximoElemento = valor;
    
    return maximoElemento

""" print(buscar_el_maximo_cola(colocar_en_pila_nros_generados_azar(generar_nros_al_azar(1, 8, 12)))) """

