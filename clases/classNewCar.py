class AutoNuevo:

    def __init__(self, id_nuevo, marca, modelo, color, cilindraje, num_llantas, anio, precio_compra):
        self.id_nuevo = id_nuevo
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.cilindraje = cilindraje
        self.num_llantas = num_llantas
        self.anio = anio
        self.precio_compra = precio_compra
   
    def leer_nuevo(self):
        print("----------------------------------------")
        print("Detalles del automovil...")
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Color:", self.color)
        print("Cilindraje:", self.cilindraje)
        print("Numero de llantas:", self.num_llantas)
        print("Año:", self.anio)
        print("Precio de compra:", self.precio_compra)
        print("----------------------------------------")

    def actualizar_nuevo(self):
        pass

    def eliminar_nuevo(self):
        pass
  
    def calcular_valor_venta(self):
            valor_venta = self.precio_compra + (self.precio_compra * 0.35)  # Valor de venta aumentado en un 35%
            return valor_venta 
