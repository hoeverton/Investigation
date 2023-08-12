import re


class MockDB:
    MEMORIA = {}

    @staticmethod
    def criar_ou_atualizar(objeto):
        MockDB.remover(objeto)
        MockDB.criar(objeto)

    @staticmethod
    def remover(objeto):
        chave_memoria = MockDB._nome_classe(objeto)

        if chave_memoria in MockDB.MEMORIA:
            for idx, item in enumerate(MockDB.MEMORIA[chave_memoria]):
                if objeto == item:
                    del MockDB.MEMORIA[chave_memoria][idx]

    @staticmethod
    def criar(objeto):
        chave_memoria = MockDB._nome_classe(objeto)

        if chave_memoria in MockDB.MEMORIA:
            MockDB.MEMORIA[chave_memoria].append(objeto)
        else:
            MockDB.MEMORIA[chave_memoria] = [objeto]

    @staticmethod
    def listar(tipo, filtro=None) -> list:
        chave_memoria = tipo.__name__
        memoria = MockDB.MEMORIA.get(chave_memoria, [])

        if filtro is not None:
            lambda_filtro = MockDB._constroi_filtro(filtro)
            return list(filter(lambda_filtro, memoria))

        return memoria

    @staticmethod
    def _constroi_filtro(filtro: str):
        padrao_regex = r"([a-z_]*) (==|>=|<=|<|>){1} [\'|\"]([0-9:A-Z\-_\.,a-z_ ]*)[\'|\"]"
        parametro, operador, valor = re.match(padrao_regex,
                                              filtro).groups()

        return lambda x: eval(f"'{getattr(x, parametro)}' {operador} '{valor}'")

    @staticmethod
    def _nome_classe(objeto):
        return type(objeto).__name__
