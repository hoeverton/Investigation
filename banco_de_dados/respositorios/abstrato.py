from banco_de_dados.conectores.graph import GraphDB
from banco_de_dados.conectores.mockdb import MockDB

from modelo import Modelo


class BancoDeDados:
    _CONECTORES = [GraphDB, MockDB]
    _CONECTORES_GRAFO = [GraphDB]


    @staticmethod
    def listar(tipo, filtro):
        return GraphDB.listar(tipo, filtro)

    @staticmethod
    def criar_ou_atualizar(data: Modelo):
        if isinstance(data, Modelo):

            for conector in BancoDeDados._CONECTORES:
                conector.criar_ou_atualizar(data)
        return data

    @staticmethod
    def criar_ou_atualizar_relacao(id_origem, id_destino, is_unique=False, **params):
        for conector in BancoDeDados._CONECTORES_GRAFO:
            conector.criar_ou_atualizar_relacao(id_origem, id_destino, unique_relation_type_for_source=is_unique, **params)


class AbstratoRespoitorio:

    def __init__(self, objeto):
        self.objeto = objeto
        self.banco = BancoDeDados

    def remover(self):
        pass

    def carregar(self):
        filtro = f"id == '{self.objeto.id}'"
        data = self.banco.listar(tipo=type(self.objeto), filtro=filtro)
        print(data)

    def criar_ou_atualizar(self):
        self.banco.criar_ou_atualizar(data=self.objeto)
