class Propietario:

    def __init__(self, id_prop, nombre, num_ident, telefono):
        self.id_prop = id_prop
        self.nombre = nombre
        self.num_ident = num_ident
        self.telefono = telefono
    
    def leer_nuevo(self):
        print("----------------------------------------")
        print("Detalles de propietario...")
        print("Nombre:", self.nombre)
        print("Numero de identificacion:", self.num_ident)
        print("Telefono de contacto:", self.telefono)
        print("----------------------------------------")

    def actualizar_nuevo(self):
        pass

    def eliminar_nuevo(self):
        pass