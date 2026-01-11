

class Producto:
    def __init__(self, id, compra_id, nombre_producto, cantidad, precio_unitario, marca = None) -> None:
        self.id = id
        self.compra_id = compra_id
        self.nombre_producto = nombre_producto
        self.marca = marca
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario


