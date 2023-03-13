elemento = \
    {
        "Codigo": 0,
        "Tipo": "",
        "Fabricante": "",
        "Precio": 0,
        "Items": 0
    }
lista = []


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


def mostrarElemento(elemento):
    print(f'Codigo: {elemento["Codigo"]}\nTipo: {elemento["Tipo"]}')
    print(f'Fabricante: {elemento["Fabricante"]}\nPrecio: {elemento["Precio"]}\nItems: {elemento["Items"]}\n')


def consultarPor(campo_de_busqueda, valor_a_buscar, lista_de_elementos):
    listaDeCoincidencias = []
    for elemento_en_lista in lista_de_elementos:
        if elemento_en_lista[campo_de_busqueda] == valor_a_buscar:
            listaDeCoincidencias.append(elemento_en_lista);
    if len(listaDeCoincidencias) != 0:
        return listaDeCoincidencias
    return False;


def menuPrincipal():
    listaOpcionesValidas = {"A", "B", "C", "D", "E"}
    eleccion = 0
    listaOpcionesMenuPrincipal.sort()
    while True:
        for i in listaOpcionesMenuPrincipal:
            print(i)
        eleccion = input()
        if eleccion in listaOpcionesValidas:
            return eleccion
        else:
            print(f"\nIngrese una de las siguientes opciones: {listaOpcionesValidas}")


def menuConsultar():
    listaOpcionesValidas = {"F", "G", "H"}
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
            menuConsultar()


def opcion_crear():
    ### Solicita el código y valida que sea numérico
    codigo = input("Ingrese el código del elemento: \n")
    if codigo.isdigit():
        ## Si el código NO existe entonces lo agrega
        if not consultarPor("Codigo", int(codigo), lista):
            elemento["Codigo"] = int(codigo)
        else:
            print("El código ya existe.\nintentelo nuevamente insertando un código que no exista.\n")
            opcion_crear()

        ## De lo contrario el usuario debe iniciar de nuevo la creación del elemento
    else:
        print("Ha ingresado un dato erroneo.\nintentelo nuevamente insertando un dato numérico\n")
        opcion_crear()

    ### Solicita el tipo de elemento y valida que no contenga números
    tipo = input("Ingrese el tipo de elemento: \n")
    if tipo.isalpha():
        elemento["Tipo"] = tipo
    else:
        print("Ha ingresado un dato erroneo. Ingrese un tipo de dato numérico\n")
        opcion_crear()

    ### Solicita el fabricante del elemento y valida que sea alfanumérico
    fabricante = input("Ingrese el fabricante de elemento: \n")
    if fabricante.isalnum():
        elemento["Fabricante"] = fabricante
    else:
        print("Ha ingresado un dato erroneo. Ingrese un tipo de dato numérico\n")
        opcion_crear()

    ### Solicita el precio del elemento y valida que sea numérico
    precio = input("Ingrese el precio por unidad del elemento: \n")
    if precio.isdigit():
        elemento["Precio"] = int(precio)
    else:
        print("Ha ingresado un dato erroneo. Ingrese un tipo de dato numérico\n")
        opcion_crear()

    ### Solicita la cantidad de items del elemento y valida que sea numérico
    items = input("Ingrese la cantidad de items en stock: \n")
    if items.isdigit():
        elemento["Items"] = int(items)
    else:
        print("Ha ingresado un dato erroneo. Ingrese un tipo de dato numérico\n")
        opcion_crear()

    ### Agrega el elemento a la lista
    lista.append(elemento.copy())
    #print(lista)
    main()


def opcion_eliminar():
    codigo_del_elemento_a_eliminar = input("Ingrese el código del elemento que desea ELIMINAR\nó cualquier letra para volver al menú anterior: \n")
    if codigo_del_elemento_a_eliminar.isdigit():
        elemento_a_eliminar = consultarPor("Codigo", int(codigo_del_elemento_a_eliminar), lista)
        if not elemento_a_eliminar:
            print("No existe un elemento con ese código.\nintentelo nuevamente.\n")
            opcion_eliminar()
    else:
        print("Ha escogido volver al menú anterior.\n")
        main()

    print("El elemento que se eliminará es: ")
    mostrarElemento(elemento_a_eliminar[0])
    confirmacion = input("Confirma eliminar el elemento? (Y/N):")
    if confirmacion.upper() == "Y":
        lista.remove(elemento_a_eliminar[0])
        print("elemento eleminado")
    main()


def opcion_consultar():
    eleccion = menuConsultar()

    if eleccion == "H":
        main()
    if eleccion == "F":

        codigo_para_consultar = input("Ingrese el código del elemento: \n")

        if codigo_para_consultar.isdigit():
            elementos_consultados = consultarPor("Codigo", int(codigo_para_consultar), lista)
            if elementos_consultados == False:
                print("El elemento no existe en la lista.")
                opcion_consultar()
            else:
                for elemento in elementos_consultados:
                    mostrarElemento(elemento)
                opcion_consultar()

            ## De lo contrario el usuario debe iniciar de nuevo la creación del elemento
        else:
            print("Ha ingresado un dato erroneo.\nintentelo nuevamente insertando un dato numérico\n")
            opcion_consultar()

    if eleccion == "G":

        fabricante_para_consultar = input("Ingrese el nombre del Fabricante del elemento: \n")

        if fabricante_para_consultar.isalnum():
            elementos_consultados = consultarPor("Fabricante", fabricante_para_consultar, lista)
            if elementos_consultados == False:
                print("No existen elementos en la lista de ese fabricante.")
                opcion_consultar()
            else:
                for elemento in elementos_consultados:
                    mostrarElemento(elemento)
                opcion_consultar()

            ## De lo contrario el usuario debe iniciar de nuevo la creación del elemento
        else:
            print("Ha ingresado un dato erroneo.\nintentelo nuevamente insertando un dato numérico\n")
            opcion_consultar()


