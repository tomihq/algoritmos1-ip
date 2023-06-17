import sys

def fibonacciNoRecursivo(n: int) -> int:
  longMax: int = n+1
  l: list[int] = []
  maxFibonacci: int = 0;
  indice: int = 0
  while(indice < longMax):
     if(len(l) == 0):
        l.append(0)
     elif(len(l) == 1):
         l.append(1)
     else:
        terminoSiguiente: int = l[indice-1] + l[indice-2] 
        l.append(terminoSiguiente)
     indice+=1

  maxFibonacci = l[len(l)-1]
  return maxFibonacci

""" 
(∃l : seq⟨Z⟩)(|l| = n + 1 ∧ esSecuenciaFiibonacci(l) ∧ l[|l|−1] = result)
La secuencia de fibonacci que tengo que hacer va hasta n +1.
Luego, devuelvo el último valor de la lista.
print("fibonacci 0: " + str(fibonacciNoRecursivo(0)))
print("fibonacci 1: " + str(fibonacciNoRecursivo(1)))
print("fibonacci 2: " + str(fibonacciNoRecursivo(2)))
print("fibonacci 3: " + str(fibonacciNoRecursivo(3)))
print("fibonacci 4: " + str(fibonacciNoRecursivo(4)))
print("fibonacci 5: " + str(fibonacciNoRecursivo(5)))
print("fibonacci 6: " + str(fibonacciNoRecursivo(6)))
print("fibonacci 7: " + str(fibonacciNoRecursivo(7)))
print("fibonacci 8: " + str(fibonacciNoRecursivo(8)))
print("fibonacci 9: " + str(fibonacciNoRecursivo(9)))
print("fibonacci 10: " + str(fibonacciNoRecursivo(10))) """

if __name__ == '__main__':
  x = int(input())
  print(fibonacciNoRecursivo(x))