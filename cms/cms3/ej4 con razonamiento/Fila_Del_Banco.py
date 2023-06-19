from queue import Queue

# El tipo de fila debería ser Queue[int], pero la versión de python del CMS no lo soporta. Usaremos en su lugar simplemente "Queue"
def avanzarFila(fila: Queue, min: int):
  #Prioridad de las cajas - CAJA 1, CAJA 2, CAJA 3. if, else if, else. Si el numero mod 4 es 0 entonces agrego una persona al final.
  comienzaCajaUno: int = 1; #1, 11, 21, 31, 41, 51
  comienzaCajaDos: int = 3; #3 (3 mod 4 = 3), 7 (7 mod 4 = 3), 11 (11 mod 4 = 4), 15 (15 mod 4 = 3), 19 (19 mod 4 = 3), 23, 27, 31 -> impares y primos.
  comienzaCajaTres: int = 2; #2 (2 mod 4 = 2), 6 (6 mod 4 = 2), 10 (10 mod 4 = 2), 14 (14 mod 4 = 2), 18, 22, 26, 30
  #Vuelven los clientes a cola no resueltos por caja 3: 3 min despues osea:
  # 2 vuelve 5 
  # 6 vuelve 9
  # 10 vuelve 13
  # 14 vuelve 17

  atiendeCajaUnoCada: int = 10; #Si resto es 1 osea, tiempo mod 10 es 1 entonces es caja 1 (todos dan resto 1, osea 00:01)
  atiendaCajaDosCada: int = 4;
  atiendeCajaTresCada: int = 4; #Quien está aquí, vuelve a la cola luego en 3 min al final.


  tiempo: int = 0; #Comienza 00:00 (abre banco)
  clienteNoResuelto: int = None;
  primerElementoAñadido: bool = False
  ultimoElementoCola: int = 1;
  tiempoEnLlegarACola: int = 3;
  tiempoQuePasoParaLlegarACola: int = 0;
  

  if(fila.qsize() == 0):
        fila.put(ultimoElementoCola)
        primerElementoAñadido = True


  while(tiempo <= min):
    if(tiempoQuePasoParaLlegarACola==tiempoEnLlegarACola):
      fila.put(clienteNoResuelto);
      clienteNoResuelto = None;
      tiempoQuePasoParaLlegarACola = 0;
    
    if(tiempo % 4 == 0 and primerElementoAñadido == False):
          if(ultimoElementoCola == 1 and fila.qsize() != 0):
              copiaCola: list[int] = list(fila.queue);
              ultimoElementoCola = copiaCola[len(copiaCola)-1]+1
          else:
             ultimoElementoCola = ultimoElementoCola+1
          fila.put(ultimoElementoCola)


    else: 
        if(tiempo >= comienzaCajaUno and tiempo % atiendeCajaUnoCada == 1 and fila.qsize() >0):
          fila.get();
    
        else: 
          if(tiempo>=comienzaCajaDos and tiempo % atiendaCajaDosCada == 3 and fila.qsize() >0):
            fila.get();
    
          else:
            if(tiempo>=comienzaCajaTres and tiempo % atiendeCajaTresCada == 2 and fila.qsize() >0):
            #acá es donde no resuelve.
              clienteNoResuelto = fila.get();
    
    if(clienteNoResuelto is not None):
      tiempoQuePasoParaLlegarACola+=1

    primerElementoAñadido = False
    tiempo+=1;

  
  listaFila = list(fila.queue)
  return listaFila

""" queue = Queue()
queue.put(1)
queue.put(2)
queue.put(3)
print(avanzarFila(queue, 13)); """

if __name__ == '__main__':
  fila: Queue = Queue()
  fila_inicial: int = int(input())
  for numero in range(1, fila_inicial+1):
    fila.put(numero)
  min: int = int(input())
  avanzarFila(fila, min)
  res = []
  for i in range(0, fila.qsize()):
    res.append(fila.get())
  print(res)


# Caja1: Empieza a atender 10:01, y atiende a una persona cada 10 minutos
# Caja2: Empieza a atender 10:03, atiende a una persona cada 4 minutos
# Caja3: Empieza a atender 10:02, y atiende una persona cada 4 minutos, pero no le resuelve el problema y la persona debe volver a la fila (se va al final y tarda 3 min en llegar. Es decir, la persona que fue atendida 10:02 vuelve a entrar a la fila a las 10:05)
# La fila empieza con las n personas que llegaron antes de que abra el banco. Cuando abre (a las 10), cada 4 minutos llega una nueva persona a la fila (la primera entra a las 10:00)

