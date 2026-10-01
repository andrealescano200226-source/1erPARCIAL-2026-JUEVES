from datetime import date 
class ProductoKwiKE :
    def __init__(self , descripcion , id_producto , fecha_vencimiento , precio, stock , categoria=""):
        self . descripcion = descripcion
        self . id_producto = id_producto
        self . fecha_vencimiento = fecha_vencimiento
        self . precio = precio
        self . stock = stock
        self . categoria = categoria 

    def cambiar_datos(self , descripcion=None , precio=None , stock=None):
        if descripcion is not None:
            self.descripcion = descripcion
        if precio is not None:
            self.precio = precio
        if stock is not None:
            self.stock = stock
    
    def dias_para_expirar(self):
        dias = (self.fecha_vencimiento - date.today()).days
        if dias < 0:
            print(f"El producto ´{self.descripcion}´ esta expirado.")
            self.stock = 0
        return dias

    def __str__(self):
        return (f"Producto: {self.descripcion} | ID: {self.id_producto} | " 
                f"Precio: ${self.precio:.2f} | stock: {self.stock}")

    def __eq__(self,otro):
        if not isinstance(otro, ProductoKwiKE) :
            return False
        return (self.id_producto == otro.id_producto
                and self.descripcion == otro.descripcion)

if __name__ == "__main__":
    a = ProductoKwiKE("Donuts Glaseadas" , 123, date(2026, 10, 10), 1.50, 50)
    b = ProductoKwiKE("Donuts Glaseadas" , 123, date(2026, 11, 1), 2.00, 10)
    print(a)
    print(a == b)