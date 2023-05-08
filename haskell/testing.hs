--Ejercicio 1.
--1. ¿Cual es el objetivo de realizar testing de un software?
--El objetivo de realizar testing de un software es validar que el software esté bien escrito y cumpla la especificación dada utilizando un Test Suite o conjunto de casos de prueba. Si bien el testing no nos garantiza la ausencia de errores, nos ayuda a poder validar si el software cumple con lo pedido.
--2. ¿Realizar testing sobre un software nos demuestra que el software funciona correctamente? Justificar.
--No. El testing no nos ayuda a probar que el software funciona bien para el 100% de los casos pues no podemos cubrir todo el dominio de entrada con casos test, sino que nos ayuda a testear casos particulares debido a que testear no justifica la ausencia de errores sino el funcionamiento de los casos de prueba particulares.
--3. ¿En que consiste el testing de caja negra? ¿Cual es su principal caracteristica? 
--El testing de caja negra es aquel que armamos el Test Suite en base a la especificación dada en base a un problema planteado específico. 
--4. ¿Se puede realizar testing de caja negra sin contar con una especificación del programa a testear? Justificar.
--No. No es posible pues el testing de caja negra se hace en base a la especificación del problema.

--Ejercicio 2. Pensando en el test de caja negra utilizando el método de partición por categorías de un programa que, dados tres enteros que se interpretan como la longitud de cada uno de los lados de un triángulo, dice si el triángulo resultante es isósceles, escaleno o equilátero. Tener en cuenta que para que un triangulo sea factible, la suma de dos de sus lados debe ser mayor a la longitud del tercer lado.

--1. Indicar cuales son los factores del programa
--Los factores del problema son los parámetros del problema a testear. En este caso son tres enteros el cual cada uno de los enteros se interpretan como cada uno de los lados de un triangulo. 
--2. ¿Existen Factores que son relaciones entre otros Factores? ¿Cuáles?
--Sí, existen. El factor que existe es que para que el triangulo sea factible, la suma de dos lados debe ser mayor a la longitud del tercer lado (el triángulo es válido). Es importante destacar, que dentro de cuando el tríangulo es válido tengo 3 casos más para probar. Seria como un subconjunto de tests del test más grande que indica que el triángulo es válido.
--1 seria que el triangulo sea válido y sea equilatero.
--2 seria que el triangulo sea válido y sea escaleno.
--3 seria que el triangulo sea válido y sea isosceles.

--Ejercicio 6. Diseñar los casos de test de caja negra utilizando el método de partición por categorı́as para los siguientes problemas

--1. multiplosDeN :: Integer -> [Integer] -> [Integer] que dado un número n y una lista xs, devuelve una lista con los elementos de xs múltiplos de n. (Ej 3.8 de la Guía 5)
module MultiplosDeN where 
multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN _ [] = []
multiplosDeN n (x:xs) | (mod x n) == 0 = x:multiplosDeN n xs
                      | otherwise = multiplosDeN n xs
