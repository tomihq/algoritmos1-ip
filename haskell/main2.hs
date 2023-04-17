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