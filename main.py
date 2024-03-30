from clases.classNewCar import *
from clases.classUsedCar import *
from clases.classNewBike import *
from clases.classUsedBike import *
from clases.classVendedor import *
from clases.classPropietario import *
from clases.classCliente import *
from clases.classClientCar import *
from clases.classMecanico import *
from clases.classOrdenDeServicio import *
from menus import *

# LISTAS PARA ALMACENAR INFORMACION DE OBJETOS #
autosNuevos = []
autosUsados = []
autosClientes = []
motosNuevas = []
motosUsadas = []
propietarios = []
vendedores = []
clientes = []
mecanicos = []
ordenes_servicio = []


# OBJETOS QUEMADOS PARA TEST #
newauto1 = AutoNuevo(101,"Chevrolet", "Aveo", "Morado mate", 1600, 4, 2024, 25000000)
usedauto1 = AutoUsado(102,"Chevrolet", "Camaro", "Amarillo mate", 2000, 4, 2010, 50000, 1, 50000000)
usedauto2 = AutoUsado(103,"Kia", "Sportage", "Blanco mate", 2000, 4, 2015, 70000, 0, 56000000)
vendedor1 = Vendedor(14,"Pedro",14,"321")
client1 = Cliente(10, "Juan", 5896, "32454564", 2)
client2 = Cliente(11, "Pedro", 5897, "32459756", 1)
mec1 = Mecanico(5, "Donchi", "23426578", "Pintor")
mec2 = Mecanico(3, "Carlos", "54678965", "Latonero")
mec3 = Mecanico(1, "Armando", "86756752", "Ensamblador", "Ocupado")
order1 = OrdenDeServicio(1, 11, 103, "Choque lateral")
order2 = OrdenDeServicio(2, 10, 102, "Falla de motor")
clientCar1 = AutoCliente(20, "Ford", "Raptor", "Rojo", 2500, 4, 2018)
clientCar2 = AutoCliente(15, "Mazda", "Mazda 2 sedan", "Blanco", 1800, 4, 2019)
autosClientes.append(clientCar1)
autosClientes.append(clientCar2)
autosNuevos.append(newauto1)
clientes.append(client1)
clientes.append(client2)
mecanicos.append(mec1)
mecanicos.append(mec2)
mecanicos.append(mec3)
vendedores.append(vendedor1)
autosUsados.append(usedauto1)
autosUsados.append(usedauto2)
ordenes_servicio.append(order1)
venta = usedauto1.calcular_valor_venta()
print(venta)


# FUNCIONES #
def asignar_orden_servicio_mecanico(orden_servicio, mecanicos):
    for mecanico in mecanicos:
        if mecanico.estado == "Libre":
            mecanico.tomar_orden_servicio(orden_servicio)
            return True
    print("No hay mecánicos disponibles en este momento.")
    return False


