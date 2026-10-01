from datetime import date,timedelta
from Ejercicio6 import ProductoKwiKE

class KwiKEMart:
    def __init__(self):
        self.pasillos = {}
    def _nueva_lista(self):
        return[]
    def agregar_producto(self, pasillo, producto):
        if pasillo not in self.pasillos:
            self.pasillos[pasillo] = self._nueva_lista()
        self.pasillo[pasillo].append(producto)
    def remover_producto(self, pasillo, id_producto):
        producto = self.buscar_por_id(id_producto)
        if producto is not None and pasillo in self.pasillos:
            self.pasillos[pasillo]remove(producto)
            return True
        return False
    def actualizar_stock(self, id_producto, nuevo_stock):
        producto = self.buscar_por_id(id_producto)
        if producto is not None:
            producto.stock = nuevo_stock
            return True
        return False
    def buscar_por_id(self , id_producto):
        for lista in self.pasillos.values():
            for producto in lista:
                if producto.id_producto == id_producto:
                    return producto
                return None
    def descartar_por_expirar(self):
        limite = date.today() + timedelta(days=1)
        descartados = 0
        for lista in self.pasillo.values():
            vencidos = [p for p in lista if p.fecha_vencimiento <= limite]
            for p in vencidos:
                lista.remove(p)
                descartados += 1
            return descartados
if __name__ == "__main__":
    k = KwiKEMart()
    k.agregar_producto("Snacks", ProductoKwiKE("Papas", 1, date.today() , 2.5, 20))
    k.agregar_producto("Bebidas" , ProductoKwiKE("Duff" , 1, date(2027, 1 , 1), 3.0, 30 ))
    print(k.descartar_por_expirar())