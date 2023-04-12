-- Ejercicio 1.a
f :: Integer -> Integer
f n | n == 1 = 8
    | n == 4 = 131
    | n == 16 = 16

-- Ejercicio 1.b
g :: Integer -> Integer
g n | n == 8 = 16
    | n == 16 = 4
    | n == 131 = 1

-- Ejercicio 1.ca. fog
h :: Integer -> Integer
--Opcion 1
h n = g (f n) -- El paréntesis nos sirve para indicarle a Haskell que si o si debe ejecutar f n para luego hacer la composición.
--Opcion 2
h n = (g.f) n --El "." sirve para componer dos funciones.

-- Ejercicio 1.cb gof
k:: Integer -> Integer
--Opcion 1
k n = f (g n)
--Opcion 2
k n = (f.g) n

-- Ejercicio 2.a. Cuando se envia un numero negativo debe ponerse en parentesis
absoluto :: Integer -> Integer
--Forma 1: absoluto n = abs n;
--Forma 2:
absoluto n | n > 0 = n
           | otherwise = -n

--Ejercicio 2.b 
maximoAbsoluto :: Integer -> Integer -> Integer
maximoAbsoluto n1 n2 | (abs n1 > abs n2) = abs n1 
                     | (abs n2 > abs n1) = abs n2 
                     | otherwise = abs(n1)

--Ejercicio 2.c
maximoEntreTres :: Integer -> Integer -> Integer -> Integer
maximoEntreTres n1 n2 n3 | (n1 > n2 && n1 > n3) = n1
                         | (n2 > n1 && n2 > n3) = n2 
                         | otherwise = n3


--Ejercicio 2.d. Sin pattern matching
algunoEsCero :: Float -> Float -> Bool
--algunoEsCero n1 n2 = n1 == 0 || n2 == 0

--Ejercicio 2.d. Con Pattern Matching
algunoEsCero 0 _ = True
algunoEsCero _ 0 = True
algunoEsCero _ _ = False

--Ejercicio 2.f 
mismoIntervalo :: Integer -> Integer -> Bool
mismoIntervalo n1 n2  | n1<=3 && n2<=3 = True
                      | (n1>3 && n2>3) && (n1<=7 && n2<=7) = True 
                      | n1>7 && n2>7 = True
                      | otherwise = False

--Ejercicio 2.g (sin utilizar funciones para crear sets y prevenir repetidos)
sumarDistintos :: Integer -> Integer -> Integer -> Integer 
sumarDistintos n1 n2 n3 | n1 == n2 = n1 + n3 
                        | n1 == n3 = n1 + n2 
                        | n2 == n3 = n2 + n1
                        | otherwise = n1 + n2 + n3

--Ejercicio 2.h
esMultiploDe :: Integer -> Integer -> Bool
esMultiploDe n1 n2 = mod n1 n2 == 0

{- Preguntar: Porque en especificacion utilizamos naturales (lo dice el enunciado), pero en el idioma "logico" no existen los naturales ni tampoco acá en programación. ¿Los pasamos a enteros en la especificacion tambien o como sería? -}
--Ejercicio 2.i (dividir un número por 10 y luego calcular su resto dará el último digito de la unidad) 4235 - 4235 / 10 = 423.5 / mod(423.5) = 5
digitoUnidades :: Integer -> Integer
digitoUnidades n1 =  mod n1 10

--Ejercicio 2.j
digitoDecenas :: Integer -> Integer
digitoDecenas n1 =  mod n1 100

--Ejercicio 3 -- TODO. Buscar si existe un k que haga la ecuacion = 0 siempre y cuando k no sea 0.
estanRelacionados :: Integer -> Integer -> Bool
estanRelacionados n1 n2 = n1 /=0 && n2 /= 0 && n1 * n1 + (n1*n2*(div (-n1) n2)) == 0

--Ejercicio 4.a Producto interno (producto escalar) entre dos tuplas RxR = R2. (1, 2) (3, 4) = 3 * 1 + 2 * 4 = 11. Preguntar como usar los reales en Haskell.
prodInt :: (Float, Float) -> (Float, Float) -> Float 
prodInt tuplaUno tuplaDos = (fst tuplaUno * fst tuplaDos) + (snd tuplaUno * snd tuplaDos)

{-Ejercicio 4.b. todoMenor: Decidir si toda coordenada de la primera tupla es menor que a la coordenada de la segunda tupla.-}
todoMenor :: (Float, Float) -> (Float, Float) -> Bool
todoMenor t1 t2 = fst t1 < fst t2 && snd t1 < snd t2 

--Ejercicio 4.c distanciaPuntos: Calcular la distancia entre dos puntos de R2
distanciaPuntos :: (Float, Float) -> (Float, Float) -> Float
distanciaPuntos t1 t2 = sqrt((fst t2 - fst t1)^2 + (snd t2 - snd t1)^2)

