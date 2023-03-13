from Talleres.Taller1_Clases import dataBase
from Talleres.Taller1_Clases.menu import Menu


class MainClass:


    def __init__(self, services_, menu_):
        self.services_object = services_
        self.menus = menu_


    def main(self):
        while (True):
            eleccion = self.menus.menuPrincipal()

            if eleccion in {"B", "C", "D"} and dataBase.DataBase.get_length_of_list() == 0:
                print("Error: la lista aún no contiene algún elemento\n")
                self.main()
            elif eleccion == "A":
                self.services_object.opcion_crear()
            elif eleccion == "B":
                self.services_object.opcion_eliminar()
            elif eleccion == "C":
                self.services_object.opcion_consultar()
            elif eleccion == "D":
                self.services_object.opcion_modificar()
            elif eleccion == "E":
                exit()
