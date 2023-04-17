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