from clases.classNewCar import *
from clases.classUsedCar import *
from clases.classNewBike import *
from clases.classUsedBike import *

class Vendedor:

    def __init__(self, id_vend, nombre, num_ident, telefono):
        self.id_vend = id_vend
        self.nombre = nombre
        self.num_ident = num_ident
        self.telefono = telefono
    
    def leer_nuevo(self):
        print("----------------------------------------")
        print("Detalles de vendedor...")
        print("Nombre:", self.nombre)
        print("Numero de identificacion:", self.num_ident)
        print("Telefono de contacto:", self.telefono)
        print("----------------------------------------")

    def actualizar_nuevo(self):
        pass

    def eliminar_nuevo(self):
        pass

    def calcular_comision(self, vehiculo):
        if isinstance(vehiculo, AutoUsado):  # Si es un auto usado
            comision = 0.07 * (vehiculo.calcular_valor_comercial() - vehiculo.precio_compra)  # Comisión del 7% sobre la utilidad
        elif isinstance(vehiculo, AutoNuevo):  # Si es un auto nuevo
            comision = 0.05 * (vehiculo.calcular_valor_venta() - vehiculo.precio_compra)  # Comisión del 5% sobre la utilidad

        elif isinstance(vehiculo, MotoUsada):  # Si es una moto usada
            comision = 0.07 * (vehiculo.calcular_valor_comercial() - vehiculo.precio_compra)  # Comisión del 7% sobre la utilidad
        elif isinstance(vehiculo, MotoNueva):  # Si es una moto nueva
            comision = 0.05 * (vehiculo.calcular_valor_venta() - vehiculo.precio_compra)  # Comisión del 5% sobre la utilidad

        return comision
