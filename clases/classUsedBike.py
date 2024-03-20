class MotoUsada:

    def __init__(self, id_usada, marca, modelo, color, cilindraje, num_llantas, anio, kilometraje, siniestros, precio_compra):
        self.id_usada = id_usada
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.cilindraje = cilindraje
        self.num_llantas = num_llantas
        self.anio = anio
        self.kilometraje = kilometraje
        self.siniestros = siniestros
        self.precio_compra = precio_compra

    def crear_usada(id_usada, marca, modelo, color, cilindraje, num_llantas, anio, kilometraje, siniestros, precio_compra):
        usada = MotoUsada(id_usada, marca, modelo, color, cilindraje, num_llantas, anio, kilometraje, siniestros, precio_compra)
        print("Moto usada ingresada al sistema exitosamente! \n")
        return usada
    
    def leer_usada(self):
        print("----------------------------------------")
        print("Detalles de la moto...")
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Color:", self.color)
        print("Cilindraje:", self.cilindraje)
        print("Numero de llantas:", self.num_llantas)
        print("Año:", self.anio)
        print("kilometraje:", self.kilometraje)
        print("Siniestros:", self.siniestros)
        print("Precio de compra:", self.precio_compra)
        print("----------------------------------------")

    def actualizar_usada(self):
        pass

    def eliminar_usada(self):
        pass