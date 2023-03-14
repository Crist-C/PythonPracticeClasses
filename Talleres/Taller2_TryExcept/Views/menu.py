
class Menu:
    listaOpcionesMenuPrincipal = ["\n~~~~~~~~~ SISTEMA PARA ADMINISTRAR BIBLIOTECAS ~~~~~~~~~~\n",
                                  " A. Agregar Libro",
                                  " B. Eliminar Libro",
                                  " C. Consultar Libro",
                                  " D. Modificar Libro",
                                  " E. Salir de la aplicación\n\n"]

    listaOpcionesMenuModificacion = [" ~~~~~~~~~ MENÚ MODIFICACIÓN DE LIBROS ~~~~~~~~~~\n",
                                     " J. Modificar Código",
                                     " K. Modificar Título",
                                     " L. Modificar Autor",
                                     " M. Modificar Editorial",
                                     " N. Modificar Numero de existencias",
                                     " O. Regresar al menú anterior"]

    listaOpcionesMenuConsultar = ["\n ~~~~~~~~~ MENU DE CONSULTAS DE LIBROS ~~~~~~~~~~\n",
                                  " F. Consultar por Código",
                                  " G. Consultar por Autor",
                                  " H. Consultar por Editorial",
                                  " I. Regresar al menú anterior\n\n"]

    def menu_consultar(self):
        lista_opciones_validas = ["F", "G", "H", "I"]
        lista_opciones_validas.sort()
        eleccion = 0
        while True:
            for i in self.listaOpcionesMenuConsultar:
                print(i)
            eleccion = input()
            if eleccion in lista_opciones_validas:
                return eleccion
            else:
                print(f"\nIngrese una de las siguientes opciones: {lista_opciones_validas}")
                self.menu_consultar()

    def menu_principal(self):
        lista_opciones_validas = ["A", "B", "C", "D", "E"]
        lista_opciones_validas.sort()
        eleccion = 0
        self.listaOpcionesMenuPrincipal.sort()
        while True:
            for i in self.listaOpcionesMenuPrincipal:
                print(i)
            eleccion = input()
            if eleccion in lista_opciones_validas:
                return eleccion
            else:
                print(f"\nIngrese una de las siguientes opciones: {lista_opciones_validas}")

    def menu_modificar(self):
        lista_opciones_validas = ["J", "K", "L", "M", "N", "O"]
        lista_opciones_validas.sort()
        eleccion = 0
        self.listaOpcionesMenuModificacion.sort()
        while True:
            for i in self.listaOpcionesMenuModificacion:
                print(i)
            eleccion = input()
            if eleccion in lista_opciones_validas:
                return eleccion
            else:
                print(f"\nIngrese una de las siguientes opciones: {lista_opciones_validas}")

    def solicitar_codigo(self):
        codigo = input("Por favor ingrese el código del libro con el siguiente formato AbcD1234: ")
        while True:
            if len(codigo) != 8:
                print("El código debe tener 8 caracteres (4 letras y 4 números).")
            elif not codigo[:4].isalpha() or not codigo[4:].isdigit():
                print("El código debe tener 4 letras seguidas de 4 números.")
            else:
                return codigo.upper()
            codigo = input("Por favor ingrese el código del libro con el siguiente formato AbcD1234: ")

    def solicitar_nombre(self):
        nombre = input("Por favor ingrese el nombre del libro: ")
        return nombre.upper()

    def solicitar_autor(self):
        autor = input("Ingrese el autor de Libro: ")
        while True:
            es_valido = True
            palabras = autor.split()

            if len(palabras) < 2:
                es_valido = False

            for caracter in autor:
                if not caracter.isalpha() and not caracter.isspace():
                    es_valido = False

            if es_valido:
                return autor.upper()
            else:
                print(
                    "Ha ingresado un nombre erroneo.\nVerifique que no haya ingresado algún número e ingrese al menos un nombre y un apellido\n")
            autor = input("Ingrese el autor de Libro: \n")

    def solicitar_editorial(self):
        editorial = input("Ingrese el editorial del Libro: ")
        while True:
            es_valido = True
            for caracter in editorial:
                if not caracter.isalnum() and not caracter.isspace():
                    es_valido = False

            if es_valido:
                return editorial.upper()
            else:
                print(
                    "Ha ingresado un nombre erroneo. No se permite ingresar solamente números\n")
            editorial = input("Ingrese el editorial del Libro: ")

    def solicitar_numero_ejemplares(self):
        while True:
            try:
                ejemplares = int(input("Ingrese el número de ejemplares del Libro: "))
            except ValueError:
                print("Ha ingresado un dato erroneo. Ingrese un tipo de dato numérico\n")
            else:
                return ejemplares

    def mostrar_libro(self, libro):
            print(f"\nCodigo: {libro.codigo}")
            print(f"Nombre del libro: {libro.nombre_libro}")
            print(f"Autor: {libro.autor}")
            print(f"Editorial: {libro.editorial}")
            print(f"Numero de ejemplares: {libro.numero_ejemplares}\n")
            # print(libro.__dict__)

    def mostrar_biblioteca(self, biblioteca):
        for libro in biblioteca:
            self.mostrar_libro(libro)
