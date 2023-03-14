class DataBase:

    BaseDeDatos = []

    @classmethod
    def get_total_registers_on_db(cls):
        return len(cls.BaseDeDatos)