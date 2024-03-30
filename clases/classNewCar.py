class AutoNuevo:

    def __init__(self, id_nuevo, marca, modelo, color, cilindraje, num_llantas, anio, precio_compra, estado="Para la venta"):
        self.id_nuevo = id_nuevo
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.cilindraje = cilindraje
        self.num_llantas = num_llantas
        self.anio = anio
        self.precio_compra = precio_compra
        self.estado = estado
   
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
        print("Estado:", self.estado)
        print("----------------------------------------")

    def actualizar_nuevo(self):
        pass

    def eliminar_nuevo(self):
        pass
  
    def calcular_valor_venta(self):
        valor_venta = 1.35 * self.precio_compra  # Valor de venta es 35% más del valor de compra
        return valor_venta 
