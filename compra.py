from datetime import datetime


class Compra:
    def __init__(self, id, lugar) -> None:
        self.id = id
        self.fecha_inicio = datetime.now()
        self.fecha_cierre = None
        self.lugar = lugar
        self.estado = "abierta"
        self.total = 0


def cerrar_compra(compra):
    if compra.estado == "cerrada":
        raise Exception("Compra ya cerrada.")

    compra.estado = "cerrada"
    compra.fecha_cierre = datetime.now()

