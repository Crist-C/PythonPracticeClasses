class DataBase:
    elemento = \
        {
            "Codigo": 0,
            "Tipo": "",
            "Fabricante": "",
            "Precio": 0,
            "Items": 0
        }

    lista = []

    @classmethod
    def get_length_of_list(cls):
        return len(cls.lista)