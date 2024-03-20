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
           
"""
def menu_usado():
    print("-- MENU --")
    print("1. Ingresar vehiculo usado")
    print("2. Leer informacion de vehiculo usado")
    print("3. Actualizar informacion de vehiculo usado")
    print("4. Eliminar informacion de vehiculo usado")
    print("5. Salir")


while True:
    menu_usado()
    opcion = input("Opcion: ")

    if opcion == "1":
        marca = input("Marca del vehiculo: ")
        modelo = input("Modelo del vehiculo: ")
        color = input("Color del vehiculo: ")
        cilindraje = input("Cilindraje del vehiculo: ")
        kilometraje = input("Kilometraje del vehiculo: ")
        siniestros = input("Numero de siniestros: ")
        precio_compra = input("Precio de compra del vehiculo: ")
        vehiculo = AutoUsado.crear_usado(marca, modelo, color, cilindraje, kilometraje, siniestros, precio_compra)
        
    elif opcion == "2":
        print("---------------------------------------------------")
        vehiculo.leer_usado()
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
kilometraje = input("Kilometraje del vehiculo: ")
siniestros = input("Numero de siniestros: ")
precio_compra = input("Precio de compra del vehiculo: ")
vehiculoU = AutoUsado.crear_usado(marca, modelo, color, cilindraje, kilometraje, siniestros, precio_compra)

AutoUsado.leer_usado(vehiculoU)
"""