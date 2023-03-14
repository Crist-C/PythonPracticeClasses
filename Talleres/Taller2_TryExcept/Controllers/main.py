from Talleres.Taller2_TryExcept.Models import dataBase
from Talleres.Taller2_TryExcept.Models.dataBase import DataBase
from Talleres.Taller2_TryExcept.Models.libro import Libro


class MainClass:

    def __init__(self, services_, menu_):
        self.services_object = services_
        self.menus = menu_

    def main(self):
        libro = Libro("ASDF1234", "ERASE UNA VEZ", "GABRIEL GARCIA", "PLANETA", 10)
        DataBase.BaseDeDatos.append(libro)

        while (True):
            eleccion = self.menus.menu_principal()

            if eleccion in {"B", "C", "D"} and dataBase.DataBase.get_total_registers_on_db() == 0:
                print("Error: la base de datos aún no contiene algún elemento\n")
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
