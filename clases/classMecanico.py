class Mecanico:

    def __init__(self, id_mec, nombre, telefono, especialidad):
        self.id_mec = id_mec
        self.nombre = nombre
        self.telefono = telefono
        self.especialidad = especialidad

    def crear_nuevo(id_mec, nombre, telefono, especialidad):
        nuevo = Mecanico(id_mec, nombre, telefono, especialidad)
        print("Mecanico ingresado al sistema exitosamente! \n")
        return nuevo
    
    def leer_nuevo(self):
        print("----------------------------------------")
        print("Detalles de propietario...")
        print("Nombre:", self.nombre)
        print("Telefono de contacto:", self.telefono)
        print("Especialidad:", self.especialidad)
        print("----------------------------------------")

    def actualizar_nuevo(self):
        pass

    def eliminar_nuevo(self):
        pass

    def asignar_tarea(self, orden_de_servicio):
        # Lógica para asignar tarea al mecánico
        pass