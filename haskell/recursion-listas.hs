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

{-Ejercicio 2.5 quitar: Dada una lista xs y un elemento x, elimina la primera aparicion de x en la lista xs (corto recursividad cuando lo encuentra). Retorno, el elemento si se encuentra será la cabeza por lo tanto deberia ir creando una nueva lista con cada elemento y cuando coincide el que busco NO lo agrego sino que devuelvo la lista realizada hasta ese momento + la cola.
[1, 3, 2, 2, 4, 4, 5] -> a eliminar el numero 2.
[1, 3, 2, 2, 4, 4, 5] -> no hace nada pues 2 != 1 -> [1]
[1, 3, 2, 2, 4, 4, 5] -> no hace nada pues 2 != 3 -> [1, 3]
[1, 3, 2, 4, 4, 5] -> al ser 2 = 2 entonces retorno la lista armada hasta ese momento [1, 3] + la cola [2, 4, 4, 5].

En cada llamada recursiva de la función quitar, se construye una nueva lista que comienza con el valor actual de x (siempre que x no sea igual a elem, en cuyo caso no se agrega x a la lista resultante) y luego se agrega la cola de la lista modificada. De esta forma, se va construyendo una nueva lista a partir de la original, en la que se eliminó la primera aparición de elem.

-}
quitar :: Eq(t) => t -> [t] -> [t]
quitar _ []  = []
quitar elem (x:xs)  | x == elem = xs
                    | otherwise = x : quitar elem xs 

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

{-Ejercicio 2.7: eliminarRepetidos: Deja una lista una unica aparicion de cada elemento, eliminando las repeticiones adicionales.
Lo que puedo hacer es que cada elemento que elimino por completo (quitarTodos) lo agrego una vez.
Por cada elemento que tiene la lista, llamo a eliminarRepetidos con quitarTodos.
-}

eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) = [x] ++ eliminarRepetidos(quitarTodos x xs)

{-Ejercicio 2.8: mismosElementos
Retorna verdadero sí y solamente ambasl istas contienen los mismos elementos.
1) Valido eliminando TODOS LOS repetidos, si una lista es mas grande que otra, entonces significa que no tienen los mismos elementos.
2) Valido si el elemento de la lista 1 está en la lista 2 y viceversa.
3) Si solo tienen dos elementos, entonces comparo solo sus cabezas.
Entrada: [3, 1, 3] y [2, 4, 5] retornará false pues al llamar a eliminarRepetidos queda [3,1] y [2, 4, 5] y no tienen la misma longitud. = False.
Entrada2:  [1, 1, 3] y [3, 3, 1] retornará true pues a llamar eliminarRepetidos queda [1, 3] y [3, 1] y ambos listas tienen los mismos elementos
Entrada3: [1,2,3] [3,2,1] -- devuelve True
Entrada4: [1,2,3] [1,2,3,4] -- devuelve False
Entrada5: [1,1,2,3] [1,2,3] -- devuelve True
Entrada6: "abc" "cab" -- devuelve True
Entrada7: "abc" "cba" -- devuelve True

OJO CON IR quitando la cola de la otra lista porque de esta forma puede ser que la lista no tenga el mismo orden y jamas encuentre al elemento
-}

mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos lista1 lista2 | longitud(eliminarRepetidos lista1) == longitud(eliminarRepetidos lista2) = mismosElementosAux lista1 lista2 
                              | otherwise = False

mismosElementosAux :: (Eq t) => [t] -> [t] -> Bool
mismosElementosAux [] _ = True
mismosElementosAux (x:xs) lista2 | pertenece x lista2 = mismosElementosAux xs lista2
                                 | otherwise = False

{-Ejercicio 2.9. capicua: Si una lista es capicua retorno True 
Ej: neuquen, acbbca, anna, otto, mom, arenera
-}

capicua :: (Eq t) => [t] -> Bool
capicua lista = lista == reverso(lista) 

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
    Recursividad debe ser llamada para comparar x con el otro valor.

    Comparar x con todos los elementos de la lista, hasta que llego a una lista de tipo [x] que me devuelve x, es decir para
    [4,2,3] el programa haria 4 > maximo([3,2]) -> 4 > 2 > maximo([3]) -> 4 > 2 > 3 y no sigue preguntando pues el caso base es que la lista retorne un elemento.
-}

maximo :: [Integer] -> Integer
maximo [x] = x
maximo (x:xs) | x>=maximo(xs) = x
              | otherwise = maximo(xs)

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
    Ejercicio 3.6 sumarElUltimo: Lo mismo que el de arriba pero con el ultimo. Reutilizo la funcion ultimo que hice hace un tiempo
-}
sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo lista = sumarElUltimoAux lista (ultimo lista)

