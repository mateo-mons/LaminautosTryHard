class Cliente:

    def __init__(self, id_cliente, nombre, num_ident, telefono, num_vehiculos):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.num_ident = num_ident
        self.telefono = telefono
        self.num_vehiculos = num_vehiculos

    def crear_nuevo(id_cliente, nombre, num_ident, telefono, num_vehiculos):
        nuevo = Cliente(id_cliente, nombre, num_ident, telefono, num_vehiculos)
        print("Cliente ingresado al sistema exitosamente! \n")
        return nuevo
    
    def leer_nuevo(self):
        print("----------------------------------------")
        print("Detalles de propietario...")
        print("Nombre:", self.nombre)
        print("Numero de identificacion:", self.num_ident)
        print("Telefono de contacto:", self.telefono)
        print("Numero de vehiculos:", self.num_vehiculos)
        print("----------------------------------------")

    def actualizar_nuevo(self):
        pass

    def eliminar_nuevo(self):
        pass