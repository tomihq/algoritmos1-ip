{-RECURSIÓN + LISTAS.-}
{-Ejercicio 1. 1. Indicar la longitud de una lista. "Desestructuro" la cabeza por cada iteracion y voy sumando 1 y hago recursion en base a cola de la lista.-}
longitud :: [t] -> Integer 
longitud [] = 0
longitud (_:xs) = 1 + longitud xs

{-Ejercicio 1. 2, dada una secuencia con más de un elemento, obtener el último elemento de la lista. Voy utilizando recursividad hasta quedarme con la cola que tiene un elemento.-}
ultimo :: [t] -> t 
ultimo lista | longitud lista == 1 = head(lista)
             | otherwise = ultimo(tail(lista))

{- Ejercicio 1. 3, dada una secuencia, retornar una nueva secuencia de tipo t que vaya desde el indice 0 hasta el anterior a la longitud de la lista. Básicamente devuelvo una copia de la lista-}

principio :: [t] -> [t]
principio lista = subseq (lista) 0 (longitud lista - 1)

{- 
    Función subseq:
    requiere: |lista| > 0 
    Ejemplo: [1, 2, 3, 9] 
    asegura: {res será una lista vacía [] si indiceDesde es menor a 0}
    asegura: {res será una lista vacía [] si indiceHasta es mayor a la longitud de la lista menos uno.}
    asegura: {res será el primer elemento de la lista en caso de que indiceDesde e indiceHasta sean 0}
    asegura: {res será una sublista de lista que tendrá los elementos de lista desde indiceDesde hasta indiceHasta}

    Input: [1, 4, 8] 1 2 
    Output: [4, 8]

    Input: [] 1 2
    Output: []

    Input: [1, 3] 0 0
    Output: head([1, 3]) = [1]

    Input: [1, 5, 6, 2] 1 2 = Tomo la cabeza y creo una nueva lista utilizando el operador : que se genera al utilizar nuevamente la función subseq para continuar añadiendo el resto de los elementos hasta que se alcance el indiceHasta.
    Proceso: Si indiceDesde es distinto de cero, entonces significa que el primer elemento de la lista original no está en la subsecuencia que queremos construir. Por lo tanto, podemos ignorar el primer elemento y crear una nueva subsecuencia que incluya los elementos de la cola de la lista. La nueva subsecuencia tendrá una longitud de indiceHasta - indiceDesde, por lo que establecemos un nuevo indiceDesde de cero y un indiceHasta de indiceHasta - 1.

    Si indiceDesde es cero, entonces eso significa que queremos incluir el primer elemento de la lista original en la subsecuencia resultante. En este caso, se agrega head(lista) a la subsecuencia resultante y se hace una llamada recursiva a subseq con la cola de la lista y con un nuevo indiceDesde de cero y un indiceHasta de indiceHasta - 1.

    En cualquier caso, si indiceDesde es mayor que cero, se hace una llamada recursiva a subseq con la cola de la lista y con un nuevo indiceDesde y indiceHasta disminuidos en uno cada uno. En cada llamada recursiva, se sigue eliminando el primer elemento de la lista hasta que indiceDesde llega a cero, momento en el cual se comienza a agregar elementos a la subsecuencia resultante.
-}

subseq :: [t] -> Integer -> Integer -> [t]
subseq lista indiceDesde indiceHasta | indiceDesde < 0 || indiceHasta < 0 = []
                                     | indiceHasta > longitud(lista)-1 = []
                                     | indiceDesde == 0 && indiceHasta == 0 = [head(lista)]
                                     | indiceDesde == 0 = head(lista) : subseq (tail(lista)) 0 (indiceHasta-1)
                                     | otherwise = subseq (tail(lista)) (indiceDesde-1) (indiceHasta-1) 

{-Ejercicio 1. 4. Creo una función auxiliar que reciba como parámetro la lista original, la listaInvertida (vacia inicialmente). Si la lista original es vacia significa que listaInvertida ya tiene todos los valores de la lista original invertidos, caso contrario, llamo a reversoAux nuevamente pero coloco la cabeza d -}
reverso :: [t] -> [t]
reverso lista = reversoAux lista [] 

