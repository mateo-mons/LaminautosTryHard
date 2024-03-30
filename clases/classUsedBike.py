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