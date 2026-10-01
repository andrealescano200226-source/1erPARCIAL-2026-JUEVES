class Nodo:
    def __init__(self, dato, sig=None):
        self._elem = dato
        self._nxt = sig

class IteradorLista:
    def __init__(self, actual):
        self.actual = actual
    def __inter__(self):
        return self
    def__next__(self):
        if self.actual is None:
            raise StopIteration
        dato = self.actual._elem
        self.actual = self.actual._nxt
        return dato

class ListaEnlazada:
    def __init__(self):
        self.header = Nodo(None)
        self.tamano = 0
    def esta_vacia(self):
        return self.header._nxt is None
    def agregar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato, self.header.xnt)
        self.header.nxt = nuevo_nodo
        self.tamano += 1
    def agregar_al_final(self, dato):
        actual = self.header
        while actual._nxt is not None:
            actual = actual._nxt
        actual._nxt = Nodo(dato)
        self. tamano += 1

    def __inter__(self):
        return IteradorLista(self.header._nxt)
    def __len__(self):
        return self.tamano
    def __str__(self):
        elementos = [str(elem) for elem in self]
        return "->". join(elementos) if elementos else "Lista vacia"
