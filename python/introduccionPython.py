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

"""
Ejercicio 5.1 Si el numero es par devolver el doble, caso contrario, retornar el mismo numero.
"""
def devolver_el_doble_si_es_par (n: int) -> int:
    if(es_par(n)):
        return n * 2
    return n

"""
Ejercicio 5.2: Devolver el mismo numero si es par, mientras que si NO es par retornar el que le sigue.
    Analizar distintas formas de implementación (usando un
    if-then-else, y 2 if), ¿todas funcionan?

    Sí, todas funcionan, pero el comportamiento no es el mismo.
    Si usamos un if if siempre entrará a ambos.
    Si usamos un if else if, entrará al primero (si se cumple la condicion) sino, verifica si se cumple la segunda condicion, si se cumple la segunda condicion hace lo que tenga que hacer pero si no, debe entrar a un else.
    Si usamos un if else hay solo dos opciones, o entra a la primera condicion o cae si o si en la segunda (else)

    En este caso, como solo tenemos dos opciones (que sea par o no) nos basta con un if else.
"""

def devolver_valor_si_es_par_sino_el_que_sigue(n: int) -> int:
    if(es_par(n)):
        return n
    else:
        return n+1

"""
    Ejercicio 5.3
    devolver el doble si es multiplo3 el triple si es multiplo9(un numero). En otro caso devolver el número original. Analizar distintas formas de implementación (usando un if-then-else, y 2 if, usando alguna opción de operación
    lógica), ¿todas funcionan?.
    Si es multiplo de 3 devuelvo num * 2
    Si es multiplo de 9 devuelvo num * 3
    Caso contrario, devuelvo el numero original.
    Si es multiplo de 9, también es múltiplo de 3. Por lo tanto, priorizo este caso del 9 por encima del 3.

    Aquí, nos sirve un if, else if, y un else pues tenemos 3 casos a evaluar (por separado, no puede entrar a los 3)
    Si solo usamos if else nos faltaría un caso.
"""
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo_9(n: int) -> int:
    if(es_multiplo_de(n, 9)):
        return n * 3
    elif(es_multiplo_de(n, 3)):
        return n * 2
    else:
        return n

"""
Ejercicio 5.4:
Dado un nombre, si la longitud es igual o mayor a 5 devolver una frase que diga "Tu nombre tiene muchas letras!" y
sino, "Tu nombre tiene menos de 5 caracteres".
"""

def retornar_frase_segun_longitud_nombre(nombre: str) -> str:
    if(len(nombre)>=5):
        return "Tu nombre tiene muchas letras"
    else:
        return "Tu nombre tiene menos de 5 caracteres"
    
"""
Ejercicio 5.5: En Argentina una persona del sexo femenino se jubila a los 60 años, mientras que aquellas del sexo masculino se jubilan
a los 65 años. Quienes son menores de 18 años se deben ir de vacaciones junto al grupo que se jubila. Al resto de
las personas se les ordena ir a trabajar. Implemente una función que, dados los parámetros de sexo (F o M) y edad,
imprima la frase que corresponda según el caso: “Andá de vacaciones” o “Te toca trabajar”.
Si es sexo femenino y tiene 60 años entonces se va de vacaciones "Andá de vacaciones".
Si es sexo masculino y tiene 65 años entonces se va de vacaciones "Andá de vacaciones".
Si es menor a 18 años se deben de ir de vacaciones "Andá de vacaciones".
Caso contrario, "te toca trabajar"
"""

def que_corresponde(sexo: str, edad: int):
    if(edad<18):
        return "Andá de vacaciones"
    elif((sexo == 'M' and edad >= 65) or (sexo == 'F' and edad >= 60)):
        return "Andá de vacaciones"
    else: 
        return "Te toca trabajar"

""" 
 Utilizando While, en todo el ejercicio 6...
 Ejercicio 6.1: Escribir una función que imprima los números del 1 al 10.
"""

def imprimir_numeros_1_al_10() -> None:
    n = 1
    while(n<=10):
        print(n)
        n+=1

"""
    Ejercicio 6.2: Escribir una función que imprima los números pares entre el 10 y el 40.
"""

def escribir_numeros_pares_desde_10_hasta_40() -> None:
    n = 10
    while(n<=40):
        if(es_par(n)):
            print(n)
        n+=1
"""
    Ejercicio 6.3: Escribir una función que imprima la palabra “eco” 10 veces.
"""

def imprimir_eco_10_veces() -> None:
    n = 1
    while(n<=10):
        print('eco')
        n+=1

"""
    Ejercicio 6.4: Escribir una funcion de cuenta regresiva para lanzar un cohete. Dicha función irá imprimiendo desde el número que me pasan por parámetro (que sería positivo) hasta el 1, y por ultimo “Despegue”.
"""

def cuenta_regresiva(n: int) -> None:
    while(n>=1):
        print(n)
        if(n==1):
            print("Despegue")
        n-=1

