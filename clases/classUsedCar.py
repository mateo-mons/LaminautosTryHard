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

    def calcular_valor_comercial(self):
        valor_comercial = self.precio_compra

        # Reducción del valor comercial por siniestros
        if self.siniestros is not None:
            valor_comercial -= (self.siniestros * 0.05 * valor_comercial)

        # Reducción del valor comercial por años anteriores a 2015
        if self.anio < 2015:
            años_antiguos = 2015 - self.anio
            valor_comercial -= (años_antiguos * 0.05 * valor_comercial)

        # Reducción adicional si el modelo es anterior a 2005
        if self.anio < 2005:
            valor_comercial -= 0.1 * valor_comercial

        # Reducción adicional si el kilometraje supera 100,000 km
        if self.kilometraje is not None and self.kilometraje > 100000:
            valor_comercial -= 0.1 * valor_comercial

        return valor_comercial
    