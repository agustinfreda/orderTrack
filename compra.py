from datetime import datetime


class Compra:
    def __init__(self, id, lugar) -> None:
        self.id = id
        self.fecha_inicio = datetime.now()
        self.fecha_cierre = None
        self.lugar = lugar
        self.estado = "abierta"
        self.total = 0
        self.cantidad_productos = 0


def cerrar_compra(compra):
    if compra.estado == "cerrada":
        raise Exception("Compra ya cerrada.")

    compra.estado = "cerrada"
    compra.fecha_cierre = datetime.now()


def cancelar_compra(compra):
    if compra.cantidad_productos > 0:
        raise Exception("La compra no debe tener productos para cancelarse.")
    
    if compra.estado != "abierta":
        raise Exception("No se puede cancelar una compra cerrada o cancelada con anterioridad.")

    compra.estado = "cancelada"


def agregar_producto(compra, producto):
    if compra.estado != "abierta":
        raise Exception("La compra no está abierta.")

    if producto.cantidad <= 0 or producto.precio_unitario <= 0:
        raise Exception("Valor ingresado incorrecto.")

    compra.total += producto.cantidad * producto.precio_unitario
    compra.cantidad_productos += 1


def recalcular_total(compra, items):
    compra.total = sum(
        item.cantidad * item.precio_unitario
        for item in items
    )