# PROGRAMA PRINCIPAL #
while True:
    main_menu()
    opcion1 = input("Opcion: ")

    if opcion1 == "1":
        while True:
            menu_ingresa_vehiculos()
            opcion2 = input("Opcion: ")

            if opcion2 == "1":
                print("- Auto nuevo -")
                identificador = int(input("Identificador del auto: "))
                marca = input("Marca del auto: ")
                modelo = input("Modelo del auto: ")
                color = input("Color del auto: ")
                cilindraje = int(input("Cilindraje del auto: "))
                num_llantas = int(input("Numero de llantas: "))
                anio = int(input("Año del auto: "))
                precio_compra = float(input("Precio de compra del auto: "))
                auto = AutoNuevo(identificador, marca, modelo, color, cilindraje, num_llantas, anio, precio_compra)
                autosNuevos.append(auto)

            elif opcion2 == "2":
                print("- Auto usado -")
                identificador = int(input("Identificador del auto: "))
                marca = input("Marca del auto: ")
                modelo = input("Modelo del auto: ")
                color = input("Color del auto: ")
                cilindraje = int(input("Cilindraje del auto: "))
                num_llantas = int(input("Numero de llantas: "))
                anio = int(input("Año del auto: "))
                kilometraje = int(input("Kilometraje del auto: "))
                siniestros = int(input("Numero de siniestros: "))
                precio_compra = int(input("Precio de compra del auto: "))
                auto = AutoUsado(identificador, marca, modelo, color, cilindraje, num_llantas, anio, kilometraje, siniestros, precio_compra)
                autosUsados.append(auto)

                print("\n- Ingresa propietario anterior -")
                identificador = int(input("Identificador del propietario: "))
                nombre = input("Nombre: ")
                num_ident = input("Numero de identificacion: ")
                telefono = input("Numero de telefono: ")
                propietario = Propietario(identificador, nombre, num_ident, telefono)
                propietarios.append(propietario)

            elif opcion2 == "3":
                print("- Moto nueva -")
                identificador = int(input("Identificador de la moto: "))
                marca = input("Marca de la moto: ")
                modelo = input("Modelo de la moto: ")
                color = input("Color de la moto: ")
                cilindraje = int(input("Cilindraje de la moto: "))
                num_llantas = int(input("Numero de llantas: "))
                anio = int(input("Año de la moto: "))
                precio_compra = int(input("Precio de compra de la moto: "))
                moto = MotoNueva(identificador, marca, modelo, color, cilindraje, num_llantas, anio, precio_compra)
                motosNuevas.append(moto)

            elif opcion2 == "4":
                print("- Moto usada -")
                identificador = int(input("Identificador de la moto: "))
                marca = input("Marca de la moto: ")
                modelo = input("Modelo de la moto: ")
                color = input("Color de la moto: ")
                cilindraje = int(input("Cilindraje de la moto: "))
                num_llantas = int(input("Numero de llantas: "))
                anio = int(input("Año de la moto: "))
                kilometraje = int(input("Kilometraje de la moto: "))
                siniestros = int(input("Numero de siniestros: "))
                precio_compra = int(input("Precio de compra de la moto: "))
                auto = MotoUsada(identificador, marca, modelo, color, cilindraje, num_llantas, anio, kilometraje, siniestros, precio_compra)
                motosUsadas.append(moto)

                print("\n- Ingresa propietario anterior -")
                identificador = int(input("Identificador del propietario: "))
                nombre = input("Nombre: ")
                num_ident = input("Numero de identificacion: ")
                telefono = input("Numero de telefono: ")
                propietario = Propietario(identificador, nombre, num_ident, telefono)
                propietarios.append(propietario)
            
            elif opcion2 == "5":
                print("...")
                break

            else:
                print("Opcion invalida, intente nuevamente")
            
    elif opcion1 == "2":
        while True:
            menu_consulta_vehiculos()
            opcion3 = input("Opcion: ")

            if opcion3 == "1":
                print("- Cosultar auto nuevo -")
                id_nuevo = int(input("Identificador del auto: "))
                for ident in autosNuevos:
                    if ident.id_nuevo == id_nuevo:
                        ident.leer_nuevo()
                        break
                else:
                    print("El auto solicitado no existe\n")
            
            elif opcion3 == "2":
                print("- Cosultar auto usado -")
                id_usado = int(input("Identificador del auto: "))
                for ident in autosUsados:
                    if ident.id_usado == id_usado:
                        ident.leer_usado()
                        break
                else:
                    print("El auto solicitado no existe\n")

            elif opcion3 == "3":
                print("- Cosultar moto nueva -")
                id_nueva = int(input("Identificador de la moto: "))
                for ident in motosNuevas:
                    if ident.id_nueva == id_nueva:
                        ident.leer_nueva()
                        break
                else:
                    print("La moto solicitada no existe\n")

            elif opcion3 == "4":
                print("- Cosultar moto usada -")
                id_usada = int(input("Identificador de la moto: "))
                for ident in motosUsadas:
                    if ident.id_usada == id_usada:
                        ident.leer_nueva()
                        break
                else:
                    print("El auto solicitado no existe\n")

            elif opcion3 == "5":
                break
            
            else:
                print("Opcion invalida, intente nuevamente")

    elif opcion1 == "3":
        while True:
            menu_ingresa_usuarios()
            opcion4 = input("Opcion: ")

            if opcion4 == "1":
                print("- Vendedor -")
                identificador = int(input("Identificador del vendedor: "))
                nombre = input("Nombre: ")
                num_ident = int(input("Numero de identificacion: "))
                telefono = input("Numero de telefono: ")
                vendedor = Vendedor(identificador, nombre, num_ident, telefono)
                vendedores.append(vendedor)

            elif opcion4 == "2":
                print("- Cliente -")
                identificador = int(input("Identificador del cliente: "))
                nombre = input("Nombre: ")
                num_ident = int(input("Numero de identificacion: "))
                telefono = input("Numero de telefono: ")
                num_vehiculos = int(input("Numero de vehiculos: "))
                cliente = Cliente(identificador, nombre, num_ident, telefono, num_vehiculos)
                clientes.append(cliente)

                # Implementacion del ingreso de los vehiculos de los clientes dependiendo del numero que tengan de estos #

            elif opcion4 == "3":
                print("- Mecanico -")
                identificador = int(input("Identificador del mecanico: "))
                nombre = input("Nombre: ")
                telefono = input("Numero de telefono: ")
                print("* Seleccione especialidad del mecanico *")
                print("1. Latonero")
                print("2. Pintor")
                print("3. Ensamblador")
                opcionEsp = input("Opción: ")

                if opcionEsp == "1":
                    especialidad = "Latonero"
                elif opcionEsp == "2":
                    especialidad = "Pintor"
                elif opcionEsp == "3":
                    especialidad = "Ensamblador"
                else:
                    print("Opción no válida.")

                mecanico = Mecanico(identificador, nombre, telefono, especialidad)
                mecanicos.append(mecanico)

            elif opcion4 == "4":
                print("...")
                break

            else:
                print("Opcion invalida, intente nuevamente")

    elif opcion1 == "4":
        while True:
            menu_consulta_usuarios()
            opcion5 = input("Opcion: ")

            if opcion5 == "1":
                print("- Consultar vendedor -")
                id_vend = int(input("Identificador del vendedor: "))
                for ident in vendedores:
                    if ident.id_vend == id_vend:
                        ident.leer_nuevo()
                        break
                else:
                    print("El vendedor solicitado no existe\n")

            elif opcion5 == "2":
                print("- Consultar propietario -")
                id_prop = int(input("Identificador del propietario: "))
                for ident in propietarios:
                    if ident.id_prop == id_prop:
                        ident.leer_nuevo()
                        break
                else:
                    print("El propietario solicitado no existe\n")

            elif opcion5 == "3":
                print("- Consultar cliente -")
                id_cliente = int(input("Identificador del cliente: "))
                for ident in clientes:
                    if ident.id_cliente == id_cliente:
                        ident.leer_nuevo()
                        break
                else:
                    print("El cliente solicitado no existe\n")

            elif opcion5 == "4":
                print("- Consultar mecanico -")
                id_mec = int(input("Identificador del mecanico: "))
                for ident in mecanicos:
                    if ident.id_mec == id_mec:
                        ident.leer_nuevo()
                        break
                else:
                    print("El vendedor solicitado no existe\n")

            elif opcion5 == "5":
                print("...")
                break

            else:
                print("Opcion invalida, intente nuevamente")

    elif opcion1 == "5":
        while True:
            menu_ventas()
            opcion6 = input("Opcion: ")

            if opcion6 == "1":
                print("- Venta auto nuevo -")
                id_ven = int(input("Identificador vendedor: "))
                id_car = int(input("Identificador del auto nuevo que será vendido: "))
                vendedor_encontrado = None
                auto_encontrado = None

                for ident in vendedores:
                    if isinstance(ident, Vendedor) and ident.id_vend == id_ven:
                        vendedor_encontrado = ident
                if vendedor_encontrado:
                
                    for ident in autosNuevos:
                        if isinstance(ident, AutoNuevo) and ident.id_nuevo == id_car:
                            auto_encontrado = ident
                    if auto_encontrado:
                        venta = auto_encontrado.calcular_valor_venta()
                        print(f"Venta del vehiculo con id {id_car} es de ${venta}")
                        comision = vendedor_encontrado.calcular_comision(auto_encontrado)
                        print(f"La comision del vendedor con id {id_ven} es de ${comision}")
                    else:
                        print("El vehiculo no esta en el sistema, verifique")
                        break
                else:
                    print("El vendedor no está en el sistema, verifique")
                    break
                
            elif opcion6 == "2":
                print("- Venta auto usado -")
                id_ven = int(input("Identificador vendedor: "))
                id_car = int(input("Identificador del auto usado que será vendido: "))
                vendedor_encontrado = None
                auto_encontrado = None

                for ident in vendedores:
                    if isinstance(ident, Vendedor) and ident.id_vend == id_ven:
                        vendedor_encontrado = ident
                if vendedor_encontrado:
                
                    for ident in autosUsados:
                        if isinstance(ident, AutoUsado) and ident.id_usado == id_car:
                            auto_encontrado = ident
                    if auto_encontrado:
                        venta = auto_encontrado.calcular_valor_venta()
                        print(f"Venta del vehiculo con id {id_car} es de ${venta}")
                        comision = vendedor_encontrado.calcular_comision(auto_encontrado)
                        print(f"La comision del vendedor con id {id_ven} es de ${comision}")
                    else:
                        print("El vehiculo no esta en el sistema, verifique")
                        break
                else:
                    print("El vendedor no está en el sistema, verifique")
                    break

            elif opcion6 == "3":
                print("- Venta moto nueva -")
                id_ven = int(input("Identificador vendedor: "))
                id_mot = int(input("Identificador de  la moto nueva que será vendida: "))
                vendedor_encontrado = None
                moto_encontrada = None

                for ident in vendedores:
                    if isinstance(ident, Vendedor) and ident.id_vend == id_ven:
                        vendedor_encontrado = ident
                if vendedor_encontrado:
                
                    for ident in motosNuevas:
                        if isinstance(ident, MotoNueva) and ident.id_nueva == id_mot:
                            moto_encontrada = ident
                    if moto_encontrada:
                        venta = moto_encontrada.calcular_valor_venta()
                        print(f"Venta de la moto con id {id_mot} es de ${venta}")
                        comision = vendedor_encontrado.calcular_comision(auto_encontrado)
                        print(f"La comision del vendedor con id {id_ven} es de ${comision}")
                    else:
                        print("La moto no esta en el sistema, verifique")
                        break
                else:
                    print("El vendedor no está en el sistema, verifique")
                    break

            elif opcion6 == "4":
                print("- Venta moto usada -")
                id_ven = int(input("Identificador vendedor: "))
                id_mot = int(input("Identificador de  la moto usada que será vendida: "))
                vendedor_encontrado = None
                moto_encontrada = None

                for ident in vendedores:
                    if isinstance(ident, Vendedor) and ident.id_vend == id_ven:
                        vendedor_encontrado = ident
                if vendedor_encontrado:
                
                    for ident in motosUsadas:
                        if isinstance(ident, MotoUsada) and ident.id_usada == id_mot:
                            moto_encontrada = ident
                    if moto_encontrada:
                        venta = moto_encontrada.calcular_valor_venta()
                        print(f"Venta de la moto con id {id_mot} es de ${venta}")
                        comision = vendedor_encontrado.calcular_comision(auto_encontrado)
                        print(f"La comision del vendedor con id {id_ven} es de ${comision}")
                    else:
                        print("La moto no esta en el sistema, verifique")
                        break
                else:
                    print("El vendedor no está en el sistema, verifique")
                    break

            elif opcion6 == "5":
                print("...")
                break

            else:
                print("opcion invalida, intente nuevamente")

    if opcion1 == "6":
        while True:
            menu_ordenesS()
            opcion7 = input("Opcion: ")

            if opcion7 == "1":
                print("- Crea una orden -")
                id_ord = int(input("Ingresa identificador de la orden: "))
                id_cli = int(input("Identificador cliente: "))
                id_veh = int(input("Identificador del auto: "))
                descripcion_problema = input("Descripcion del problema: ")
                cliente_encontrado = None
                auto_encontrado = None

                for ident in clientes:
                    if isinstance(ident, Cliente) and ident.id_cliente == id_cli:
                        cliente_encontrado = ident
                if cliente_encontrado:
                    print("-------------------------------------------------------------------")
                    print(f"Cliente: {cliente_encontrado.nombre}")                
                    for ident in autosClientes:
                        if isinstance(ident, AutoCliente) and ident.id_car == id_veh:
                            auto_encontrado = ident
                    if auto_encontrado:
                        print(f"Vehiculo: {auto_encontrado.marca}")
                        auto_encontrado.actualizar_estado_vehiculo()
                        if auto_encontrado.estado == "En reparacion":
                            orden_servicio = OrdenDeServicio(id_ord, id_cli, id_veh, descripcion_problema)
                            ordenes_servicio.append(orden_servicio)
                            orden_servicio.ver_orden() 

                        # Asignar orden de servicio a un mecánico
                        asignar = asignar_orden_servicio_mecanico(orden_servicio, mecanicos)

                        if asignar:
                            print("\nEstado actual de los mecánicos:")
                            for mecanico in mecanicos:
                                print(f"{mecanico.nombre}: {mecanico.estado}")
                        print("----------------------------------------")
                              
                    else:
                        print("El vehiculo no esta en el sistema, verifique")
                        break
                else:
                    print("El cliente no está en el sistema, verifique")
                    break
            
            elif opcion7 == "2":
                print("- Busca una orden -")
                id_ord = int(input("Identificador de la orden: "))
                orden_encontrada = None

                for ident in ordenes_servicio:
                    if isinstance(ident, OrdenDeServicio) and ident.id_orden == id_ord:
                        orden_encontrada = ident
                if orden_encontrada:
                    orden_encontrada.ver_orden()
                    orden_encontrada.actualizar_estado_orden()
                    orden_encontrada.ver_orden()
                    
                else:
                    print("La orden no esta registrada en el sistema, verifique")
                    break

            elif opcion7 == "3":
                print("...")
                break

            else:
                print("Opcion invalida, intente nuevamente")

    elif opcion1 == "7":
        print("Hasta pronto!")
        break

    else:
        print("Opcion invalida, intente nuevamente")
    
    

