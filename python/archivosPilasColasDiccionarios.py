#1.1 Implementar una funcion contarlineas que cuenta la cantidad de lineas de texto del archivo dado. nombre_archivo es de tipo str y es in, por lo tanto no hay qu emodificarlo.
def contar_lineas(nombre_archivo: str) -> int:
    file:list[str] = open(nombre_archivo, "r", encoding="utf-8");
    cantidadLineas: int = len(file.readlines())
    file.close()
    return cantidadLineas;

""" print(contar_lineas("test.txt")) """

#1.2: una funcion existePalabra(in palabra : str, in nombre archivo : str) → bool que dice si una palabra existe en un archivo de texto o no. No utilizo early return porque prefieren un return solo al final de la funcion.

def pertenece(s: list[int], e: int) -> bool:
    for i in range(0, len(s)):
        if(s[i] == e): return True
    return False

#1.2 (forma 1)
def existePalabra1(palabra: str, nombre_archivo: str) -> bool:
    file:list[str] = open(nombre_archivo, "r", encoding="utf-8");
    existePalabra: bool = False;    
    for i in file.readlines():
        palabrasEnLinea: list[str] = i.split();
        if(pertenece(palabrasEnLinea, palabra)):
            existePalabra = True
            break 
    
    file.close()
    return existePalabra

print(existePalabra1("laboratorio", "test.txt"))

#1. 3. una función cantidadApariciones(in nombre archivo : str, in palabra : str) → int que devuelve la cantidad de apariciones de una palabra en un archivo de texto
def cantidadApariciones(nombre_archivo: str, palabra: str) -> int:
    file:list[str] = open(nombre_archivo, "r", encoding="utf-8");
    cantidadAparicionesPalabra: int = 0;    
    for i in file.readlines():
        palabrasEnLinea: list[str] = i.split();
        for j in range(0, len(palabrasEnLinea)):
            if(palabrasEnLinea[j] == palabra):
                cantidadAparicionesPalabra+=1
       
    
    file.close()
    return cantidadAparicionesPalabra

#expected: 4
print(cantidadApariciones("test.txt", "clases"))

"""
2. Dado un archivo de texto con comentarios, implementar una funci´on clonarSinComentarios(innombre archivo : str)
que toma un archivo de entrada y genera un nuevo archivo que tiene el contenido original sin las l´ıneas comentadas. Para este
ejercicio vamos a considerar comentarios como aquellas l´ıneas que tienen un caracter # como primer caracter de la l´ınea, o si no
es el primer caracter, se cumple que todos los anteriores son espacios.
Ejemplo:
    # esto es un comentario
    # esto tambien
    esto no es un comentario # esto tampoco

    Leo cada una de las lineas (las convierto en array para tener todas, accedo a la primera palabra y me fijo si es #)

"""
def clonarSinComentarios(nombre_archivo: str) -> None:
    file:list[str] = open(nombre_archivo, "r", encoding="utf-8");
    archivoDestino = open("archivoSinComentarios.txt", "w", encoding="utf-8");  
    lineasArchivoNuevo: list[str] = []; 
    for i in file.readlines():
        if(not(i[0] == "#")):
            lineasArchivoNuevo.append(i);
    file.close()

    for linea in lineasArchivoNuevo:
        archivoDestino.write(linea)
    
    archivoDestino.close()
    
    

print(clonarSinComentarios("archivoConComentarios.txt"))