from Talleres.Taller2_TryExcept.Models.dataBase import DataBase
from Talleres.Taller2_TryExcept.Controllers.utils import Utils
from Talleres.Taller2_TryExcept.Models.libro import Libro


class Services:
    main_object = None

    def __init__(self, menu_):
        self.menus = menu_

    def set_main_object(self, main_):
        self.main_object = main_

    def consultar_por(self, campo_de_busqueda, valor_a_buscar, lista_de_elementos):
        lista_de_coincidencias = []

        for elemento_en_lista in lista_de_elementos:
            if hasattr(elemento_en_lista, campo_de_busqueda) and getattr(elemento_en_lista,
                                                                         campo_de_busqueda) == valor_a_buscar:
                lista_de_coincidencias.append(elemento_en_lista);

        if len(lista_de_coincidencias) != 0:
            return lista_de_coincidencias

        return False;

    def validar_si_existe_elemento_por_codigo(self, codigo):
        # Validamos si existe el código en la base de datos
        if self.consultar_por("codigo", codigo, DataBase.BaseDeDatos):
            return True
        else:
            return False

    def opcion_crear(self):

        libro = Libro("", "", "", "", 0)

        # 1. Solicita el código y valida que sea numérico
        codigo = self.menus.solicitar_codigo()

        # Validamos si existe el código en la base de datos
        if self.validar_si_existe_elemento_por_codigo(codigo):
            print("El código ya existe.\nintentelo nuevamente insertando un código que no exista.\n")
            self.opcion_crear()
        else:
            libro.codigo = codigo

        # 2. Solicita el nomobre del Libro
        nombre = self.menus.solicitar_nombre()
        libro.nombre_libro = nombre

        # 3. Solicita el Autor del Libro y valida que sea alfanumérico
        autor = self.menus.solicitar_autor()
        libro.autor = autor

        # 4. Solicita el Editorial del Libro y valida que sea alfanumérico
        editorial = self.menus.solicitar_editorial()
        libro.editorial = editorial

        # 5. Solicita el numero de ejemplares del Libro y valida que sea numérico
        numero_ejemplares = self.menus.solicitar_numero_ejemplares()
        libro.numero_ejemplares = numero_ejemplares

        # Agrega el Libro a la lista
        DataBase.BaseDeDatos.append(libro)
        print("\nLibro agregado a la biblioteca con éxito")
        self.menus.mostrar_biblioteca(DataBase.BaseDeDatos)

    def opcion_eliminar(self):

        codigo_del_elemento_a_eliminar = self.menus.solicitar_codigo()

        if self.validar_si_existe_elemento_por_codigo(codigo_del_elemento_a_eliminar):
            # Como si existe el elemento, lo leemos de la BD
            Libro_a_eliminar = self.consultar_por("codigo", codigo_del_elemento_a_eliminar, DataBase.BaseDeDatos)
        else:
            print("No existe ningún libro con ese ID")
            self.main_object.main()

        print(f"\nEl Libro que se eliminará es: ")
        self.menus.mostrar_biblioteca(Libro_a_eliminar)

        while True:
            try:
                confirmacion = input("\nConfirma eliminar el Libro? (Y/N):")
            except ValueError:
                print("Valor incorrecto, ingreselo nuevamente")
            else:
                if confirmacion.upper() == "Y":
                    DataBase.BaseDeDatos.remove(Libro_a_eliminar[0])
                    self.menus.mostrar_biblioteca(DataBase.BaseDeDatos)
                    print("Libro eliminado")
                    break
                if confirmacion.upper() == "N":
                    print("NO se ha eliminado nungún Libro")
                    break
        self.main_object.main()

    def opcion_consultar(self):

        eleccion = self.menus.menu_consultar()

        if eleccion == "I":
            self.main_object.main()

        if eleccion == "F":

            codigo_para_consultar = self.menus.solicitar_codigo()

            libros_consultados = self.consultar_por("codigo", codigo_para_consultar, DataBase.BaseDeDatos)
            if not libros_consultados:
                print("El libro no existe en la biblioteca.")
                self.opcion_consultar()
            else:
                self.menus.mostrar_biblioteca(libros_consultados)
            self.opcion_consultar()

        if eleccion == "G":

            autor_para_consultar = self.menus.solicitar_autor()

            libros_consultados = self.consultar_por("autor", autor_para_consultar, DataBase.BaseDeDatos)
            if not libros_consultados:
                print("No existen Libros en la lista de ese Autor.")
                self.opcion_consultar()
            else:
                self.menus.mostrar_biblioteca(libros_consultados)
            self.opcion_consultar()

        if eleccion == "H":

            editorial_para_consultar = self.menus.solicitar_editorial()

            libros_consultados = self.consultar_por("editorial", editorial_para_consultar, DataBase.BaseDeDatos)
            if not libros_consultados:
                print("No existen Libros en la lista de esa editorial.")
                self.opcion_consultar()
            else:
                self.menus.mostrar_biblioteca(libros_consultados)
            self.opcion_consultar()

    def opcion_modificar(self):

        libro_actualizado = False

        # Solicitamos el código al usuario
        print("\nPara hacer una modificación, primero ingrese el código del Libro que desea modificar")
        codigo_del_elemento_a_modificar = self.menus.solicitar_codigo()

        # Buscamos el líbro por código. Si no existe, se muestra un mensaje al usuario
        libro_a_modificar = self.consultar_por("codigo", codigo_del_elemento_a_modificar, DataBase.BaseDeDatos)
        if not libro_a_modificar:
            print("No existe un Libro con ese código.\n")
            self.opcion_modificar()

        # Mostramos el libro encontrado
        print("El Libro escogido es :")
        libro_a_modificar[0].mostrar()

        # Mostramos el menú de modificar solicitando la opción deseada
        eleccion = self.menus.menu_modificar()

        # Si es O, retorna al menú principal
        if eleccion == "O":
            self.main_object.main()

        # Si es J, modificamos el código
        if eleccion == "J":
            self.opcion_modificar_codigo(codigo_del_elemento_a_modificar)

        # Si es K, modificamos el título del libro
        if eleccion == "K":
            self.opcion_modificar_titulo(codigo_del_elemento_a_modificar)

        # Si es K, modificamos el Autor
        if eleccion == "L":
            self.opcion_modificar_autor(codigo_del_elemento_a_modificar)

        # Si es M, modificamos el Editorial
        if eleccion == "M":
            self.opcion_modificar_editorial(codigo_del_elemento_a_modificar)

        if eleccion == "N":
            self.opcion_modificar_numero_existencias(codigo_del_elemento_a_modificar)

        '''
        if not libro_actualizado:
            libro_actualizado = self.consultar_por("codigo", codigo_del_elemento_a_modificar, DataBase.BaseDeDatos)
        print("\nEl Libro modificado es:")
        libro_actualizado[0].get_libro_like_dictionary()
        self.main_object.main()
        '''

    def opcion_modificar_codigo(self, codigo_del_elemento_a_modificar):

        # Solicitamos el nuevo código
        print("El CÓDIGO que se le solicitará será el NUEVO código del Libro\n")
        nuevo_valor = self.menus.solicitar_codigo()

        if nuevo_valor == codigo_del_elemento_a_modificar:
            print("El código ingresado es el original del libro")
            self.opcion_modificar()

        # Validamos si ya existe un libro con ese nuevo código
        if self.validar_si_existe_elemento_por_codigo(nuevo_valor):
            print("Ya existe un Libro con este código. Intentelo nuevamente")
            self.opcion_modificar()

        # Si no existe entonces modificamos el código
        else:
            self.modificar_campo(codigo_del_elemento_a_modificar, "codigo", nuevo_valor, DataBase.BaseDeDatos)

        self.opcion_modificar()

    def opcion_modificar_titulo(self, codigo_del_elemento_a_modificar):

        print("El NOMBRE que se le solicitará será el NUEVO TÍTULO del Libro\n")
        nuevo_valor = self.menus.solicitar_nombre()

        self.modificar_campo(codigo_del_elemento_a_modificar, "nombre_libro", nuevo_valor, DataBase.BaseDeDatos)
        self.opcion_modificar()

    def opcion_modificar_autor(self, codigo_del_elemento_a_modificar):
        print("El AUTOR que se le solicitará será el NUEVO AUTOR del Libro\n")
        nuevo_valor = self.menus.solicitar_autor()

        self.modificar_campo(codigo_del_elemento_a_modificar, "autor", nuevo_valor, DataBase.BaseDeDatos)
        print("Campo modificado")

        self.opcion_modificar()

    def opcion_modificar_editorial(self, codigo_del_elemento_a_modificar):

        print("El EDITORIAL que se le solicitará será el NUEVO EDITORIAL del Libro\n")
        nuevo_valor = self.menus.solicitar_editorial()

        self.modificar_campo(codigo_del_elemento_a_modificar, "editorial", nuevo_valor, DataBase.BaseDeDatos)
        self.opcion_modificar()

    def opcion_modificar_numero_existencias(self, codigo_del_elemento_a_modificar):

        print("El NUMERO DE EXISTENCIAS que se le solicitará será el NUEVO NUMERO DE EXISTENCIAS del Libro\n")
        nuevo_valor = self.menus.solicitar_numero_ejemplares()

        self.modificar_campo(codigo_del_elemento_a_modificar, "numero_ejemplares", nuevo_valor, DataBase.BaseDeDatos)
        print("Campo modificado")

        self.opcion_modificar()

    # Codigo del Libro que se desea modificar
    # Nombre del atributo que se desea modificar del Libro
    # El nuevo valor que tomará ese atriburo
    # La lista en donde se debe buscar el Libro
    def modificar_campo(self, codigo, atributo_a_modificar, nuevo_valor, lista_elementos):

        for libro_a_modificar in lista_elementos:
            if getattr(libro_a_modificar, "codigo") == codigo:
                setattr(libro_a_modificar, atributo_a_modificar, nuevo_valor)
                print("\nLibro modificado: ")
                libro_a_modificar.mostrar()
                break
            else:
                print("Libro no modificado")