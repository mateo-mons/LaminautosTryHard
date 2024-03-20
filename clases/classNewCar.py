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

    def crear_nuevo(id_nuevo, marca, modelo, color, cilindraje, num_llantas, anio, precio_compra):
        nuevo = AutoNuevo(id_nuevo, marca, modelo, color, cilindraje, num_llantas, anio, precio_compra)
        print("Auto nuevo ingresado al sistema exitosamente! \n")
        return nuevo
    
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
           
"""
while True:
    menu_nuevo()
    opcion = input("Opcion: ")

    if opcion == "1":
        marca = input("Marca del auto: ")
        modelo = input("Modelo del auto: ")
        color = input("Color del auto: ")
        cilindraje = input("Cilindraje del auto: ")
        num_llantas = input("Numero de llantas: ")
        anio = input("Año del auto: ")
        precio_compra = input("Precio de compra del auto: ")
        auto = AutoNuevo.crear_nuevo(marca, modelo, color, cilindraje, precio_compra)
        
    elif opcion == "2":
        print("---------------------------------------------------")
        auto.leer_nuevo()
        print("---------------------------------------------------")

    elif opcion == "3":
        pass

    elif opcion == "4":
        pass

    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opcion invalida. Intente de nuevo")


marca = input("Marca del vehiculo: ")
modelo = input("Modelo del vehiculo: ")
color = input("Color del vehiculo: ")
cilindraje = input("Cilindraje del vehiculo: ")
precio_compra = input("Precio de compra del vehiculo: ")
vehiculo = AutoNuevo.crear_nuevo(marca, modelo, color, cilindraje, precio_compra)

AutoNuevo.leer_nuevo(vehiculo)

"""
