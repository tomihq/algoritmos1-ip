"""
    Ejercicio 1. Codificar en Python las siguientes funciones sobre secuencias:

    problema pertenece (in s:seq<Z>, in e: Z) : Bool {
    requiere: { True }
    asegura: { res = true ↔ (∃i : Z)(0 ≤ i < |s| → s[i] = e)}
    }
    ¿Si la especificaramos e implementáramos con tipos genéricos, se podría usar esta misma función para buscar un caracter dentro de un string? Python en sí no tiene una forma de aceptar tipos genéricos.

    s y e son de tipo in porque nos interesa el valor que tienen ambos, pero no se modifican a la salida.

    2. problema divideATodos (in s:seq<Z>, in e: Z) : Bool {
        requiere: {e != 0 }
        asegura: { res = true ↔ (∀i : Z)(0 ≤ i < |s| → s[i] mod e = 0)}
    }
"""

def pertenece(s: list[int], e: int):
    for i in range(0, len(s)):
        if(s[i] == e): return True
    return False

lista: list[int] = [10, 20, 30, 40]
print(pertenece(lista, 30));

def divideATodos(s: list[int], e:int): 
    cantidadVecesQueDivide = 0;
    for i in range(0, len(s)):
        if(s[i] % e) == 0: cantidadVecesQueDivide+=1
    
    return (cantidadVecesQueDivide == len(s))

print(divideATodos(lista, 2));

