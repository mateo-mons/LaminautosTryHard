class MotoNueva:

    def __init__(self, id_nueva, marca, modelo, color, cilindraje, num_llantas, anio, precio_compra):
        self.id_nueva = id_nueva
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.cilindraje = cilindraje
        self.num_llantas = num_llantas
        self.anio = anio
        self.precio_compra = precio_compra

    def crear_nueva(id_nueva, marca, modelo, color, cilindraje, num_llantas, anio, precio_compra):
        nueva = MotoNueva(id_nueva, marca, modelo, color, cilindraje, num_llantas, anio, precio_compra)
        print("Moto nueva ingresada al sistema exitosamente! \n")
        return nueva
    
    def leer_nueva(self):
        print("----------------------------------------")
        print("Detalles de la moto...")
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Color:", self.color)
        print("Cilindraje:", self.cilindraje)
        print("Numero de llantas:", self.num_llantas)
        print("Año:", self.anio)
        print("Precio de compra:", self.precio_compra)
        print("----------------------------------------")

    def actualizar_nueva(self):
        pass

    def eliminar_nueva(self):
        pass

    def calcular_valor_venta(self):
            valor_venta = self.precio_compra + (self.precio_compra * 0.35)  # Valor de venta aumentado en un 35%
            return valor_venta 
           


