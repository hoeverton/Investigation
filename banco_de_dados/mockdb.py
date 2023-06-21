

class MockDB:
    MEMORIA = {}

    @staticmethod
    def upinsert(objeto):
        MockDB.remove(objeto)
        MockDB.cria(objeto)

    @staticmethod
    def remove(objeto):
        chave_memoria = MockDB._nome_classe(objeto)

        if chave_memoria in MockDB.MEMORIA:
            for idx, item in enumerate(MockDB.MEMORIA[chave_memoria]):
                if objeto == item:
                    del MockDB.MEMORIA[chave_memoria][idx]

    @staticmethod
    def cria(objeto):
        chave_memoria = MockDB._nome_classe(objeto)

        if chave_memoria in MockDB.MEMORIA:
            MockDB.MEMORIA[chave_memoria].append(objeto)
        else:
            MockDB.MEMORIA[chave_memoria] = [objeto]

    @staticmethod
    def lista(tipo):
        chave_memoria = tipo.__name__
        return MockDB.MEMORIA.get(chave_memoria, [])

    @staticmethod
    def _nome_classe(objeto):
        return type(objeto).__name__