"""
    Ejercicio 6.5: Hacer una función que monitoree un viaje en el tiempo. Dicha función recibe dos parámetros, “el año de partida” y “algún año de llegada”, siendo este último parámetro siempre más chico que el primero. El viaje se realizará de a saltos de un año y la función debe mostrar el texto: “Viajó un año al pasado, estamos en el año: <año>” cada vez que se realice un salto de año.

    Volver al pasado.
"""

def viaje_en_el_tiempo(anioDePartida: int, anioDeLlegada: int) -> None:
    while(anioDePartida>anioDeLlegada):
        anioDePartida-=1
        print("Viajó un año al pasado, estamos en el año: " + str(anioDePartida))

"""
    Ejercicio 6.6: Implementar de nuevo la función de monitoreo de viaje en el tiempo, pero desde el año de partida hasta lo más cercano al 384 a.C., donde conoceremos a Aristóteles. Y para que sea mas rapido el viaje, ¡vamos a viajar de a 20 años en cada salto!
"""

def viaje_en_el_tiempo_ac(anioDePartida: int, anioDeLlegada: int) -> None:
    while(anioDePartida>anioDeLlegada):
        anioDePartida-=20
        print("Viajó un año al pasado, estamos en el año: " + str(anioDePartida))

"""
Ejercicio 7. Lo mismo que los del 6 pero con for.
Recordar que el inrange es de esta forma [1, 11) por lo tanto acá iria desde el 1 hasta el 10 pues, el 11 no está incluido
"""
        
def imprimir_numeros_1_al_10_for() -> None:
    for num in range(1, 11):
        print(num)

def escribir_numeros_pares_desde_10_hasta_40_for() -> None:
    for n in range (10, 41):
        if(es_par(n)):
            print(n)

def imprimir_eco_10_veces() -> None:
    for n in range (1, 11):
        print('eco')

def cuenta_regresiva_for(n: int) -> None:
    for n in range(n, 0, -1):
        print(n)
        if(n==1):
            print("Despegue")


def viaje_en_el_tiempo_for(anioDePartida: int, anioDeLlegada: int) -> None:
    for anio in range(anioDePartida-1, anioDeLlegada-1, -1):
        print("Viajó un año al pasado, estamos en el año: " + str(anio))



ejercicio1 = raizDe2()
ejercicio1_2 = imprimir_hola()
ejercicio1_3 = imprimir_un_verso()
ejercicio1_4 = factorial_de_dos()
ejercicio1_5 = factorial_de_tres()
ejercicio1_6 = factorial_de_cuatro()
ejercicio1_7 = factorial_de_cinco()
ejercicioExtraFactorialGenerico = factorial_generico(5)
ejercicio2_1 = imprimir_saludo('Tomás')
ejercicio2_2 = raiz_cuadrada_de(49); #Expected 7.
ejercicio2_3 = imprimir_dos_veces('I wanna runnaway')
ejercicio2_4 = es_multiplo_de(4, 2)
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
ejercicio5_1 = devolver_el_doble_si_es_par(4) #Expected 4.
ejercicio5_2 = devolver_valor_si_es_par_sino_el_que_sigue(3) #Expected 4
ejercicio5_3 = devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo_9(6) #Expected 12
ejercicio5_3_2 = devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo_9(9) #Expected 27
ejercicio5_3_3 = devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo_9(14) #Expected 14
ejercicio5_4 = retornar_frase_segun_longitud_nombre('Tomás Hernández') #Expected "Tu nombre tiene muchas letras"
ejercicio5_4_1 = retornar_frase_segun_longitud_nombre('Tom') #Expected "Tu nombre tiene menos de 5 caracteres"
ejercicio5_5 = que_corresponde("M", 17) #Expected "Andá de vacaciones"
ejercicio5_5_2 = que_corresponde("M", 60) #Expected "Te toca trabajar"
ejercicio5_5_3 = que_corresponde("M", 65) #Expected "Andá de vacaciones"
ejercicio5_5_4 = que_corresponde("F", 60) #Expected "Andá de vacaciones"
ejercicio5_5_5 = que_corresponde("F", 55) #Expected "Te toca trabajar"
ejercicio6_1 = imprimir_numeros_1_al_10();
ejercicio6_2 = escribir_numeros_pares_desde_10_hasta_40();
ejercicio6_3 = imprimir_eco_10_veces();
ejercicio6_4 = cuenta_regresiva(10);
ejercicio6_5 = viaje_en_el_tiempo(2016, 2010)
ejercicio6_6 = viaje_en_el_tiempo_ac(2023, 384)
ejercicio7_1 = imprimir_numeros_1_al_10_for();
ejercicio7_2 = escribir_numeros_pares_desde_10_hasta_40_for();
ejercicio7_3 = cuenta_regresiva_for(15)
ejercicio7_4 = viaje_en_el_tiempo_for(2016, 2010)
ejercicio7_5 = viaje_en_el_tiempo_ac_for(2023, 384)