--Ejercicio 4.d sumaTerna: Dado una terna de enteros, calcular la suma de sus tres elementos (sumando uno a uno)
sumaTerna :: (Integer, Integer, Integer) -> Integer
--sumaTerna (x1, x2, x3) = x1 + x2 + x3

--Ejercicio 4.d sumaTerna: Lo mismo que arriba pero utilizando sumatoria.
sumaTerna (x1, x2, x3) = sum[actualNumber | actualNumber <-[x1, x2, x3]]

--Ejercicio 4.e sumarSoloMultiplos: Dada una terna de numeros enteros y un natural, calcula la suma de los elementos de la terna que son multiplos del numero natural.
sumarSoloMultiplos :: (Integer, Integer, Integer) -> Integer -> Integer
sumarSoloMultiplos (x, y, z) n = sum[actualNumber | actualNumber <- [x, y, z], esMultiploDe actualNumber n]

{-  
    Ejercicio 4.f posPrimerPar: Dada una terna de enteros, devuelve la posicion del primer numero par si es que hay alguno, y devuelve 4 si son todos impares. TODO: No se como acceder a los indices. REFACTORIZAR para evitar tantos guardas.
-}
posPrimerPar :: (Integer, Integer, Integer) -> Integer
posPrimerPar (x1, x2, x3) | mod x1 2 == 0 = 0
                          | mod x2 2 == 0 = 1
                          | mod x3 2 == 0 = 2
                          | otherwise = 4

{-
    -- Ejercicio 4.g crearPar: Crea un par a partir de sus dos componentes dados por separados (debe funcionar para elementos de cualquier tipo)
    PREGUNTAS: ¿Al momento de ingresar los valores de entrada, serán del mismo tipo genérico o serán distintos? Aquí consideraré que ambos pueden ser de distinto tipo, por ejemplo, crear una tupla que sea de char e integer, float y char, etc.
     Ej: 
        'h' 'k' => ('h', 'k')
        1 2 => (1, 2)
        'h' 1 => ('h', 1)
-}
crearPar :: tx -> ty -> (tx, ty)
crearPar c1 c2 = (c1, c2)

{-
    Ejercicio 4.h invertir:  invierte los elementos del par pasado como parámetro (debe funcionar para elementos de cualquier tipo).
    PREGUNTAS: ¿Al momento de ingresar los valores de entrada, serán del mismo tipo genérico o serán distintos? Aquí consideraré que ambos pueden ser de distinto tipo, por ejemplo, crear una tupla que sea de char e integer, float y char, etc.
    Ej: 
        'h' 'k' => ('k', 'h')
        1 2 => (2, 1)
        'h' 1 => (1, 'h')
-}
invertir :: tx -> ty -> (ty, tx)
invertir e1 e2 = (e2, e1)

-- Ejercicio 5 
esPar :: Integer -> Bool
esPar n = mod n 2 == 0

f2 :: Integer -> Integer
f2 n | n>7 = 2*n-1
     | otherwise = n^2

g2 :: Integer -> Integer
g2 n | esPar n = div n 2
     | otherwise = 3*n + 1

{-
    Básicamente se envian en orden cada valor de la tupla a las funciones f y g, y si los valores de n mutados con f son mayores a los de g vuelve true.
    Ej: (4, 4, 9)
        (16 > 2) && (16 > 2) && (17 > 28) -- Retornaría false.
    Ej 2: (1, 1, 1)
        (1 > 4) -- Como la primera no se cumple el resultado sería false. Haskell es perezoso y evalúa condición por condición de izquierda a derecha.
    Ej 3: (3, 1, 4)
        (9 > 10) -- Como la primera no se cumple el resultado sería false.
    Ej 4: (4, 4, 2)
        (16 > 2) && (16 > 2) && (4 > 1) -- Retornaría true. Todas se cumplen
-}
todosMenores :: (Integer, Integer, Integer) -> Bool
todosMenores (n1, n2, n3) = ((f2 n1 > g2 n1) && (f2 n2 > g2 n2) && (f2 n3 > g2 n3))

-- Ejercicio 6. Reutilizo esMultiploDe
bisiesto :: Integer -> Bool
bisiesto anio | (not (esMultiploDe anio 4) || ((esMultiploDe anio 100) && (not (esMultiploDe anio 400)))) = False
              | otherwise = True

{- 
    Ejercicio 7. distanciaManhattan. Recibo dos ternas de floats y retorno el valor absoluto de otro float (IMPORTANTE LO ULTIMO porque puede dar negativo y las distancias siempre son positivas). Reutilizo absoluto.
    Preguntar: ¿Como haría para poder iterar las ternas sin tener que "separar la terna" en 3 fijamente? En este ejemplo si o si nos especifican que nos mandaran 3 valores por lo tanto sería innecesario pensar que podrían ingresar más, pero para saber :p
-} 

distanciaManhattan :: (Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattan (p1, p2, p3) (q1, q2, q3) = abs((p1 - q1) + (p2 - q2) + (p3 - q3))

{-
    Ejercicio 8: Preguntar que significa el símbolo de "≺" NO es el simbolo de menor.
-}