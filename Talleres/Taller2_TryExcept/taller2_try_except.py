from Talleres.Taller2_TryExcept.Controllers.main import MainClass
from Talleres.Taller2_TryExcept.Views.menu import Menu
from Talleres.Taller2_TryExcept.Controllers.services import Services

menu_object = Menu()
service_object = Services(menu_object)
main_object = MainClass(service_object, menu_object)
service_object.set_main_object(main_object)

main_object.main()
