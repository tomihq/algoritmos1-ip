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
#comensales = 4, min_cant_de_porciones = 5, se necesitan 20 porciones de pizza (5*4) = 20. ¿Cuantas pizzas necesito? Necesitaría= 24/3 pizzas par no estar justo, se agrega una pizza mas por si acaso.

##def cantidad_de_pizzas(comensales: int, min_cant_de_porciones: int) -> int:

def cantidad_de_pizzas(comensales: int, min_cant_de_porciones: int) -> int:
    return (comensales*min_cant_de_porciones/8)+1

#Ejercicio 3. Resuelva los siguientes ejercicios utilizando los operadores logicos and, or, not. Resolverlos sin utilizar el if.

#Ejercicio 3.1 alguno_es_0(numero1, numero2): Dados dos numeros racionales decide si alguno de los dos es igual a 0

def alguno_es_0(numero1: float, numero2: float) -> bool:
    return (numero1 == 0) or (numero2 == 0)

#Ejercicio 3.2: ambos_son_0 lo mismo que antes pero los dos iguales a 0.
def ambos_son_cero(numero1: float, numero2: float) -> bool:
    return (numero1 == 0) and (numero2 == 0)

#Ejercicio 3.3 es_nombre_largo dado un parámetro de entrada de tipo String que sea in, valida si la longitud del nombre esta entre 3 y 8 inclusive. 

def es_nombre_largo(nombre: str) -> bool:
    return (len(nombre)>=3 and len(nombre)<=8)

#Ejercicio 3.4 es_bisiesto(año) indica si un año tiene 366 dias. Recordar que un año es bisiesto si es multiplo de 400, o bien es multiplo de 4 pero no de 100.
def es_bisiesto(anio: str) -> bool: 
    return (es_multiplo_de(anio, 400) or (es_multiplo_de(anio, 4) and not(es_multiplo_de(anio, 100))))

"""
Ejercicio 4. Usar min y max. En una plantacion de pinos de cada arbol se conoce la altura expresada en metros. EL peso de un pino se pude estimar a partir de la altura d la siguiente manera:
  3kg por CADA CENTIMETRO hasta 3 metros.
  2kg por CADA CENTIMETRO arriba de los 3 metros.
Por ejemplo, 2 metros pesan 600kg porque 200 * 3 = 600
5 metros pesan 1300kg, porque los primeros 3 metros pesan 900kg y los siguientes pesan los 400 restantes.

Los pinos se usan para llevarlos a una fabrica de muebles a la que le sirvven arboles de entre 400 y 1000 kilos, un pino fuera de este rango NO sirve a la fabrica.
"""
def calcular_peso_pino(altura: int) -> int:
    if altura <= 3:
        peso = altura * 100 * 3  # altura en centímetros * 3 kg por cada centímetro
    else:
        peso_primeros_tres_metros = 3 * 100 * 3  # primeros 3 metros pesan 900 kg
        peso_adicional = (altura - 3) * 100 * 2  # peso adicional por cada centímetro arriba de los 3 metros
        peso = peso_primeros_tres_metros + peso_adicional
    
    return peso

def es_peso_util(peso: int) -> bool:
    return peso>=400 and peso <= 1000

def sirve_pino(altura: int) -> bool:
    return es_peso_util(calcular_peso_pino(altura))

ejercicio1 = raizDe2();
ejercicio1_2 = imprimir_hola();
ejercicio1_3 = imprimir_un_verso();
ejercicio1_4 = factorial_de_dos();
ejercicio1_5 = factorial_de_tres();
ejercicio1_6 = factorial_de_cuatro();
ejercicio1_7 = factorial_de_cinco();
ejercicioExtraFactorialGenerico = factorial_generico(5);
ejercicio2_1 = imprimir_saludo('Tomás');
ejercicio2_2 = raiz_cuadrada_de(49); #Expected 7.
ejercicio2_3 = imprimir_dos_veces('I wanna runnaway')
ejercicio2_4 = es_multiplo_de(4, 2);
ejercicio2_5 = es_par(1); #Expected False
ejercicio2_5_bis = es_par(2) #Expected True
ejercicio3_1 = alguno_es_0(0, 2) #Expected True.
ejercicio3_2 = ambos_son_cero(0, 0) #Expeted True - (0, 1) False, (2, 0) False.
ejercicio3_3 = es_nombre_largo('To') #Expected False
ejercicio3_3_1 = es_nombre_largo('Tom') #Expected True
ejercicio3_3_2 = es_nombre_largo('Tomas Tom') #Expected False
ejercicio3_3_3 = es_nombre_largo('Tomas T') #Expected True
ejercicio3_4 = es_bisiesto(2024) #Expected True
ejercicio3_4_2 = es_bisiesto(2016) #Expected True
ejercicio3_4_2 = es_bisiesto(2015) #Expected False
ejercicio4 = sirve_pino(2) #Expected True pues el peso del pino serian 600kg.
"""
Envio 4m.
Si cortamos la cuenta hasta los 3 metros que serian 300 cm deberiamos hacer 300 * 3 = 900kg.
nos quedan por calcular 1m, entonces 100 * 2 = 200kg

total 1100kg. ¿le sirve a la fabrica? no.
"""
ejercicio4_1 = sirve_pino(4) #Expected False