{-
    Proceso: Recibe una lista a invertir [1, 2] y una lista vacia por defecto.
    Quita la cabeza de la lista [1] y la agrega como elemento a la listaInvertida vacia [1]. Ahora ambas listas quedaron [2] y [1].
    Repite el proceso, y ahora de la lista original quita el elemento [2] y lo agrega al principio de la lista invertida [1] -> [2, 1].
    ¡Listo! Hay que recordar que aquí siempre tenemos que ir colocando los elementos adelante a medida que vamos iterando utilizando ":" que tiene como firma a -> [a] -> [a] el cual nos indica que a partir de un elemento, se lo enviamos a una lista y nos retorna una lista con el elemento de tipo a dentro de la lista de tipo [a].
-}
reversoAux :: [t] -> [t] -> [t]
reversoAux [] listaInvertida = listaInvertida
reversoAux (x:xs) listaInvertida = reversoAux xs (x:listaInvertida)

{-OTRA OPCION:
reverso :: [t] -> [t]
reverso [] = []
reverso (x:xs) = reverso(xs) ++ [x]  -> no me gusta la idea de aplicar siempre la recursion antes de dar un resultado (en la teorica se habia dicho primero operaciones y luego recursion nuevamente)
-}

{-Ejercicio 2. 1. Pertenece: Debo verificar si un valor pertenece a una secuencia ¿Voy validando si el elemento es igual a la cabeza de la lista, y si no pasa, entonces llamo nuevamente a recursion pero con la cola de la lista? 
Véase que por primera vez utilizamos  Eq t: Es una restricción de tipo que significa que el tipo t debe ser una instancia de la clase de tipos Eq lo cual significa que los valores de tipo t deben ser comparables por la igualdad con el operador "==" Por lo tanto podemos utilizar este operador.
-}
pertenece :: (Eq t) => t -> [t] -> Bool 
pertenece valorABuscar lista | longitud(lista) == 0 = False
                             | head(lista) == valorABuscar = True 
                             | otherwise = pertenece valorABuscar (tail lista) 

{-Ejercicio 2.2. Todos iguales: Que dada una lista devuelve verdadero sí y solamente sí todos sus elementos son iguales.
Una opción sería crear un Set (conjunto) pero hasta ahora no se "permitió" crear nuevos tipos.
Ej: [1, 3, 2, 4] -> como 1 es distinto a 3, entonces false.
Ej: [1, 1, 3, 1] -> como 1 es igual a 1, sigue, como 1 es distinto a 3 entonces retorno false. Tengo que iterar hasta el ultimo elemento de la lista, si la longitud de la lista original es 0 entonces retorno true.
Proceso:
Paso 1: Comparo el head = 1 con el ultimo de la cola de la lista 1. 1 = 1 entonces sigo
Paso 2: Comparo el head = 1 con el ultimo de la cola de la lista 1. 1 = 1 entonces sigo.
Paso 3: Comparo el head = 3 con el ultimo de la cola de la lista 1. 3 /= 1 entonces es False.
-}

todosIguales :: (Eq t) => [t] -> Bool
todosIguales lista | longitud(lista) <= 1 = True
                   | longitud(lista) /= 0 && head(lista) == ultimo(tail(lista)) = todosIguales (tail(lista))
                   | otherwise = False
{-
    Ejercicio 2.3. EXISTE un i j que pertenece a los enteros tal que i y j estan 0 y la longitud de la lista - 1.
    i != j pero el elemento en la lista en ambos indices son iguales.
    Por ejemplo: lista = [1, 2, 2]
    i = 1 (cabeza)
    j = 2 (ultimo de la cola)
    lista[i] == lista[j] -> 2 = 2 por lo tanto, al ser el mismo elemento en i y j, no son todosDistintos.
-}
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos lista | longitud(lista) == 1 = False
                     | longitud(lista) /= 0 && head(lista) /= ultimo(tail(lista)) = True
                     | otherwise = todosDistintos(tail(lista))

