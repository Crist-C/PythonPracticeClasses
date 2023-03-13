def ejercicio2():
    count = 0
    valorMinimo = int(input("Ingrese el número inicial: "))
    valorMaximo = int(input("Ingrese el número final: "))
    for i in range(valorMinimo, valorMaximo + 1, 1):
        print(i, end=" ")
        for j in range(1, i + 1):
            if (i % j) == 0:
                count += 1
        if count <= 2:
            print(f'{i} es primo')


def ejercicio1():
    print("\n Primer ejercicio\n")
    for i in range(6):
        print(i, end=" ")

    print("\n Segundo ejercicio\n")
    for i in range(-5, 10, 2):
        print(i, end=" ")
    else:
        print(f'La variable i ya llego al valor {i}')

    print("\n Tercer ejercicio\n")
    for i in range(10, -10, -1):
        print(i, end=" ")


def ejercicioListas():
    lista_alimentos = ["Carne", 2.4, "Arroz", 35, "Atun", "Carne"]
    print(f'Lista  de alimentos: {lista_alimentos}')
    print(f'La longitud de la lista es: {len(lista_alimentos)}')

    string = "Texto de prueba"
    print(f'la cadena {string} contiene {len(string)} caracteres')

    lista_alimentos.append(99)
    print(f'La longitud de la lista es: {len(lista_alimentos)}')
    for elemento in lista_alimentos:
        print(elemento, end=" ")

    for i in range(0, len(lista_alimentos) + 1):
        print(f'El elemento {i} de la lista es {lista_alimentos[i - 1]}')

    lista_vacia = []


def ejercicioListasPag3():
    NOMBRES = []

    print(f'Elementos de la lista Nombres: {NOMBRES}')

    for x in range(5):
        NOMBRES.append(input("Ingrese un nombre: "))

    print(NOMBRES)


def ejercicioMarcasDeCarros():
    MARCA_CARROS = ["Renault", "VolksVagen", "Hynduai", "Mazda"]
    print(f"La lista original es: {MARCA_CARROS}")
    print(f"El tipo de dato es {type(MARCA_CARROS)}")

    MARCA_CARROS[1] = "Seat"
    print(f"la lista modificada es: {MARCA_CARROS}")

    MARCA_CARROS[1:3] = ["Skoda", "Kia"]
    print(f"la lista modificada es: {MARCA_CARROS}")

    MARCA_CARROS[1:3] = ["MERCEDES"]
    print(f"la lista modificada es: {MARCA_CARROS}")

    MARCA_CARROS[1:3] = ["BMW", "Volvo", "Honda", "Audi"]
    print(f"La lista modificada es: {MARCA_CARROS}")

    MARCA_CARROS.insert(3, "Buggati")
    print(f"la lista modificada es: {MARCA_CARROS}")

    if "SUBARU" in MARCA_CARROS:
        MARCA_CARROS.remove("SUBARU")
        print(f"Se removio el nombre SUBARU de la lista: {MARCA_CARROS}")
    else:
        print(f"La marca SUBARU no está dentro de la lista Marca carros: {MARCA_CARROS}")

    if "Volvo" in MARCA_CARROS:
        MARCA_CARROS.remove("Volvo")
        print(f"Se removio el nombre VOLVO de la lista: {MARCA_CARROS}")
    else:
        print(f"La marca VOLVO no está dentro de la lista Marca carros: {MARCA_CARROS}")


def ejercicioAsignacionPorObjeto():
    prueba = [5, -2, -4, 10, 7]
    test = prueba
    print(test, prueba)

    prueba.sort()
    print(test, prueba)

    prueba = [5, -2, -4, 10, 7]
    test = prueba.copy()
    prueba.sort()
    print(test, prueba)

    prueba = ['b', 'a', 'c', 'z']
    prueba.sort()
    print(prueba)


def ejemploDiccionarios():
    ELEMENTO = {
        "Tipo": "Leche",
        "Fabricante": "Colanta",
        "Precio": 3500,
        "Items": 15
    }

    ELEMENTO2 = {
        "Tipo": "Huevos",
        "Fabricante": "Kikes",
        "Precio": 14300,
        "Items": 10
    }

    print(f"{ELEMENTO} \n{ELEMENTO2}")

    print(ELEMENTO["Tipo"], ELEMENTO["Items"],  ELEMENTO["Precio"],  ELEMENTO["Fabricante"])
    print(ELEMENTO2["Tipo"], ELEMENTO2["Items"],  ELEMENTO2["Precio"],  ELEMENTO2["Fabricante"])

    zzz = ELEMENTO["Tipo"]
    www = ELEMENTO.get("Tipo")
    print(f"ZZZ: {zzz}\nWWW: {www}")

    ELEMENTO["Items"] = 4
    ELEMENTO["Precio"] = 4000
    print(ELEMENTO["Tipo"], ELEMENTO["Items"],  ELEMENTO["Precio"],  ELEMENTO["Fabricante"])

    claves = ELEMENTO.keys()
    valores = ELEMENTO.values()
    print(claves)
    print(valores)
    aaa = ELEMENTO.items()
    print(aaa)

    ELEMENTO.pop("Fabricante")
    print(f"Se eliminó Fabricante del elemento {ELEMENTO}")

    ELEMENTO.clear()
    print(ELEMENTO)


def ejemploListaDeDiccionario():
    listado = []

    elemento = {
        "Tipo": "Leche",
        "Fabricante": "Colanta",
        "Precio": 3500,
        "Items": 15
    }
    listado.append(elemento)

    elemento = {
        "Tipo": "Salchicha",
        "Fabricante": "Zenu",
        "Precio": 6700,
        "Items": 22
    }
    listado.append(elemento)

    elemento = {
        "Tipo": "Huevos",
        "Fabricante": "Kikes",
        "Precio": 12300,
        "Items": 5
    }
    listado.append(elemento)

    elemento = {
        "Tipo": "Pan",
        "Fabricante": "Bimbo",
        "Precio": 7500,
        "Items": 11
    }
    listado.append(elemento)
    print(listado)
    print(listado[0])
    print(listado[1])
    print(listado[2])
    print(listado[3])
    
    print(listado[0]['Tipo'], listado[0]['Fabricante'], listado[0]['Precio'], listado[0]['Items'])
    print(listado[1]['Tipo'], listado[1]['Fabricante'], listado[1]['Precio'], listado[1]['Items'])
    print(listado[2]['Tipo'], listado[2]['Fabricante'], listado[2]['Precio'], listado[2]['Items'])

    for x in listado:
        print(x)

    print(f"Longitud del listado {len(listado)}")

    for i in range(len(listado)):
        print(listado[i]['Tipo'])

def funcion_1( Nombre, Apellido):
    Nombre.upper();
    Apellido.upper();
    print(Nombre,Apellido)

def funcion_2 (lista: list):
    for x in lista:
        print(x, type(x), end=" ")
    print("\n********************")


lista = ["Ajiaco", "Salmon", "Crema de auyama", "Ensalada de frutas"]
funcion_2(lista)

lista2 = [1,2,3,5]
funcion_2(lista2)

lista3 = [1.2, 64.67, -567.56534]
funcion_2(lista3)

lista4 = []
elemento1 = {
    "Tipo": "Leche",
    "Fabricante":"Colanta"
}
lista4.append(elemento1)

elemento1 = {
    "Tipo": "Huevos",
    "Fabricante":"Kikes"
}
lista4.append(elemento1)
funcion_2(lista4)


