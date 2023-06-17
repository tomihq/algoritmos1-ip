from typing import List

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.}

def valor_mas_grande(l: List[int]):
  valorMasGrande: int = 0
  for i in range(0, len(l)):
    if(l[i]>valorMasGrande):
      valorMasGrande = l[i]
    
  return valorMasGrande

def mesetaMasLarga(l: List[int]) -> int:
  if(len(l) == 0): return 0
  listaApariciones: List[int] = []
  numActual = l[0];
  indiceActual = 1
 
  for i in range(1, len(l)):
    if(l[i] != numActual):
      listaApariciones.append(indiceActual)
      numActual = l[i];
      indiceActual = 1
    else:
      indiceActual += 1
  
  listaApariciones.append(indiceActual)
  return valor_mas_grande(listaApariciones)

"""
  Tengo que contar la cantidad de veces que aparece el mismo numero consecutivamente.
  #Expected 0
  print(mesetaMasLarga([]))
  #Expected: 1
  print(mesetaMasLarga([1]))
  #Expected: 5
  print(mesetaMasLarga([1, 1, 1, 3, 3, 3, 3, 4, 4, 4, 4, 4]))
  #Expected: 3
  print(mesetaMasLarga([1, 1, 1, 3, 4]))
  #Expected: 6
  print(mesetaMasLarga([1, 1, 3, 3, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4]))
"""
  

if __name__ == '__main__':
  x = input()
  print(mesetaMasLarga([int(j) for j in x.split()]))