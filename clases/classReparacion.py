from clases.classOrdenDeServicio import *

class Reparacion():

    def __init__(self):
        self.ordenes_servicio = []

    def ingresar_vehiculo_reparacion(self, cliente, vehiculo, descripcion_problema):
        print("Seleccione el estado de la reparación:")
        for i, estado in enumerate(OrdenDeServicio.estados_reparacion):
            print(f"{i + 1}. {estado}")
        
        opcion_estado = int(input("Opción: "))
        if opcion_estado < 1 or opcion_estado > len(OrdenDeServicio.estados_reparacion):
            print("Opción no válida.")
            return

        estado_reparacion = OrdenDeServicio.estados_reparacion[opcion_estado - 1]

        orden_servicio = OrdenDeServicio(cliente, vehiculo, descripcion_problema, estado_reparacion)
        self.ordenes_servicio.append(orden_servicio)
        print("Vehículo ingresado a reparación.")