module TestDeMisFunciones where
    
import Test.HUnit
import MultiplosDeN --carga un archivo.

testSuite = test[
    "Caso 1: Múltiplos de 2" ~: (multiplosDeN 2 [1, 2, 3, 4, 5, 6]) ~?= [2, 4, 6],
    "Caso 2: Múltiplos de 0" ~: (multiplosDeN 0 [0, 2, 3, 4, 5, 6]) ~?= [],
    "Caso 3: Lista vacía"    ~: (multiplosDeN 4 []) ~?= [],
    "Caso 4: Hay un solo múltiplo" ~: (multiplosDeN 4 [8, 9]) ~?= [8],
    "Caso 5: No hay múltiplos con n negativo" ~: (multiplosDeN (-4) [1, 3, 5, 9, 12]) ~?= [],
    "Caso 6: Hay más de un múltiplo con n negativo" ~: (multiplosDeN (-6) [1, 4, 3, 12, 18]) ~?= [12, 18]
    ]

runCases = runTestTT testSuite
--Para probarlo en GHCI colocar runCases