
def funcion (lista1: list[(chr, chr)], lista2: list[chr]) -> list[chr]:
    lista: list[chr] = []
    for i in range(0, len(lista2)):
        for j in range(0, len(lista1)):
            if(lista2[i] == lista1[j][0]):
                lista.append( lista1[j][1]) 
    return lista

print(funcion([("B", "D"), ("A", "F")], ["B", "A"]))