class Mecanico:

    especialidades_mec = ["Latonero", "Pintor", "Ensamblador"]
    estados_mec = ["Libre", "Ocupado"]

    def __init__(self, id_mec, nombre, telefono, especialidad, estado="Libre"):
        self.id_mec = id_mec
        self.nombre = nombre
        self.telefono = telefono
        if especialidad in self.especialidades_mec:
            self.especialidad = especialidad
        if estado in self.estados_mec:
            self.estado = estado

    def leer_nuevo(self):
        print("----------------------------------------")
        print("Detalles de mecanico...")
        print("Nombre:", self.nombre)
        print("Telefono de contacto:", self.telefono)
        print("Especialidad:", self.especialidad)
        print("Estado: ", self.estado)
        print("----------------------------------------")

    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado in self.estados_mec:
            self.estado = nuevo_estado
        else:
            print("Estado no válido.")

    def actualizar_estado_mecanico(self):
        print("* Seleccione el estado del mecanico *")
        print("1. Libre")
        print("2. Ocupado")
        opcion = input("Opción: ")

        if opcion == "1":
            self.cambiar_estado("Libre")
        elif opcion == "2":
            self.cambiar_estado("Ocupado")
        else:
            print("Opción no válida.")

    def tomar_orden_servicio(self, orden_servicio):
        if self.estado == "Libre":
            self.orden_servicio = orden_servicio
            self.estado = "Ocupado"
            print(f"{self.nombre} ha tomado la orden de servicio.")
        else:
            print(f"{self.nombre} está ocupado en otra tarea.")

    def actualizar_nuevo(self):
        pass

    def eliminar_nuevo(self):
        pass

