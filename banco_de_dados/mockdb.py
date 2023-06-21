import re


class MockDB:
    MEMORIA = {}

    @staticmethod
    def atualizar(objeto):
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
    def lista(tipo, filtro = None) -> list:
        chave_memoria = tipo.__name__
        memoria = MockDB.MEMORIA.get(chave_memoria, [])

        if filtro is not None:
            filtro_decomposto = re.match(r"([a-z_]*) (==|>=|<=|<|>){1} ([a-z_]*)", filtro).groups()

            lambda_filtro = lambda x: eval(f"'{x.getattr(filtro_decomposto[0])}' {filtro_decomposto[1]} '{filtro_decomposto[2]}'")
            return list(filter(lambda_filtro, memoria))
        return memoria

    @staticmethod
    def _nome_classe(objeto):
        return type(objeto).__name__
