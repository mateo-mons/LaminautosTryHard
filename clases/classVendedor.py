class Vendedor:

    def __init__(self, id_vend, nombre, num_ident, telefono):
        self.id_vend = id_vend
        self.nombre = nombre
        self.num_ident = num_ident
        self.telefono = telefono

    def crear_nuevo(id_vend, nombre, num_ident, telefono):
        nuevo = Vendedor(id_vend, nombre, num_ident, telefono)
        print("Vendedor ingresado al sistema exitosamente! \n")
        return nuevo
    
    def leer_nuevo(self):
        print("----------------------------------------")
        print("Detalles del vendedor...")
        print("Nombre:", self.nombre)
        print("Numero de identificacion:", self.num_ident)
        print("Telefono de contacto:", self.telefono)
        print("----------------------------------------")

    def actualizar_nuevo(self):
        pass

    def eliminar_nuevo(self):
        pass