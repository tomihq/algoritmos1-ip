"""
    Ejercicio 1. Codificar en Python las siguientes funciones sobre secuencias:

    problema pertenece (in s:seq<Z>, in e: Z) : Bool {
    requiere: { True }
    asegura: { res = true ↔ (∃i : Z)(0 ≤ i < |s| → s[i] = e)}
    }
    ¿Si la especificaramos e implementáramos con tipos genéricos, se podría usar esta misma función para buscar un caracter dentro de un string? Python en sí no tiene una forma de aceptar tipos genéricos.

    s y e son de tipo in porque nos interesa el valor que tienen ambos, pero no se modifican a la salida.

"""

def pertenece(s: list[int], e: int):
    for i in range(0, len(s)):
        if(s[i] == e): return True
    return False

lista: list[int] = [10, 20, 30, 40]
print(pertenece(lista, 30));

"""
   2. problema divideATodos (in s:seq<Z>, in e: Z) : Bool {
        requiere: {e != 0 }
        asegura: { res = true ↔ (∀i : Z)(0 ≤ i < |s| → s[i] mod e = 0)}
    }
"""

def divideATodos(s: list[int], e:int): 
    cantidadVecesQueDivide = 0;
    for i in range(0, len(s)):
        if(s[i] % e) == 0: cantidadVecesQueDivide+=1
    
    return (cantidadVecesQueDivide == len(s))

print(divideATodos(lista, 2));

"""
    3. problema sumaTotal (in s:seq<Z>) : Z {
        requiere: { True }
        asegura: { res es la suma de todos los elementos de s}
    }
    Nota: no utilizar la función sum() nativa
"""

def sumaTotal(s: list[int]):
    acum = 0;
    for i in range(0, len(s)):
        acum+=s[i]
    return acum;

print(sumaTotal(lista));

"""
    problema ordenados (in s:seq<Z>) : Bool {
        requiere: { True }
        asegura: { res = true ↔ (∀i : Z)(0 ≤ i < (|s|−1) → s[i] < s[i + 1]}
    }

    Para todos los elementos de la lista valida si el actual es menor que el siguiente.
    Si el actual es mayor que el siguiente retorno False (ya encontré una excepción), caso contrario, dejo que termine de recorrer y devuelvo True. Si no entró al caso False es porque no había ninguno
"""

def ordenados(s: list[int]):
    for i in range(0, len(s)):
        #Caso borde
        if(i == len(s)-1): return True
        elif(s[i]>s[i+1]):
            return False 

#Expected True.
listaOrdenada: list[int] = [10, 20, 30, 40]
print(ordenados(listaOrdenada));
#Expected False.
listaDesordenada: list[int] = [20, 10, 30, 40]
print(ordenados(listaDesordenada));
#Expected False.
listaDesordenada2: list[int] = [10, 20, 40, 30]
print(ordenados(listaDesordenada2));

"""
    5. Dada una lista de palabras, devolver verdadero si alguna palabra tiene longitud mayor a 7.
    res = True si y solo sí Existe una palabra perteneciente a la lista, que está dentro del rango de la lista 0<=i<=longitud(lista)-1 -> longitud(palabra[i])>7


"""

def hay_palabra_con_mas_de_7_letras(listaPalabras: list[str]):
    for i in range (0, len(listaPalabras)):
        if(len(listaPalabras[i])>7):
            return True; 
    return False

palabras: list[str] = ["h", "hola", "hola como andan"]
print(hay_palabra_con_mas_de_7_letras(palabras));
palabras2: list[str] = ["h", "hola", "hola"]
print(hay_palabra_con_mas_de_7_letras(palabras2));

"""
6. Dada una cadena de texto (string), devolver verdadero si esta es palíndroma (se lee igual en ambos sentidos), falso en caso contrario.

Es lo mismo que capicua. Hago el reverso de la string y si es exáctamente igual entonces es True.
"""

def reverso(palabra: str):
    return palabra[::-1]

def es_palindroma(palabra: str):
    return palabra == reverso(palabra)

#Expected True
print(es_palindroma('neuquen'))
#Expected True
print(es_palindroma('ana'))
#Expected False
print(es_palindroma('gasolina'))

