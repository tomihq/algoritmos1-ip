from typing import List

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.

def filasParecidas(m: List[List[int]]) -> bool :
  for n in range (len(m)):
    if(filasParecidasAanterior(m, n)):
      return True

  return False

def filasParecidasAanterior(m: List[List[int]], n: int) -> bool:
  for i in range(1, len(m)):
    if(filaAnteriorMasN(m, i, n) == False):
      return False
    
  return True

def filaAnteriorMasN(m: List[List[int]], i, n: int) -> bool:
  for j in range (0, len(m[0])):
    if(m[i][j] != m[i-1][j] + n):
      return False
  return True
  

"""
  Osea que basicamente busca que exista un n IGUAL que haga que la fila de la derecha de la izq sea igual a la de la derecha.
  #Expected True pues cuando n es igual a 1, todas las filas en la misma posicion se incrementan en uno.
  print(filasParecidas([[1, 2, 3], [2, 3, 4], [3, 4, 5]]))
  #Expected True (n = 0)
  print(filasParecidas([[1, 2, 3], [1, 2, 3]]))
  #Expected False no existe un n igual que haga que la fila que le sigue sea igual a la de la izq.
  print(filasParecidas([[1, 2, 3], [3, 4, 5], [1, 2, 3]]))
  #Expected False
  print(filasParecidas([[1, 2, 3], [3, 4, 5]]))
"""

if __name__ == '__main__':
  filas = int(input())
  columnas = int(input())
 
  matriz = []
 
  for i in range(filas):         
    fila = input()
    if len(fila.split()) != columnas:
      print("Fila " + str(i) + " no contiene la cantidad adecuada de columnas")
    matriz.append([int(j) for j in fila.split()])
  
  print(filasParecidas(matriz))