class OrdenDeServicio:
    estados_reparacion = ["En reparación", "En pintura", "Para entrega"]

    def __init__(self, cliente, vehiculo, descripcion_problema, estado_reparacion):
        self.cliente = cliente
        self.vehiculo = vehiculo
        self.descripcion_problema = descripcion_problema
        if estado_reparacion in self.estados_reparacion:
            self.estado_reparacion = estado_reparacion
        else:
            print("Estado de reparación no válido.")