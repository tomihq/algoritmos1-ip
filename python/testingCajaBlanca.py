#No es necesario codear todo esto, pero quiero validar mis tests.

def triangle(a: int, b: int, c: int) -> int:
    if(a <= 0 or b <= 0 or c <= 0):
        return 4 #invalido
    if(not((a+b > c) and (a+c > b) and (b+c>a))):
        return 4 #invalido
    if(a == b and b == c):
        return 1 #equilatero
    if(a == b or b == c or a == c):
        return 2 #isosceles
     
    return 3

""" #Expected 4.
print(triangle(0, 1, 2))
#Expected 4.
print(triangle(1, 1, 2))
#Expected 1.
print(triangle(1, 1, 1))
#Expected 2.
print(triangle(2, 1, 2))
#Expected 3.
print(triangle(4, 2, 3))

 """

##EJERCICIO 17 -> Luego de haber resuelto los tests en papel, los plasmo aquí para dejar registro y ver si solución funciona.
def calcular_fragmento_mas_largo(s: str) -> int: 
    n = 0
    i = 0
    f = 0
    while(i<len(s)):
        if(f>n):
            n = f
        if(s[i] == ";"):
            f = 0
        else: 
            f+=1
        i+=1
    return n

#Según la especificacion, deberia retornar la palabra con mas letras pero parece haber un problema siempre en la ultima iteración (cuando la palabra mas larga está luego del último pues la última letra del fragmento no es leída por el ciclo.;)

#Expected: 1, Got: 1
print(calcular_fragmento_mas_largo("T;"))

#Expected 2 - Got: 1 
print(calcular_fragmento_mas_largo("T;TO"));
"""
Recorre hasta i = 3 pues recorre cuando i<len(T;TO)
Primera ejecución: n = 0 f = 0 i = 0 -> n = 0 f = 1 i = 1
Segunda ejecución: n = 0 f = 1 i = 1 -> n = 1 f = 0 i = 2
Tercera ejecución: n = 1 f = 0 i = 2 -> n = 1 f = 1 i = 3
Cuarta ejecucion: n = 1 f = 1 i = 3 -> n = 1 f = 2 i = 4
Podemos observar, que el problema es que se compara f = 1 con n = 1 y jamas entra pues 1 no es mayor que 1.

Entonces, concluimos que el problema siempre toma la palabra anterior al punto y coma aunque la de la derecha sea mas larga.
Esto se arreglaría añadiendo el primer if al final, luego de incrementar f por 1 si sigue en la misma palabra.
"""
#Expected 3 - Got: 2
print(calcular_fragmento_mas_largo("T;TO;TOM"))

"""
    Misma función, pero sin defectos:
"""

def calcular_fragmento_mas_largo_func(s: str) -> int: 
    n = 0
    i = 0
    f = 0
    while(i<len(s)):
        if(s[i] == ";"):
            f = 0
        else: 
            f+=1
        if(f>n):
            n = f
        i+=1
    return n


#Expected: 1, Got: 1
print(calcular_fragmento_mas_largo_func("T;"))

#Expected: 2, Got: 2
print(calcular_fragmento_mas_largo_func("T;TO"))

#Expected: 3, Got: 3
print(calcular_fragmento_mas_largo_func("T;TO;TOM"))
