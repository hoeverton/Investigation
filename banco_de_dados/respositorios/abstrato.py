from banco_de_dados.conectores.graph import GraphDB
from banco_de_dados.conectores.mockdb import MockDB


class BancoDeDados:
    _CONECTORES = [GraphDB, MockDB]
    _CONECTORES_GRAFO = [MockDB]

    @staticmethod
    def criar(data):
        for conector in BancoDeDados._CONECTORES:
            conector.criar(data)

    @staticmethod
    def criar_relacao(id_origem, id_destino, **params):
        for conector in BancoDeDados._CONECTORES_GRAFO:
            conector.criar_relacao(id_origem, id_destino, params)


class AbstratoRespoitorio:

    def __init__(self, objeto):
        self.objeto = objeto
        self.banco = BancoDeDados

    def atualizar(self):
        pass

    def remover(self):
        pass

    def criar(self):
        self.banco.criar(data=self.objeto)
