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
        
if __name__ == "__main__":
    p = ProductoKwiKE("Donuts Glaseadas", 123 , date(2026, 10 ,10) , 1.50 , 50)
    print(p.dias_para_expirar())
    p.cambiar_datos(precio=2.0, stock=40)