{- Ejercicio 1: Secuencia de Fibonacci. Mando n = 3 -> fib(3-1) + fib(3-2) -> fib(2) + fib(1)-> fib(2-1) + 1 => 1 + 1 = 2 -}

fib :: Integer -> Integer
fib n | n == 0 = 0
      | n == 1 = 1
      | otherwise = fib(n-1) + fib(n-2);

fibonacci :: Integer -> Integer
fibonacci n = fib n

