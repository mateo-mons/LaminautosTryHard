class AutoUsado:

    def __init__(self, id_usado, marca, modelo, color, cilindraje, num_llantas, anio, kilometraje, siniestros, precio_compra):
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

    def crear_usado(id_usado, marca, modelo, color, cilindraje, num_llantas, anio, kilometraje, siniestros, precio_compra):
        usado = AutoUsado(id_usado, marca, modelo, color, cilindraje, num_llantas, anio, kilometraje, siniestros, precio_compra)
        print("Auto usado ingresado al sistema exitosamente! \n")
        return usado
    
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
        print("----------------------------------------")

    def actualizar_usado(self):
        pass

    def eliminar_usado(self):
        pass
        
        