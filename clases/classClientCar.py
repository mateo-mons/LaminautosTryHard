class AutoCliente:

    estados_vehiculo = ["Optimo", "En reparacion"]

    def __init__(self, id_car, marca, modelo, color, cilindraje, num_llantas, anio, estado="Optimo"):
        self.id_car = id_car
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.cilindraje = cilindraje
        self.num_llantas = num_llantas
        self.anio = anio
        if estado in self.estados_vehiculo:
            self.estado = estado
        else:    
            print("Estado no valido")
        
    def leer_auto_cliente(self):
        print("----------------------------------------")
        print("Detalles del automovil...")
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Color:", self.color)
        print("Cilindraje:", self.cilindraje)
        print("Numero de llantas:", self.num_llantas)
        print("Año:", self.anio)
        print("Estado: ", self.estado)
        print("----------------------------------------")

    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado in self.estados_vehiculo:
            self.estado = nuevo_estado
        else:
            print("Estado no válido.")

    def actualizar_estado_vehiculo(self):
        print("* Estado del vehículo *")
        print("1. Reparacion")
        opcion = input("Opción: ")

        if opcion == "1":
            self.cambiar_estado("En reparacion")
        else:
            print("Opción no válida.")