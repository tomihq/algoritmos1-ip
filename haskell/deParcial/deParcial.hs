cantApariciones :: (Eq t) => t -> [t] -> Int
cantApariciones e l | length l == 0 = 0
                    | (head l) == e = 1 + cantApariciones e (tail l)
                    | otherwise = 0 + cantApariciones e (tail l)

{- cantApariciones 1 [1, 1, 2, 1] -}

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece e lista | length lista == 0 = False
                  | (head lista) == e = True
                  | otherwise = pertenece e (tail lista)

{- pertenece 1 [2, 3, 1]
pertenece 1 []
pertenece 1 [2, 3, 2] -}

eliminarRepetidos :: (Eq t)  => [t] -> [t]
eliminarRepetidos l | length l == 0 = []
                    | otherwise = eliminarRepetidosAux l []

eliminarRepetidosAux :: (Eq t) => [t] -> [t] -> [t]
eliminarRepetidosAux l listaSinRep | length l == 0 = []
                                   | not(pertenece (head l) listaSinRep) = (head l) : eliminarRepetidosAux (tail l) ((head l):listaSinRep)
                                   | otherwise = eliminarRepetidosAux (tail l) listaSinRep

{-
eliminarYContarRep [1, 2, 3, 4, 1, 2] 
[(1, 2, 3, 4), [(1, 1), (2, 1), (3, 0), (4, 0)]]
-}

eliminarYContarRep :: (Eq t)  =>  [t] -> ([t], [(t, Int)]) 
eliminarYContarRep l = (eliminarRepetidos l, eliminarYContarRepAux (eliminarRepetidos l) l)

eliminarYContarRepAux :: (Eq t) => [t] -> [t] -> [(t, Int)]
eliminarYContarRepAux [] _ = []
eliminarYContarRepAux (x:xs) lista = (x, (cantApariciones x lista) - 1) : eliminarYContarRepAux xs lista
