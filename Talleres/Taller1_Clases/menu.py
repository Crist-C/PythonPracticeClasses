
class Menu:

    listaOpcionesMenuPrincipal = ["\n~~~~~~~~~ SISTEMA PARA ADMINISTRAR INVENTARIOS ~~~~~~~~~~\n",
                                  " A. Crear Item",
                                  " B. Eliminar Item",
                                  " C. Consultar Item",
                                  " D. Modificar Item",
                                  " E. Salir\n\n"]

    listaOpcionesMenuModificacion = [" ~~~~~~~~~ MENÚ MODIFICACIÓN ~~~~~~~~~~\n", " I. Modificar Código",
                                     " J. Modificar Tipo",
                                     " K. Modificar Fabricante",
                                     " L. Modificar Precio",
                                     " M. Modificar Cantidad",
                                     " N. Regresar al menú anterior"]


    def menuPrincipal(self):
        listaOpcionesValidas = ["A", "B", "C", "D", "E"]
        listaOpcionesValidas.sort()
        eleccion = 0
        self.listaOpcionesMenuPrincipal.sort()
        while True:
            for i in self.listaOpcionesMenuPrincipal:
                print(i)
            eleccion = input()
            if eleccion in listaOpcionesValidas:
                return eleccion
            else:
                print(f"\nIngrese una de las siguientes opciones: {listaOpcionesValidas}")


    def menuConsultar(self):
        listaOpcionesValidas = ["F", "G", "H"]
        listaOpcionesValidas.sort()
        eleccion = 0
        while True:
            print("\n~~~~~~~~~ MENU DE CONSULTAS DE ITEMS ~~~~~~~~~~\n")
            print(" F. Consultas por código")
            print(" G. Consultas por fabricante")
            eleccion = input(" H. Regresar al menú anterior\n\n")
            if eleccion in listaOpcionesValidas:
                return eleccion
            else:
                print(f"\nIngrese una de las siguientes opciones: {listaOpcionesValidas}")
                self.menuConsultar()


    def menuModificar(self):
        listaOpcionesValidas = {"I", "J", "K", "L", "M", "N"}
        eleccion = 0
        self.listaOpcionesMenuModificacion.sort()
        while True:
            for i in self.listaOpcionesMenuModificacion:
                print(i)
            eleccion = input()
            if eleccion in listaOpcionesValidas:
                return eleccion
            else:
                print(f"\nIngrese una de las siguientes opciones: {listaOpcionesValidas}")