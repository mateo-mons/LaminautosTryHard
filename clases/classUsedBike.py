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

    def calcular_valor_venta(self):
            valor_venta = self.precio_compra + (self.precio_compra * 0.35)  # Valor de venta aumentado en un 35%
            valor_venta -= valor_venta * (self.siniestros * 0.05)  # Descuento por siniestros
            valor_venta -= valor_venta * ((2024 - self.anio) * 0.05)  # Descuento por años anteriores a 2015

            if self.anio < 2005:
                return 0  # No se realiza la transacción

            if self.kilometraje > 100000:
                valor_venta -= valor_venta * 0.10  # Descuento por kilometraje excesivo

            return valor_venta