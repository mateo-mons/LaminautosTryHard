class AutoUsado:

    estados_vehiculo = ["Para la venta", "En reparacion"]

    def __init__(self, id_usado, marca, modelo, color, cilindraje, num_llantas, anio, kilometraje, siniestros, precio_compra, estado="Para la venta"):
        self.id_usado = id_usado
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.cilindraje = cilindraje
        self.num_llantas = num_llantas
        self.anio = anio
        self.kilometraje = kilometraje
        self.siniestros = siniestros
        self.precio_compra = precio_compra
        if estado in self.estados_vehiculo:
            self.estado = estado
        else:    
            print("Estado no valido")
    
    def leer_usado(self):
        print("----------------------------------------")
        print("Detalles del automovil...")
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Color:", self.color)
        print("Cilindraje:", self.cilindraje)
        print("Numero de llantas:", self.num_llantas)
        print("Año:", self.anio)
        print("kilometraje:", self.kilometraje)
        print("Siniestros:", self.siniestros)
        print("Precio de compra:", self.precio_compra)
        print("Estado: ", self.estado)
        print("----------------------------------------")

    '''
    def actualizar_usado(self, marca=None, modelo=None, color=None, num_llantas=None, anio=None):
        if marca:
            self.marca = marca
        if modelo:
            self.modelo = modelo
        if color:
            self.color = color
        if num_llantas:
            self.num_llantas = num_llantas
        if anio:
            self.anio = anio
    '''

    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado in self.estados_vehiculo:
            self.estado = nuevo_estado
        else:
            print("Estado no válido.")

    def actualizar_estado_vehiculo(self):
        print("* Seleccione el estado del vehículo *")
        print("1. Para la venta")
        print("2. En reparacion")
        opcion = input("Opción: ")

        if opcion == "1":
            self.cambiar_estado("Para la venta")
        elif opcion == "2":
            self.cambiar_estado("En reparacion")
        else:
            print("Opción no válida.")


    def eliminar_usado(self):
        pass
        
    def calcular_valor_venta(self):
        valor_venta = self.precio_compra + (self.precio_compra * 0.35)  # Valor de venta aumentado en un 35%
        valor_venta -= valor_venta * (self.siniestros * 0.05)  # Descuento por siniestros
        valor_venta -= valor_venta * ((2024 - self.anio) * 0.05)  # Descuento por años anteriores a 2015

        if self.anio < 2005:
            return 0  # No se realiza la transacción

        if self.kilometraje > 100000:
            valor_venta -= valor_venta * 0.10  # Descuento por kilometraje excesivo

        return valor_venta