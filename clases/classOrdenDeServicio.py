
class OrdenDeServicio:
    estados_reparacion = ["En reparación", "En pintura", "Para entrega"]

    def __init__(self, cliente, vehiculo, descripcion_problema, estado_reparacion):
        self.cliente = cliente
        self.vehiculo = vehiculo
        self.descripcion_problema = descripcion_problema
        self.estado_reparacion = estado_reparacion

    def ver_orden(self):
        print("----------------------------------------")
        print("Detalles de orden de servicio...")
        print("Cliente:", self.cliente)
        print("Vehículo:", self.vehiculo)
        print("Descripción del problema:", self.descripcion_problema)
        print("Estado de reparación: ", self.estados_reparacion[self.estado_reparacion[0]])
        print("----------------------------------------")

