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

--Ejercicio 2.i (dividir un número por 10 y luego calcular su resto dará el último digito de la unidad) 4235 - 4235 / 10 = 423.5 / mod(423.5) = 5
digitoUnidades :: Integer -> Integer
digitoUnidades n1 =  mod n1 10

--Ejercicio 2.j
digitoDecenas :: Integer -> Integer
digitoDecenas n1 =  mod n1 100

--Ejercicio 3 -- TODO. Buscar si existe un k que haga la ecuacion = 0 siempre y cuando k no sea 0.
--estanRelacionados :: Integer -> Integer -> Bool
--estanRelacionados n1 n2 = (n1 * n1) + (n1 * n2 * k) == 0

--Ejercicio 4.a Producto interno (producto escalar) entre dos tuplas RxR = R2. (1, 2) (3, 4) = 3 * 1 + 2 * 4 = 11. Preguntar como usar los reales en Haskell.
prodInt :: (Float, Float) -> (Float, Float) -> Float 
prodInt tuplaUno tuplaDos = (fst tuplaUno * fst tuplaDos) + (snd tuplaUno * snd tuplaDos)

{-Ejercicio 4.b. todoMenor: Decidir si toda coordenada de la primera tupla es menor que a la coordenada de la segunda tupla.-}
todoMenor :: (Float, Float) -> (Float, Float) -> Bool
todoMenor t1 t2 = fst t1 < fst t2 && snd t1 < snd t2 