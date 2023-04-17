{- Ejercicio 1: Secuencia de Fibonacci. Mando n = 3 -> fib(3-1) + fib(3-2) -> fib(2) + fib(1)-> fib(2-1) + 1 => 1 + 1 = 2 -}

fib :: Integer -> Integer
fib n | n == 0 = 0
      | n == 1 = 1
      | otherwise = fib(n-1) + fib(n-2);

fibonacci :: Integer -> Integer
fibonacci n = fib n

{-Ejercicio 2. 
    4.82 -> 3.82 -> 2.82 -> 1.82 -> 0.82 entonces como es menor que 1 sumo 0.
    -4.5 -> 1 + parteEntera(-4.5 + 1) => 1 + parteEntera(-5.5)
-}

parteEntera :: Float -> Integer
parteEntera n | (n>=0 && n<1) || (n > -1 && n<=0) = 0
              | n >= 1 = 1 + parteEntera(n-1)
              | n <= 1 = -1 + parteEntera(n+1)

{- Ejercicio 3. Dados dos numeros naturales determine si el primero es divisile por el segundo. No esta permitido utilizar mod ni div. 
-- no es divisible -> 9 2 -> 9 - 2 -> 7 - 2 -> 5 - 2 -> 3 - 2 -> 1. Al no ser 0 no es divisible.
-- no es divisible -> 9 5 -> 9 - 5 -> 4 - 5 -> Como x<y entonces no es divisible.
-- es divisible -> 10 5 -> 10 - 5 -> 5 - 5 -> Como quedó x-y == 0 entonces es divisible.
-- es divisible -> 4 1 -> 4 - 1 -> 3 - 1 -> 2 - 1 -> 1 - 1 -> como quedó x-y == 0 entones es divisible.
-}

esDivisible :: Integer -> Integer -> Bool
esDivisible x y | (x < y) && (x > 0) = False
                | (x-y == 0) = True
                | otherwise = esDivisible (x-y) y

{- Ejercicio 4. Sumar los impares hasta n. Entrada 5 entonces -> 1 + 3 + 5 + 7 + 9 = 25
-}

sumaImpares :: Integer -> Integer
sumaImpares n | n == 0 = 0
              | otherwise = 2*n-1 + sumaImpares(n-1)

{- Ejercicio 5. Dado un entero calcula n!! = n(n-2)(n-4) -> n = 10 salida 3840 -}
medioFac :: Integer -> Integer
medioFac n | n == 0 = 1
           | n < 0 = 0
           | otherwise = n * medioFac(n-2)

-- Ejercicio 6. Sumar digitos de un número natural, utilizar mod y div.
sumaDigitos :: Integer -> Integer
sumaDigitos n | n < 10 = n
              | otherwise = mod n 10 + sumaDigitos(div n 10)

-- Ejercicio 7. todosDigitosIguales, determina si todos los digitos de un número natural son iguales. 111 true 112 false

todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n | n < 10 = True  
                      | (decena n == unidad n) = todosDigitosIguales(digitoSinUnidad n)
                      | otherwise = False

decena :: Integer -> Integer
decena n = unidad (digitoSinUnidad n)

unidad :: Integer -> Integer
unidad n = mod n 10

digitoSinUnidad :: Integer -> Integer
digitoSinUnidad n = div n 10

{- 
Ejercicio 8 iesimoDigito - Recibe 2 enteros y retorna 1 entero que dado un n que pertenezca a los naturales y un i perteneciente a los naturales menor o igual a la cantidad de ditios de n, devuelve el iesimo digito de n.
Por ejemplo: n: 2543 -> i: 3 -> 4
-}

iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i | i == cantDigitos n = unidad n 
                 | otherwise = iesimoDigito (div n 10) i 

cantDigitos :: Integer -> Integer
cantDigitos n | n < 10 = 1 
              | otherwise = 1 + cantDigitos (div n 10)


