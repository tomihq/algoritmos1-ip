from typing import List
from typing import Dict
import json

def unir_diccionarios(a_unir: List[Dict[str,str]]) -> Dict[str,List[str]]:
  nuevoDiccionario: Dict[str, List[int]] = {}
  for i in range (0, len(a_unir)):
    for j in range (0, len(a_unir[i].items())):
      listOfTuples:List[tuple(str, int)] = list(a_unir[i].items())
      if listOfTuples[j][0] in nuevoDiccionario:  
               nuevoDiccionario[listOfTuples[j][0]].append(listOfTuples[j][1]) 
      else: 
          nuevoDiccionario[listOfTuples[j][0]] = [listOfTuples[j][1]]
     
  return nuevoDiccionario

#Ejemplo cátedra
""" print(unir_diccionarios([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'a': 5}])) """
#Expected {'a': [1, 5], 'b': [2], 'c': [4, 6]} NO puede haber dos C en un mismo diccionario con distinto valor. Got: {'a': [1, 5], 'b': [2], 'c': [4, 6]}
""" print(unir_diccionarios([{'a': 1, 'b': 2}, {'c': 3, 'c': 4}, {'a': 5, 'c': 6}])) """
#Expected {'a': [1], 'b': [2], 'c': [3, 12], 'd': [12]} NO puede haber dos C en un mismo diccionario con distinto valor. Got: {'a': [1], 'b': [2], 'c': [3, 12], 'd': [12]}
""" print(unir_diccionarios([{'a': 1, 'b': 2}, {'c': 3, 'd': 12}, {'c': 6}])) """

if __name__ == '__main__':
  x = json.loads(input()) # Ejemplo de input: [{"a":2},{"b":3,"a":1}]
  print(unir_diccionarios(x))