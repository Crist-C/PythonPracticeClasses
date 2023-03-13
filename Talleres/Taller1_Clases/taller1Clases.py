from Talleres.Taller1_Clases.main import MainClass
from Talleres.Taller1_Clases.menu import Menu
from Talleres.Taller1_Clases.services import Services

menu_object = Menu()
service_object = Services(menu_object)
main_object = MainClass(service_object, menu_object)
service_object.set_main_object(main_object)

main_object.main()
