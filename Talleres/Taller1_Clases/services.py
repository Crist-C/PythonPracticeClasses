from Talleres.Taller1_Clases.dataBase import DataBase
from Talleres.Taller1_Clases.utils import Utils


class Services:
    main_object = None

    def __init__(self, menu_):
        self.menus = menu_

    def set_main_object(self, main_):
        self.main_object = main_

    def consultar_por(self, campo_de_busqueda, valor_a_buscar, lista_de_elementos):
        lista_de_coincidencias = []
        for elemento_en_lista in lista_de_elementos:
            if elemento_en_lista[campo_de_busqueda] == valor_a_buscar:
                lista_de_coincidencias.append(elemento_en_lista);
        if len(lista_de_coincidencias) != 0:
            return lista_de_coincidencias
        return False;

    def opcion_crear(self):
        ### Solicita el código y valida que sea numérico
        codigo = input("Ingrese el código del elemento: \n")
        if codigo.isdigit():
            ## Si el código NO existe entonces lo agrega
            if not self.consultar_por("Codigo", int(codigo), DataBase.lista):
                DataBase.elemento["Codigo"] = int(codigo)
            else:
                print("El código ya existe.\nintentelo nuevamente insertando un código que no exista.\n")
                self.opcion_crear()

            ## De lo contrario el usuario debe iniciar de nuevo la creación del elemento
        else:
            print("Ha ingresado un dato erroneo.\nintentelo nuevamente insertando un dato numérico\n")
            self.opcion_crear()

        ### Solicita el tipo de elemento y valida que no contenga números
        tipo = input("Ingrese el tipo de elemento: \n")
        if tipo.isalpha():
            DataBase.elemento["Tipo"] = tipo
        else:
            print("Ha ingresado un dato erroneo. Ingrese un tipo de dato numérico\n")
            self.opcion_crear()

        ### Solicita el fabricante del elemento y valida que sea alfanumérico
        fabricante = input("Ingrese el fabricante de elemento: \n")
        if fabricante.isalnum():
            DataBase.elemento["Fabricante"] = fabricante
        else:
            print("Ha ingresado un dato erroneo. Ingrese un tipo de dato numérico\n")
            self.opcion_crear()

        ### Solicita el precio del elemento y valida que sea numérico
        precio = input("Ingrese el precio por unidad del elemento: \n")
        if precio.isdigit():
            DataBase.elemento["Precio"] = int(precio)
        else:
            print("Ha ingresado un dato erroneo. Ingrese un tipo de dato numérico\n")
            self.opcion_crear()

        ### Solicita la cantidad de items del elemento y valida que sea numérico
        items = input("Ingrese la cantidad de items en stock: \n")
        if items.isdigit():
            DataBase.elemento["Items"] = int(items)
        else:
            print("Ha ingresado un dato erroneo. Ingrese un tipo de dato numérico\n")
            self.opcion_crear()

        ### Agrega el elemento a la lista
        DataBase.lista.append(DataBase.elemento.copy())
        # print(lista)

    def opcion_eliminar(self):
        codigo_del_elemento_a_eliminar = input(
            "Ingrese el código del elemento que desea ELIMINAR\nó cualquier letra para volver al menú anterior: \n")
        if codigo_del_elemento_a_eliminar.isdigit():
            elemento_a_eliminar = self.consultar_por("Codigo", int(codigo_del_elemento_a_eliminar), DataBase.lista)
            if not elemento_a_eliminar:
                print("No existe un elemento con ese código.\nintentelo nuevamente.\n")
                self.opcion_eliminar()
        else:
            print("Ha escogido volver al menú anterior.\n")
            self.main_object.main()

        print("El elemento que se eliminará es: ")
        Utils.mostrar_elemento(elemento_a_eliminar[0])
        confirmacion = input("Confirma eliminar el elemento? (Y/N):")
        if confirmacion.upper() == "Y":
            DataBase.lista.remove(elemento_a_eliminar[0])
            print("elemento eleminado")
        self.main_object.main()

    def opcion_consultar(self):
        eleccion = self.menus.menuConsultar()

        if eleccion == "H":
            self.main_object.main()
        if eleccion == "F":

            codigo_para_consultar = input("Ingrese el código del elemento: \n")

            if codigo_para_consultar.isdigit():
                elementos_consultados = self.consultar_por("Codigo", int(codigo_para_consultar), DataBase.lista)
                if elementos_consultados == False:
                    print("El elemento no existe en la lista.")
                    self.opcion_consultar()
                else:
                    for elemento in elementos_consultados:
                        Utils.mostrar_elemento(elemento)
                    self.opcion_consultar()

                ## De lo contrario el usuario debe iniciar de nuevo la creación del elemento
            else:
                print("Ha ingresado un dato erroneo.\nintentelo nuevamente insertando un dato numérico\n")
                self.opcion_consultar()

        if eleccion == "G":

            fabricante_para_consultar = input("Ingrese el nombre del Fabricante del elemento: \n")

            if fabricante_para_consultar.isalnum():
                elementos_consultados = self.consultar_por("Fabricante", fabricante_para_consultar, DataBase.lista)
                if elementos_consultados == False:
                    print("No existen elementos en la lista de ese fabricante.")
                    self.opcion_consultar()
                else:
                    for elemento in elementos_consultados:
                        Utils.mostrar_elemento(elemento)
                    self.opcion_consultar()

                ## De lo contrario el usuario debe iniciar de nuevo la creación del elemento
            else:
                print("Ha ingresado un dato erroneo.\nintentelo nuevamente insertando un dato numérico\n")
                self.opcion_consultar()

    def opcion_modificar(self):

        elemento_actualizado = False

        codigo_del_elemento_a_modificar = ""

        codigo_del_elemento_a_modificar = input(
            "\nPara hacer una modificación, primero ingrese el código del elemento que desea modificar: \n")
        print(f"El valor ingesado es: {codigo_del_elemento_a_modificar}")

        if codigo_del_elemento_a_modificar.isdigit():
            elemento_a_modificar = self.consultar_por("Codigo", int(codigo_del_elemento_a_modificar), DataBase.lista)
            if not elemento_a_modificar:
                print("No existe un elemento con ese código.\n")
                self.opcion_modificar()
        else:
            print("Ha ingresado un dato erroneo.\nintentelo nuevamente insertando un dato numérico\n")
            self.opcion_modificar()

        codigo_del_elemento_a_modificar = int(codigo_del_elemento_a_modificar)

        print("\nEl elemento a modificar es UNO : ")
        Utils.mostrar_elemento(elemento_a_modificar[0])
        # print(
        #    f"Codigo:{elemento_a_modificar[0]['Codigo']}, Tipo: {elemento_a_modificar[0]['Tipo']}, Fabricante: {elemento_a_modificar[0]['Fabricante']}, Precio: {elemento_a_modificar[0]['Precio']}, Items: {elemento_a_modificar[0]['Items']}\n")

        eleccion = self.menus.menuModificar()

        if eleccion == "N":
            self.main_object.main()

        if eleccion == "I":
            nuevo_valor = input("Ingrese el nuevo código del elemento: \n")
            if nuevo_valor.isdigit():
                if self.consultar_por("Codigo", int(nuevo_valor), DataBase.lista):
                    print("Ya existe un elemento con este código. Intentelo nuevamente")
                    self.opcion_modificar()
                else:
                    self.modificarCampo(codigo_del_elemento_a_modificar, "Codigo", int(nuevo_valor), DataBase.lista)
                    elemento_actualizado = self.consultar_por("Codigo", int(nuevo_valor), DataBase.lista)
                    codigo_del_elemento_a_modificar = int(nuevo_valor)
                print("Campo modificado")
            else:
                print("Ha ingresado un dato erroneo.\nintentelo nuevamente insertando un dato numérico\n")
                self.opcion_modificar()

        if eleccion == "J":
            nuevo_valor = input("Ingrese el nuevo tipo del elemento: \n")
            if nuevo_valor.isalpha():
                self.modificarCampo(codigo_del_elemento_a_modificar, "Tipo", nuevo_valor, DataBase.lista)
                print("Campo modificado")
            else:
                print("Ha ingresado un dato erroneo.\nintentelo nuevamente insertando un valor sin números\n")
                self.opcion_modificar()

        if eleccion == "K":
            nuevo_valor = input("Ingrese el nuevo fabricante del elemento: \n")
            if nuevo_valor.isalnum():
                self.modificarCampo(codigo_del_elemento_a_modificar, "Fabricante", nuevo_valor, DataBase.lista)
                print("Campo modificado")
            else:
                print("Ha ingresado un dato erroneo.\nintentelo nuevamente.\n")
                self.opcion_modificar()

        if eleccion == "L":
            nuevo_valor = input("Ingrese el nuevo Precio del elemento: \n")
            if nuevo_valor.isdigit():
                self.modificarCampo(codigo_del_elemento_a_modificar, "Precio", int(nuevo_valor), DataBase.lista)
                print("Campo modificado")
            else:
                print("Ha ingresado un dato erroneo.\nintentelo nuevamente insertando un dato numérico\n")
                self.opcion_modificar()

        if eleccion == "M":
            nuevo_valor = input("Ingrese la nueva cantidad de items del elemento en stock: \n")
            if nuevo_valor.isdigit():
                self.modificarCampo(codigo_del_elemento_a_modificar, "Items", int(nuevo_valor), DataBase.lista)
                print("Campo modificado")
            else:
                print("Ha ingresado un dato erroneo.\nintentelo nuevamente insertando un dato numérico\n")
                self.opcion_modificar()

        if not elemento_actualizado:
            elemento_actualizado = self.consultar_por("Codigo", int(codigo_del_elemento_a_modificar), DataBase.lista)
        print("\nEl elemento modificado es:")
        Utils.mostrar_elemento(elemento_actualizado[0])
        self.main_object.main()

    def modificarCampo(self, codigo, campo_a_modificar, nuevo_valor, lista_elementos):
        for elemento_a_modificar in lista_elementos:
            if elemento_a_modificar["Codigo"] == codigo:
                elemento_a_modificar[campo_a_modificar] = nuevo_valor
                # print(f"{campo_a_modificar}: {elemento_a_modificar[campo_a_modificar]}")
                break
