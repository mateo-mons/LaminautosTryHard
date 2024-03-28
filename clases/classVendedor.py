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
        if isinstance(vehiculo, AutoUsado):
            utilidad_venta = vehiculo.calcular_valor_venta() - vehiculo.precio_compra
            comision = utilidad_venta * 0.07  # 7% de la utilidad de venta para autos usados
        elif isinstance(vehiculo, AutoNuevo):
            utilidad_venta = vehiculo.calcular_valor_venta() - vehiculo.precio_compra
            comision = utilidad_venta * 0.05  # 5% de la utilidad de venta para autos nuevos
        elif isinstance(vehiculo, MotoUsada):
            utilidad_venta = vehiculo.calcular_valor_venta() - vehiculo.precio_compra
            comision = utilidad_venta * 0.07  # 7% de la utilidad de venta para motos usadas
        elif isinstance(vehiculo, MotoNueva):
            utilidad_venta = vehiculo.calcular_valor_venta() - vehiculo.precio_compra
            comision = utilidad_venta * 0.05  # 5% de la utilidad de venta para motos nuevas


        return comision