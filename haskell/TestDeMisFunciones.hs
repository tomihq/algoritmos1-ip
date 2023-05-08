module TestDeMisFunciones where
    
import Test.HUnit
import MultiplosDeN --carga un archivo.

testSuite = test[
    "Caso 1: Múltiplos de 2" ~: (multiplosDeN 2 [1, 2, 3, 4, 5, 6]) ~?= [2, 4, 6]
    ]

runCases = runTestTT testSuite
--Para probarlo en GHCI colocar runCases