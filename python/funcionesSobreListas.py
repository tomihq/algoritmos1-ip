"""
    Ejercicio 1. Codificar en Python las siguientes funciones sobre secuencias:

    problema pertenece (in s:seq<Z>, in e: Z) : Bool {
    requiere: { True }
    asegura: { res = true ↔ (∃i : Z)(0 ≤ i < |s| → s[i] = e)}
    }
    ¿Si la especificaramos e implementáramos con tipos genéricos, se podría usar esta misma función para buscar un caracter dentro de un string? Python en sí no tiene una forma de aceptar tipos genéricos.

    s y e son de tipo in porque nos interesa el valor que tienen ambos, pero no se modifican a la salida.

    22/5 se modificó el enunciado: Implementar al menos de 3 formas distintas éste problema

"""

def pertenece(s: list[int], e: int) -> bool:
    for i in range(0, len(s)):
        if(s[i] == e): return True
    return False

def pertenece_while(s: list[int], e: int) -> bool:
    index = 0;
    while(index < len(s)):
        if(s[index] == e): return True
        index+=1
    return False

def pertenece_recursividad(s: list[int], e:int) -> bool:
    if(len(s) == 0): return False
    elif(s[len(s)-1] == e): return True
    else: 
       s.pop()
       return pertenece_recursividad(s, e)



lista: list[int] = [10, 20, 30, 40]
print(pertenece(lista, 30)); 
print("pertenece_while: " + str(pertenece_while(lista, 30)))
print("pertenece_recursividad: " + str(pertenece_recursividad(lista, 30)))

"""
   2. problema divideATodos (in s:seq<Z>, in e: Z) : Bool {
        requiere: {e != 0 }
        asegura: { res = true ↔ (∀i : Z)(0 ≤ i < |s| → s[i] mod e = 0)}
    }
"""

def divideATodos(s: list[int], e:int) -> bool: 
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

def sumaTotal(s: list[int]) -> int:
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

def ordenados(s: list[int]) -> bool:
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

def hay_palabra_con_mas_de_7_letras(listaPalabras: list[str]) -> bool:
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

res = True <-> reverso(palabra) == palabra
"""

def reverso(palabra: str) -> str:
    return palabra[::-1]

def es_palindroma(palabra: str) -> bool:
    return palabra == reverso(palabra)

#Expected True
print(es_palindroma('neuquen'))
#Expected True
print(es_palindroma('ana'))
#Expected False
print(es_palindroma('gasolina'))

"""
    7. Analizar la fortaleza de una contraseña. El parámetro de entrada sería un string con la contraseña a analizar, y la salida
    otro string con tres posibles valores: VERDE, AMARILLA y ROJA. Nota: en python la “ñ/Ñ” es considerado un caracter especial y no se comporta como cualquier otra letra.
    
    La contraseña sería VERDE si:
        a) la longitud es mayor a 8 caracteres
        b) Tiene al menos 1 letra minúscula (probar qué hace "a"<="A"<="z")
        c) Tiene al menos 1 letra mayúscula Tiene al menos 1 letra minúscula (probar qué hace "A"<="A"<="Z"
        )
        d) Tiene al menos 1 dígito numérico (0..9) 
   
    La contraseña será roja si:
    a) la longitud es menor a 5 caracteres.
    
    En caso contrario será AMARILLA.

    El caso que evaluaré al principio será la longitud de la palabra, pues, es lo más corto y facil de validar.
    
    TODO: Investigar como en Python puedo validar si es minuscula o no sin utilizar funciones externas.
"""

"""
    ord('0') = 48
    ord('9') = 57
    ord('A') = 65
    ord('Z') = 90
    ord('Ñ') = 209
    ord('a') = 97
    ord('z') = 122
    ord('ñ') = 241
"""

"""
    limInf>= 48 && limInf<= 57 = Números
    limInf>= 65 && limInf<= 90 = Mayúsculas
    limInf>= 97 && limInf<= 122 = Minúsculas
    especial: ord(a) == 209 or ord(b) == 241
"""

def tiene_elemento(palabra: str, limInf: int, limSup: int) -> bool:
    index: int = 0;

    while(index<len(palabra)):
        if((ord(palabra[index])>=limInf and ord(palabra[index])<=limSup)): return True
        index+=1

    return False

def fortaleza_de_contraseña(contrasenia: str) -> str:
    if(len(contrasenia)<5): return 'ROJA'
    elif(
         len(contrasenia)>8 
         and tiene_elemento(contrasenia, 97, 122) 
         and tiene_elemento(contrasenia, 65, 90) 
         and tiene_elemento(contrasenia, 48, 57)
        ): return 'VERDE'
    else: return 'AMARILLA'

#Expected VERDE. (1 mayúscula, minúsculas y número y > 8 caracteres)
print(fortaleza_de_contraseña('Hola, como andan 1'))
#Expected ROJA (<5 caracteres)
print(fortaleza_de_contraseña('H1ña'))
#Expected AMARILLA (8 caracteres)
print(fortaleza_de_contraseña('Hola a1ñ'))
#TODO: Contemplar ñ. Ahora da amarilla porque no la contemplé
#print(fortaleza_de_contraseña('Ññññññññññ'))



"""
    8. Dada una lista de tuplas, que representa un historial de movimientos en una cuenta bancaria, devolver el saldo actual.
    Asumir que el saldo inicial es 0. Las tuplas tienen una letra que nos indica el tipo de movimiento “I” para ingreso de
    dinero y “R” para retiro de dinero, y además el monto de cada operación. 
    Por ejemplo [("I", 2000), ("R", 20),("R", 1000),("I", 300)] -> saldo = 1280.
