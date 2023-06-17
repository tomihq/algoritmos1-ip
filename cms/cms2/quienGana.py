import sys

def gana(j1, j2: str) -> bool:
   return piedraGanaAtijera(j1, j2) or tijeraGanaAPapel(j1, j2) or papelGanaAPiedra(j1, j2)

def piedraGanaAtijera(j1, j2: str) -> bool:
   return j1 == 'Piedra' and j2 == 'Tijera'

""" 
  #Expected False
  print(tijeraGanaAPapel('Tijera', 'Piedra'))
  #Expected True
  print(tijeraGanaAPapel('Piedra', 'Tijera'))  
"""


def tijeraGanaAPapel(j1, j2: str) -> bool:
   return j1 == 'Tijera' and j2 == 'Papel'


""" 
#Expected False
print(tijeraGanaAPapel('Papel', 'Tijera'))
#Expected True
print(tijeraGanaAPapel('Tijera', 'Papel'))  """


def papelGanaAPiedra(j1, j2: str) -> bool:
   return j1 == 'Papel' and j2 == 'Piedra'

""" #Expected False
print(papelGanaAPiedra('Piedra', 'Papel'))
#Expected True
print(papelGanaAPiedra('Papel', 'Piedra')) """

def quienGana(j1: str, j2: str) -> str:
    res: str = "";
    if(gana(j1, j2)):
       res = "Jugador1"
    elif(gana(j2, j1)):
       res = "Jugador2"
    else:
       res = "Empate" 
    return res

#quienGana("Piedra", "Tijera") -> Jugador1 pues la Piedra le gana a la tijera.
#quienGana("Piedra", "Papel") -> Jugador2 pues el Papel le gana a la piedra.
#quienGana("Piedra", "Piedra") -> Empate
#quienGana("Tijera", "Tijera") -> Empate


if __name__ == '__main__':
  x = input()
  jug = str.split(x)
  print(quienGana(jug[0], jug[1]))

