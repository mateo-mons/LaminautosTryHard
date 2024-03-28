class Mecanico:
    estados_mec = ["Libre", "Ocupado"]

    def __init__(self, id_mec, nombre, telefono, especialidad, estado):
        self.id_mec = id_mec
        self.nombre = nombre
        self.telefono = telefono
        self.especialidad = especialidad
        if estado in self.estados_mec:
            self.estado = estado
        else:
            print("Estado no válido.")
    
    def leer_nuevo(self):
        print("----------------------------------------")
        print("Detalles de mecanico...")
        print("Nombre:", self.nombre)
        print("Telefono de contacto:", self.telefono)
        print("Especialidad:", self.especialidad)
        print("Estado: ", self.estado)
        print("----------------------------------------")

    def actualizar_nuevo(self):
        pass

    def eliminar_nuevo(self):
        pass

    def asignar_tarea(self, orden_de_servicio):
        # Lógica para asignar tarea al mecánico
        pass