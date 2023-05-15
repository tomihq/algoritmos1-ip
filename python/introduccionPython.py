import math
#Ejercicio 1. 1: Devolver la raiz de 2 con 4 decimales
def raizDe2() -> float: 
    return round(math.sqrt(2), 4)

#Ejercicio 1. 2: imprimir_hola ---- Imprime hola por consola (es un procedimiento pues no modifica nada global ni tiene retorno)
def imprimir_hola() -> None:
    print('hola')


#Ejercicio 1. 3: imprimir_un_verso()
def imprimir_un_verso() -> None:
    print ('hola\nsoy yo!\ncomo estaaaan\n')

#Ejercicio 1. 4: factorial_de_dos
def factorial_de_dos() -> int:
    return 2 * 1

#Ejercicio 1. 5: factorial_de_tres
def factorial_de_tres() -> int:
    return 3 * 2 * 1

#Ejercicio 1. 6. factorial_de_cuatro
def factorial_de_cuatro() -> int:
    return 4 * 3 * 2 * 1

#Ejercicio 1. 7. factorial_de_cinco
def factorial_de_cinco() -> int:
    return 5 * 4 * 3 * 2 * 1

#Ejercicio extra factorial_generico (usando loops para prevenir que se supere la cantidad de memoria por recursividad)
def factorial_generico(n: int) -> int:
    factorialN: int = 1
    while(n>1):
        factorialN *= n
        n -= 1
    return factorialN

#Ejercicio 2. Definir las siguientes funciones y procedimientos con parametros
#Ejercicio 2.1 nombre es parametro String (in) por lo tanto entra pero no se modifica.
def imprimir_saludo(nombre: str) -> None: 
    print('Hola ' + nombre);

#Ejercicio 2.2 devuelve la raiz cuadrada de un numero n.
def raiz_cuadrada_de(numero: int) -> int:
    return math.sqrt(numero);

#Ejercicio 2.3 imprimir_dos_veces(estribillo) dado un string, que lo devuelva dos veces.
def imprimir_dos_veces(estribillo: str):
    return print(estribillo * 2)

#Ejercicio 2.4. es_multiplo_de() dado dos numeros n y m de tipos enteros que sean ambos (in) devolver si uno es multiplo del otro

def es_multiplo_de(n: int, m:int) -> bool:
    return n % m == 0

#Ejercicio 2.5 es_par() que indique si un numero es par, usar la funcion de es_multiplo_de
def es_par(numero: int)-> bool:
    return es_multiplo_de(numero, 2)

#Ejercicio 2.6 cantidad_de_pizzas(comensales, min_cant_de_porciones)
#Que devuelva la cantidad de pizzas que necesitamos para que cada comensal coma como minimo min_cant_de_porciones porciones de pizza. Considere que cada pizza tiene 8 porciones y que se prefiere que sobren porciones.
#comensales = 4, min_cant_de_porciones = 5, se necesitan 20 porciones de pizza (5*4) = 20. ¿Cuantas pizzas necesito? Necesitaría 3 pizzas pues 8 + 8 + 8 = 24 y 24 es mayor que 20.

##def cantidad_de_pizzas(comensales: int, min_cant_de_porciones: int) -> int:


ejercicio1 = raizDe2();
print(ejercicio1);
ejercicio1_2 = imprimir_hola();
ejercicio1_3 = imprimir_un_verso();
ejercicio1_4 = factorial_de_dos();
ejercicio1_5 = factorial_de_tres();
ejercicio1_6 = factorial_de_cuatro();
ejercicio1_7 = factorial_de_cinco();
ejercicioExtraFactorialGenerico = factorial_generico(5);
print(ejercicioExtraFactorialGenerico);
ejercicio2_1 = imprimir_saludo('Tomás');
ejercicio2_2 = raiz_cuadrada_de(49); #Expected 7.
print(ejercicio2_2)
ejercicio2_3 = imprimir_dos_veces('I wanna runnaway')
ejercicio2_4 = es_multiplo_de(4, 2);
print(ejercicio2_4)
ejercicio2_5 = es_par(1); #Expected False
print(ejercicio2_5)
ejercicio2_5_bis = es_par(2) #Expected True
print(ejercicio2_5_bis);