"""
#Utilizo elif para evitar que me envien otra letra no reconocida y hacer una resta o suma cuando no corresponde.
def historial_movimientos(movimientos: list[(str, int)]):
    saldo = 0
    for i in range (0, len(movimientos)):
        if(movimientos[i][0] == 'I'): saldo += movimientos[i][1]
        elif(movimientos[i][0] == 'R'): saldo -= movimientos[i][1]
    return saldo

print(historial_movimientos([("I", 2000), ("R", 20),("R", 1000),("I", 300)]))

"""
    9. Recorrer una palabra y devolver True si ésta tiene al menos 3 vocales distintas. En caso contrario devolver False.

    1) Creo lista de qué letras son vocales.
    2) Creo lista para almacenar las vocales de la palabra (no se aceptan repetidas) por lo tanto, antes tengo que validar si pertenece.
    3) Si la cantidad de vocales es mayor o igual a 3, es true.
"""


def perteneceLetraALista(s: list[str], e: str) -> bool:
    for i in range(0, len(s)):
        if(s[i] == e): return True
    return False

vocales: list[str] = ["A", "E", "I", "O", "U"];
def tiene_al_menos_tres_vocales(palabra: str) -> bool:
    vocalesDePalabra: list[str] = [];
    for i in range (0, len(palabra)):
       if perteneceLetraALista(vocales, palabra[i].upper()) and not perteneceLetraALista(vocalesDePalabra, palabra[i].upper()):
        vocalesDePalabra.append(palabra[i].upper())

    return len(vocalesDePalabra)>=3

#Expected False.
print(tiene_al_menos_tres_vocales("Casa"))
#Expected True.
print(tiene_al_menos_tres_vocales("Murciélago"))
#Expected True.
print(tiene_al_menos_tres_vocales("Computadora"))

"""
    Ejercicio 2. Implementar las siguientes funciones sobre secuencias pasadas por parametro.
"""
"""
    1. Implementar una funcion que dada una lista de numeros, en las POSICIONES PARES borra el valor original y coloca un cero.
    (Véase que aquí estamos hablando de un parámetro in-out porque nos interesa su valor de entrada, y debemos modificarlo para la salida)
"""

def colocar_cero_en_posiciones_pares(lista: list[int]) -> list[int]:
    for i in range(0, len(lista)):
        if(i % 2 == 0):
            lista[i] = 0
    return lista

#Expected 0, 2, 0, 4, 0
print(colocar_cero_en_posiciones_pares([1, 2, 3, 4, 5,]))

"""
    2.Implementar la función del punto anterior pero esta vez sin modificar la lista original, devolviendo una nueva lista,
    igual a la anterior pero con las posiciones pares en cero. Nota: La lista sería de tipo in.

    Aquí, creo una variable que sea solamente de tipo out para retornar como respuesta.
"""

def colocar_cero_en_posiciones_pares_out(lista: list[int]) -> list[int]:
    copiaLista = lista.copy() #Otra opción podría ser llamar a una función que me extraiga los valores de la lista en esta nueva variable, recuerde NO HACER que copiaLista = lista  debido a que tendría la misma referencia en memoria, por lo tanto si modificamos una o la otra, se modifican ambas...
    for i in range(0, len(copiaLista)):
        if(i % 2 == 0):
            copiaLista[i] = 0
   
    return copiaLista

print(colocar_cero_en_posiciones_pares_out([1, 2, 3, 4, 5,]))

"""
3. Implementar una función que dada una cadena de texto de entrada (in) devuelva una cadena igual a la anterior, pero
sin las vocales. Nota: No agrega espacios, sino que borra la vocal y concatena a continuación.

Como la cadena original es in, debo crear otro parametro out que devuelva la lista modificada sin vocales.
"""

#Como no puedo usar uppercase ni lowercase...
def es_vocal(letra: str) -> bool:
    vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    cantBusquedas = 0;

    while(cantBusquedas<len(vocales)):
        if(letra == vocales[cantBusquedas]): 
            return True
        cantBusquedas+=1

    return False

def eliminar_vocales(palabra: str) -> str:
    palabraSinVocales = ""
    for i in range (0, len(palabra)):
        if(not(es_vocal(palabra[i]))):
            palabraSinVocales += palabra[i]
    return palabraSinVocales

print(eliminar_vocales("hola mundo"))