def menuModificar():
    listaOpcionesValidas = {"I", "J", "K", "L", "M", "N"}
    eleccion = 0
    listaOpcionesMenuModificacion.sort()
    while True:
        for i in listaOpcionesMenuModificacion:
            print(i)
        eleccion = input()
        if eleccion in listaOpcionesValidas:
            return eleccion
        else:
            print(f"\nIngrese una de las siguientes opciones: {listaOpcionesValidas}")


def opcion_modificar():

    elemento_actualizado = False

    codigo_del_elemento_a_modificar = input("\nPara hacer una modificación, primero ingrese el código del elemento que desea modificar: \n")
    if codigo_del_elemento_a_modificar.isdigit():
        elemento_a_modificar = consultarPor("Codigo", int(codigo_del_elemento_a_modificar), lista)
        if not elemento_a_modificar:
            print("No existe un elemento con ese código.\n")
            opcion_modificar()
    else:
        print("Ha ingresado un dato erroneo.\nintentelo nuevamente insertando un dato numérico\n")
        opcion_modificar()

    codigo_del_elemento_a_modificar = int(codigo_del_elemento_a_modificar)

    print("\nEl elemento a modificar es :")
    mostrarElemento(elemento_a_modificar[0])
    #print(
    #    f"Codigo:{elemento_a_modificar[0]['Codigo']}, Tipo: {elemento_a_modificar[0]['Tipo']}, Fabricante: {elemento_a_modificar[0]['Fabricante']}, Precio: {elemento_a_modificar[0]['Precio']}, Items: {elemento_a_modificar[0]['Items']}\n")

    eleccion = menuModificar()

    if eleccion == "N":
        main()

    if eleccion == "I":
        nuevo_valor = input("Ingrese el nuevo código del elemento: \n")
        if nuevo_valor.isdigit():
            if consultarPor("Codigo", int(nuevo_valor), lista):
                print("Ya existe un elemento con este código. Intentelo nuevamente")
                opcion_modificar()
            else:
                modificarCampo(codigo_del_elemento_a_modificar, "Codigo", int(nuevo_valor), lista)
                elemento_actualizado = consultarPor("Codigo",int(nuevo_valor),lista)
            print("Campo modificado")
        else:
            print("Ha ingresado un dato erroneo.\nintentelo nuevamente insertando un dato numérico\n")
            opcion_modificar()

    if eleccion == "J":
        nuevo_valor = input("Ingrese el nuevo tipo del elemento: \n")
        if nuevo_valor.isalpha():
            modificarCampo(codigo_del_elemento_a_modificar, "Tipo", nuevo_valor, lista)
            print("Campo modificado")
        else:
            print("Ha ingresado un dato erroneo.\nintentelo nuevamente insertando un valor sin números\n")
            opcion_modificar()

    if eleccion == "K":
        nuevo_valor = input("Ingrese el nuevo fabricante del elemento: \n")
        if nuevo_valor.isalnum():
            modificarCampo(codigo_del_elemento_a_modificar, "Fabricante", nuevo_valor, lista)
            print("Campo modificado")
        else:
            print("Ha ingresado un dato erroneo.\nintentelo nuevamente.\n")
            opcion_modificar()

    if eleccion == "L":
        nuevo_valor = input("Ingrese el nuevo Precio del elemento: \n")
        if nuevo_valor.isdigit():
            modificarCampo(codigo_del_elemento_a_modificar, "Precio", int(nuevo_valor), lista)
            print("Campo modificado")
        else:
            print("Ha ingresado un dato erroneo.\nintentelo nuevamente insertando un dato numérico\n")
            opcion_modificar()

    if eleccion == "M":
        nuevo_valor = input("Ingrese la nueva cantidad de items del elemento en stock: \n")
        if nuevo_valor.isdigit():
            modificarCampo(codigo_del_elemento_a_modificar, "Items", int(nuevo_valor), lista)
            print("Campo modificado")
        else:
            print("Ha ingresado un dato erroneo.\nintentelo nuevamente insertando un dato numérico\n")
            opcion_modificar()

    if not elemento_actualizado:
        elemento_actualizado = consultarPor("Codigo",codigo_del_elemento_a_modificar, lista)
    print("\nEl elemento modificado es: ")
    mostrarElemento(elemento_actualizado[0])
    main()


def modificarCampo(codigo, campo_a_modificar, nuevo_valor, lista_elementos):
    for elemento_a_modificar in lista_elementos:
        if elemento_a_modificar["Codigo"] == codigo:
            elemento_a_modificar[campo_a_modificar] = nuevo_valor
            #print(f"{campo_a_modificar}: {elemento_a_modificar[campo_a_modificar]}")
            break


def main():
    eleccion = menuPrincipal()

    if eleccion in {"B", "C", "D"} and len(lista) == 0:
        print("Error: la lista aún no contiene algún elemento\n")
        main()
    elif eleccion == "A":
        opcion_crear()
    elif eleccion == "B":
        opcion_eliminar()
    elif eleccion == "C":
        opcion_consultar()
    elif eleccion == "D":
        opcion_modificar()
    elif eleccion == "E":
        exit()


main()