sumarElUltimoAux :: [Integer] -> Integer -> [Integer]
sumarElUltimoAux [] _  = []
sumarElUltimoAux (x:xs) ultimoElemento =  (x+ultimoElemento) : sumarElUltimoAux xs ultimoElemento
                                     
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


{-
Ejercicio 4.1: sacarBlancosRepetidos: Reemplaza cada subsecuencia de blancos contiguos de la primera lista por un solo blanco en la segunda lista.
Ej: "Hola                 Mundo" - Se le quitan todos los espacios demás y deja uno solo Hola Mundo
Ej 2:"                    a" - como hay muchos espacios en blanco y la letra no está instantaneamente, hago recursion hasta encontrar una.
Ej 3: "hola      como     estan    " retornaria "hola como estan"   - quito los espacios en blanco entre las palabras y sanitizo el final tambien.    
-}

sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos (x:xs)
    | x == ' ' = sacarBlancosRepetidos xs --si la cabeza de la lista es vacía, sigo haciendo recursividad hasta encontrar primer caracter (ej. 2)
    | otherwise = sacarBlancosRepetidos' (x:xs)
  where
    sacarBlancosRepetidos' [] = []
    sacarBlancosRepetidos' [x] = if x == ' ' then [] else [x] --si la lista tiene un solo caracter y es vacio, devuelve nada, caso contrario el valor.
    sacarBlancosRepetidos' (x:xs) | x == ' ' && head xs == ' ' = sacarBlancosRepetidos' xs --si sucede algo como hola  como elimina un espacio                                                                                 en blanco.
                                  | otherwise = x : sacarBlancosRepetidos' xs

{-
Ejercicio 4.2: contarPalabras -> Recibo un palabra, mando a sacarBlancosRepetidos y la cantidad de espacios que hay, es la cantidad de palabras que hay.
Esta    es   una prueba  -> Esta es una prueba -> 3 espacios = 4 palabras.
(nada) = 0 palabras
h = 1 palabra
hola                = 1 palabra
-}

contarPalabras :: [Char] -> Integer
contarPalabras [] = 0
contarPalabras lista  | tail(lista) ==  [] = 1
contarPalabras lista  | head lista == ' ' && head(tail(lista)) == ' ' = contarPalabras(tail(lista))
contarPalabras lista  | head lista == ' ' && head(tail(lista)) /= ' ' =  1 + contarPalabras(tail(lista))
contarPalabras lista  | otherwise = contarPalabras(tail(lista)) 


{-
Ejercicio 4.3.: palabras Dada una lista arma una nueva lista con las palabras de la lista original. Cuando hay un espacio termina la palabra y debería crear una nueva lista y concatenarsela.
"hola     es     una   prueba" -> quito espacios "hola es una prueba" -> ["hola", "es", "una", "prueba"]
El proceso sería algo así:
h == ' '? no, por lo tanto agrego la h a una nueva secuencia 
o == ' '? no, por lo tanto agrego la h a la secuencia anterior creada.
l == ' '? no, por lo tanto agrego la h a la secuencia anterior creada.
a == ' '? no, por lo tanto agrego la h a la secuencia anterior creada.
' ' == ' '? sí, por lo tanto acá terminó la palabra, debería de crear un nuevo "indice" para la siguiente palabra.
e == ' '? no, por lo tanto agrego la e a la nueva secuencia.
s == ' '? no, por lo tanto agrego la s a la secuencia anterior creada.
hasta ahora ["hola", "es"]
y así sucesivamente.

Si ya la cola de la lista es vacia, entonces retorno []
-}


{-
    Ejercicio 4.5 aplanar: A partir de una lista de palabras arma una lista de caracteres concatenandola
    [] => "Hola"
-}

aplanar :: [[Char]] -> [Char]
aplanar [] = []
aplanar [x] = x
aplanar (x:xs) = x ++ aplanar(xs) --Voy concatenando el valor a una nueva lista.

{-
    Ejercicio 4.6: aplanarConBlancos:  que a partir de una lista de palabras, arma una lista de caracteres
concatenándolas e insertando un blanco entre cada palabra
-}

--Lo mismo que la de arriba pero por cada vez que termina una palabra agrego espacio.
aplanarConBlancos :: [[Char]] -> [Char]
aplanarConBlancos lista = aplanarConBlancosAux lista (longitud lista)

aplanarConBlancosAux :: [[Char]] -> Integer -> [Char]
aplanarConBlancosAux palabras cantidad | cantidad == 0 = []
                                       | otherwise = recorrerPalabra palabras (longitud(palabras))

recorrerPalabra :: [[Char]] -> Integer -> [Char] 
recorrerPalabra [] _ = []
recorrerPalabra [x] _ = x
recorrerPalabra (x:xs) letra = x ++ ' ' : recorrerPalabra xs (letra-1)
