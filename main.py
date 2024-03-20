from clases.classNewCar import *
from clases.classUsedCar import *
from clases.classNewBike import *
from clases.classUsedBike import *
from clases.classVendedor import *
from clases.classPropietario import *
from clases.classCliente import *
from clases.classMecanico import *
from clases.classOrdenDeServicio import *
from menus import *

# LISTAS PARA ALMACENAR INFORMACION #
autosNuevos = []
autosUsados = []
motosNuevas = []
motosUsadas = []
propietarios = []
vendedores = []
clientes = []
mecanicos = []


while True:
    main_menu()
    opcion1 = input("Opcion: ")

    if opcion1 == "1":
        while True:
            menu_ingresa_vehiculos()
            opcion2 = input("Opcion: ")

            if opcion2 == "1":
                print("- Auto nuevo -")
                identificador = input("Identificador del auto: ")
                marca = input("Marca del auto: ")
                modelo = input("Modelo del auto: ")
                color = input("Color del auto: ")
                cilindraje = input("Cilindraje del auto: ")
                num_llantas = input("Numero de llantas: ")
                anio = input("Año del auto: ")
                precio_compra = input("Precio de compra del auto: ")
                auto = AutoNuevo.crear_nuevo(identificador, marca, modelo, color, cilindraje, num_llantas, anio, precio_compra)
                autosNuevos.append(auto)

            elif opcion2 == "2":
                print("- Auto usado -")
                identificador = input("Identificador del auto: ")
                marca = input("Marca del auto: ")
                modelo = input("Modelo del auto: ")
                color = input("Color del auto: ")
                cilindraje = input("Cilindraje del auto: ")
                num_llantas = input("Numero de llantas: ")
                anio = input("Año del auto: ")
                kilometraje = input("Kilometraje del auto: ")
                siniestros = input("Numero de siniestros: ")
                precio_compra = input("Precio de compra del auto: ")
                auto = AutoUsado.crear_usado(identificador, marca, modelo, color, cilindraje, num_llantas, anio, kilometraje, siniestros, precio_compra)
                autosUsados.append(auto)

            elif opcion2 == "3":
                print("- Moto nueva -")
                identificador = input("Identificador de la moto: ")
                marca = input("Marca de la moto: ")
                modelo = input("Modelo de la moto: ")
                color = input("Color de la moto: ")
                cilindraje = input("Cilindraje de la moto: ")
                num_llantas = input("Numero de llantas: ")
                anio = input("Año de la moto: ")
                precio_compra = input("Precio de compra de la moto: ")
                moto = MotoNueva.crear_nueva(identificador, marca, modelo, color, cilindraje, num_llantas, anio, precio_compra)
                motosNuevas.append(moto)

            elif opcion2 == "4":
                print("- Moto usada -")
                identificador = input("Identificador de la moto: ")
                marca = input("Marca de la moto: ")
                modelo = input("Modelo de la moto: ")
                color = input("Color de la moto: ")
                cilindraje = input("Cilindraje de la moto: ")
                num_llantas = input("Numero de llantas: ")
                anio = input("Año de la moto: ")
                kilometraje = input("Kilometraje de la moto: ")
                siniestros = input("Numero de siniestros: ")
                precio_compra = input("Precio de compra de la moto: ")
                auto = MotoUsada.crear_usada(identificador, marca, modelo, color, cilindraje, num_llantas, anio, kilometraje, siniestros, precio_compra)
                motosUsadas.append(moto)
            
            elif opcion2 == "5":
                print("...")
                break

            else:
                print("Opcion incorrecta, intente nuevamente")
            
    elif opcion1 == "2":
        while True:
            menu_consulta_vehiculos()
            opcion3 = input("Opcion: ")

            if opcion3 == "1":
                print("- Cosultar auto nuevo -")
                id_nuevo = input("Identificador del auto: ")
                for ident in autosNuevos:
                    if ident.id_nuevo == id_nuevo:
                        ident.leer_nuevo()
                        break
                else:
                    print("El auto solicitado no existe\n")
            
            elif opcion3 == "2":
                print("- Cosultar auto usado -")
                id_usado = input("Identificador del auto: ")
                for ident in autosUsados:
                    if ident.id_usado == id_usado:
                        ident.leer_usado()
                        break
                else:
                    print("El auto solicitado no existe\n")

            elif opcion3 == "3":
                print("- Cosultar moto nueva -")
                id_nueva = input("Identificador de la moto: ")
                for ident in motosNuevas:
                    if ident.id_nueva == id_nueva:
                        ident.leer_nueva()
                        break
                else:
                    print("La moto solicitada no existe\n")

            elif opcion3 == "4":
                print("- Cosultar moto usada -")
                id_usada = input("Identificador de la moto: ")
                for ident in motosUsadas:
                    if ident.id_usada == id_usada:
                        ident.leer_nueva()
                        break
                else:
                    print("El auto solicitado no existe\n")

            elif opcion3 == "5":
                print("...")
                break
            
            else:
                print("Opcion incorrecta, intente nuevamente")

    elif opcion1 == "3":
        while True:
            menu_ingresa_usuarios()
            opcion4 = input("Opcion: ")

            if opcion4 == "1":
                print("- Vendedor -")
                identificador = input("Identificador del vendedor: ")
                nombre = input("Nombre: ")
                num_ident = input("Numero de identificacion: ")
                telefono = input("Numero de telefono: ")
                vendedor = Vendedor.crear_nuevo(identificador, nombre, num_ident, telefono)
                vendedores.append(vendedor)

            elif opcion4 == "2":
                print("- Propietario -")
                identificador = input("Identificador del propietario: ")
                nombre = input("Nombre: ")
                num_ident = input("Numero de identificacion: ")
                telefono = input("Numero de telefono: ")
                propietario = Propietario.crear_nuevo(identificador, nombre, num_ident, telefono)
                propietarios.append(propietario)

            elif opcion4 == "3":
                print("- Cliente -")
                identificador = input("Identificador del cliente: ")
                nombre = input("Nombre: ")
                num_ident = input("Numero de identificacion: ")
                telefono = input("Numero de telefono: ")
                num_vehiculos = input("Numero de vehiculos: ")
                cliente = Cliente.crear_nuevo(identificador, nombre, num_ident, telefono, num_vehiculos)
                clientes.append(cliente)

            elif opcion4 == "4":
                print("- Mecanico -")
                identificador = input("Identificador del mecanico: ")
                nombre = input("Nombre: ")
                telefono = input("Numero de telefono: ")
                especialidad = input("Especialidad: ")
                mecanico = Mecanico.crear_nuevo(identificador, nombre, telefono, especialidad)
                mecanicos.append(mecanico)

            elif opcion4 == "5":
                print("...")
                break

            else:
                print("Opcion incorrecta, intente nuevamente")

    elif opcion1 == "4":
        while True:
            menu_consulta_usuarios()
            opcion5 = input("Opcion: ")

            if opcion5 == "1":
                print("- Consultar vendedor -")
                id_vend = input("Identificador del vendedor: ")
                for ident in vendedores:
                    if ident.id_vend == id_vend:
                        ident.leer_nuevo()
                        break
                else:
                    print("El vendedor solicitado no existe\n")

            elif opcion5 == "2":
                print("- Consultar propietario -")
                id_prop = input("Identificador del propietario: ")
                for ident in propietarios:
                    if ident.id_prop == id_prop:
                        ident.leer_nuevo()
                        break
                else:
                    print("El propietario solicitado no existe\n")

            elif opcion5 == "3":
                print("- Consultar cliente -")
                id_cliente = input("Identificador del cliente: ")
                for ident in clientes:
                    if ident.id_cliente == id_cliente:
                        ident.leer_nuevo()
                        break
                else:
                    print("El cliente solicitado no existe\n")

            elif opcion5 == "4":
                print("- Consultar mecanico -")
                id_mec = input("Identificador del mecanico: ")
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
                print("Opcion incorrecta, intente nuevamente")

    elif opcion1 == "5":
        pass

    elif opcion1 == "6":
        pass

    elif opcion1 == "7":
        print("Hasta pronto")
        break

    else:
        print("Opcion incorrecta, intente nuevamente")
    
    


