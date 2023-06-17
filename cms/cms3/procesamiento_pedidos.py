from queue import Queue
from typing import List
from typing import Dict
from typing import Union
import json
    
# ACLARACIÓN: El tipo de "pedidos" debería ser: pedidos: Queue[Dict[str, Union[int, str, Dict[str, int]]]]
# Por no ser soportado por la versión de CMS, usamos simplemente "pedidos: Queue"
def procesamiento_pedidos(pedidos: Queue,
                          stock_productos: Dict[str, int],
                          precios_productos: Dict[str, float]) -> List[Dict[str, Union[int, str, float, Dict[str, int]]]]:
  res:List[Dict[str, Union[int, str, float, Dict[str, int]]]] = []
  while(not(pedidos.empty())):
      pedidoIncompleto: bool = False
      acum: float = 0
      pedido = pedidos.get()
      productosPedido = list(pedido["productos"].items())
      productosDisponibles: dict[str, int] = {}
      for i in range (0, len(productosPedido)):
          productoSolicitado:tuple(str, int) = productosPedido[i]
          cantDisponibleStockProductoSolicitado = stock_productos[productoSolicitado[0]]
          precioProductoSolicitado = precios_productos[productoSolicitado[0]]
          if(cantDisponibleStockProductoSolicitado >= productoSolicitado[1]):
              productosDisponibles[productoSolicitado[0]] = productoSolicitado[1]
              acum += productoSolicitado[1] * precioProductoSolicitado
              stock_productos[productoSolicitado[0]] -= productoSolicitado[1]
          else:
              pedidoIncompleto = True
              acum += stock_productos[productoSolicitado[0]] * precioProductoSolicitado
              productosDisponibles[productoSolicitado[0]] = stock_productos[productoSolicitado[0]]
              stock_productos[productoSolicitado[0]] = 0 
              
      pedido["precio_total"] = acum
      if(pedidoIncompleto):
          pedido["estado"] = 'incompleto'
      else:
          pedido["estado"] = 'completo'
      pedido["productos"] = productosDisponibles
      
      res.append(pedido)
        
  return res


""" 
TESTS PORQUE FALLA CMS NO SÉ PORQUE
1. 
pedidos = Queue()
pedidos.put({"id": 21, "cliente": "Gabriela", "productos": {"Manzana": 1}})
stock_productos = {"Manzana": 110, "Leche": 15, "Pan": 63, "Factura": 50}
precios_productos = {"Manzana": 3.5, "Leche": 5.5, "Pan": 3.5, "Factura": 5}

print(procesamiento_pedidos(pedidos, stock_productos, precios_productos))

2. 
pedidos = Queue()
pedidos.put({"id":21,"cliente":"Gabriela", "productos":{"Manzana":1, "Leche":5, "Pan":3,}})
pedidos.put({"id":20,"cliente":"Tomas", "productos":{"Manzana":1,"Leche":5, "Pan":3, "Factura":6}})
stock_productos = {"Manzana":5, "Leche":5, "Pan":5, "Factura":5}
precios_productos = {"Manzana":3.5, "Leche":5.5, "Pan":3.5, "Factura":5}
print(procesamiento_pedidos(pedidos, stock_productos, precios_productos))

"""


if __name__ == '__main__':
  pedidos: Queue = Queue()
  list_pedidos = json.loads(input())
  [pedidos.put(p) for p in list_pedidos]
  stock_productos = json.loads(input())
  precios_productos = json.loads(input())
  print("{} {}".format(procesamiento_pedidos(pedidos, stock_productos, precios_productos), stock_productos))

# Ejemplo input  
# pedidos: [{"id":1,"cliente":"Juan","productos":{"Manzana":2,"Pan":4,"Factura":6}}]
# stock_productos: {"Manzana":10, "Leche":5, "Pan":3, "Factura":0}
# precios_productos: {"Manzana":3.5, "Leche":5.5, "Pan":3.5, "Factura":5}