{-
    Ejercicio 2.4 hayRepetidos: Existe un i,j que pertenece a los enteros tal que i y j están entre 0 y la longitud de la lista -1.
    Si i != j pero en la lista tienen el mismo elemento entonces hayRepetidos.
-}

hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos lista | longitud(lista) == 1 = False
                   | longitud(lista) /= 0 && head(lista) == ultimo(tail(lista)) = True
                   | otherwise = hayRepetidos(tail(lista))

{-
    Ejercicio 2.6 quitarTodos: dada una lista xs y un elemento x, elimina la primera aparicion de x en la lista xs (de haberla).
    Tengo un elemento y una lista:
        Si la lista es vacia significa que no se encontró nunca el elemento. Retorno la misma lista original.
        Si el elemento es igual a la cabeza de la lista retorno una nueva lista en base a la cola de la lista y termino recursión.
        Caso contrario, quito la cabeza y vuelvo a hacer recursion.

        Ej: 2 [1, 2, 3] -> 2 es distinto que 1. 2 es igual a 1, por lo tanto retorno [1, 3]. listaAux es la misma lista original pero se le quita el elemento cuando son iguales. 
        Ej 2: 2 [2, 1, 3] -> 2 es igual a 2 por lo tanto devuelvo la cola. Listo.
        Ej 3: 3 [2, 1, 3] -> 3 es distinto de 2, 3 es distinto de 1, 3 es igual a 3, por lo tanto retorno la listaAux que tenia los mismos elementos que la original pero sin el ultimo que son iguales.
        Ej 4: 3 [3, 1, 3] -> retorno [1]
        
-}

quitarTodos  :: (Eq t) => t  -> [t] -> [t]
quitarTodos elemento lista = quitarAux elemento lista []

quitarAux :: (Eq t) => t -> [t] -> [t] -> [t]
quitarAux _ [] listaAux = listaAux
quitarAux elemento (x:xs) listaAux | x == elemento = quitarAux elemento xs listaAux
                                   | otherwise = quitarAux elemento xs (listaAux ++ [x])


{-
    Ejercicio 3.1 Sumatoria. Hacer una sumatoria de los valores de la lista.
-}

sumatoria :: [Integer] -> Integer 
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria(xs)

{-
    Ejercicio 3.2. Productoria
-}

productoria :: [Integer] -> Integer 
productoria [] = 1
productoria (x:xs) = x * productoria(xs)

{-
    Ejercicio 3.3 maximo de una lista.
    La lista debe tener minimo 1 elemento por lo tanto no hace falta verificarlo.
-}

{-
    Ejercicio 3.4 sumarN: Dado un n y una lista, sumar n a cada elemento de la lista.
-}

sumarN :: Integer -> [Integer]  -> [Integer]
sumarN n []   = []
sumarN n (x:xs) =  (x+n) : sumarN n xs 

{-
    Ejercicio 3.5 sumarElPrimero: Suma cada elemento de la lista con el primero de la lista original.
    Ej: [1, 2, 3] da como resultado [2, 3, 4]
-}

sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero lista = sumarElPrimeroAux lista (head(lista) )

sumarElPrimeroAux :: [Integer] -> Integer -> [Integer]
sumarElPrimeroAux [] _  = []
sumarElPrimeroAux (x:xs) primerElemento =  (x+primerElemento) : sumarElPrimeroAux xs primerElemento
                                     
{-
    Ejercicio 3.7. pares: De una lista quitar los impares.
    Voy haciendo una nueva lista una vez que encuentro el primer par.
-}

pares :: [Integer] -> [Integer]
pares (x:xs) | longitud(xs) == 0 = xs
             | mod x 2 == 0 = x : pares xs
             | otherwise = pares xs

{-
    Ejercicio 3.8. multiplosDeN: Dado un entero y una lista xs, devuelve una lista con los elementos de xs multiplos de n.
    Nos va a terminar retornando una lista que va acumulando los x que son multiplos de n.
-}

multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN n (x:xs) | longitud(xs) == 0 = xs
                      | mod x n == 0 = x : multiplosDeN n xs
                      | otherwise = multiplosDeN n xs
