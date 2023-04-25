{-RECURSIÓN + LISTAS.-}
{-Ejercicio 1. Indicar la longitud de una lista. "Desestructuro" la cabeza por cada iteracion y voy sumando 1 y hago recursion en base a cola de la lista.-}
longitud :: [t] -> Integer 
longitud [] = 0
longitud (_:xs) = 1 + longitud xs

{-Ejercicio 2, dada una secuencia con más de un elemento, obtener el último elemento de la lista. Voy utilizando recursividad hasta quedarme con la cola que tiene un elemento.-}
ultimo :: [t] -> [t] 
ultimo lista | longitud lista == 1 = lista
             | otherwise = ultimo(tail(lista))
