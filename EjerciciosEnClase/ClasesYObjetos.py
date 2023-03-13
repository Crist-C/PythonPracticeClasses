class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return (self.base * self.altura) / 2.0;


class Item:
    def __init__(self, lista):
        self.descripcion = lista[0]
        self.fabricante  = lista[1]
        self.precio = lista[2]


data_base = []
lista = []
i = 1
while i > 0:
    descripcion = input("Ingrese la descripción\n")
    fabricante = input("Ingrese el fabricante\n")
    precio = int(input("Ingrese el precio\n"))
    lista.append(descripcion)
    lista.append(fabricante)
    lista.append(precio)

    item = Item(lista)
    data_base.append(lista)
    i-=1
print(data_base)

rectangulo1 = Rectangulo(2.5, 3.0)
rectangulo2 = Rectangulo(4, 5)

print(f'Rectangulo 1 -> Base {rectangulo1.altura}, altura:{rectangulo1.base}')
print(f'Rectangulo 2 -> Base {rectangulo2.altura}, altura:{rectangulo2.base}')
print(f'Área del rectangulo 1: {rectangulo1.calcularArea()}')
print(f'Área del rectangulo 2: {rectangulo2.calcularArea()}')
