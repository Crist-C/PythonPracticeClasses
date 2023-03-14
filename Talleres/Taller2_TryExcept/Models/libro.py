class Libro:

    def __init__(self, codigo, nombre_libro, autor, editorial, numero_ejemplares):
        self.codigo = codigo
        self.nombre_libro = nombre_libro
        self.autor = autor
        self.editorial = editorial
        self.numero_ejemplares = numero_ejemplares

    def get_libro_like_dictionary(self):
        diccionary = {
            "Codigo": self.codigo,
            "Nombre_libro": self.nombre_libro,
            "Autor": self.autor,
            "Editorial": self.editorial,
            "Numero_ejemplares": self.numero_ejemplares
        }
        return diccionary

    def mostrar(self):
        print(f"Codigo: {self.codigo} \nNombre del libro: {self.nombre_libro} \nAutor: {self.autor} \nEditorial: {self.editorial} \nNumero de ejemplares: {self.numero_ejemplares}\n")
