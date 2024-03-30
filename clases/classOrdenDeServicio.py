from clases.classCliente import *

class OrdenDeServicio:

    estados_reparacion = ["En reparacion", "En pintura", "Para entrega"]

    def __init__(self, id_orden, cliente, vehiculo, descripcion_problema, estado_reparacion="En reparacion"):
        self.id_orden = id_orden
        self.cliente = cliente
        self.vehiculo = vehiculo
        self.descripcion_problema = descripcion_problema
        if estado_reparacion in self.estados_reparacion:
            self.estado_reparacion = estado_reparacion

    def ver_orden(self):
        print("----------------------------------------")
        print("Detalles de orden de servicio...")
        print("Cliente:", self.cliente)
        print("Vehículo:", self.vehiculo)
        print("Descripción del problema:", self.descripcion_problema)
        print("Estado de reparación: ", self.estado_reparacion)
        print("----------------------------------------")

    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado in self.estados_reparacion:
            self.estado_reparacion = nuevo_estado
        else:
            print("Estado de reparación no válido.")

    def actualizar_estado_orden(self):
        print("* Seleccione el estado de la orden *")
        print("1. En reparacion")
        print("2. En pintura")
        print("3. Para entrega")
        opcion = input("Opción: ")

        if opcion == "1":
            self.cambiar_estado("En reparacion")
        elif opcion == "2":
            self.cambiar_estado("En pintura")
        elif opcion == "3":
            self.cambiar_estado("Para entrega")
        else:
            print("Opción no válida.")

