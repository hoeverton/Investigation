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

    @staticmethod
    def listar_relacoes(id_no_origem):
        for conector in BancoDeDados._CONECTORES_GRAFO:
            return conector.listar_relacoes(id_no_origem=id_no_origem)


class AbstratoRespoitorio:
    banco = BancoDeDados

    def remover(self, objeto):
        pass

    def carregar(self, objeto):
        filtro = f"id == '{objeto.id}'"
        data = self.banco.listar(tipo=type(objeto), filtro=filtro)
        print(data)

    def criar_ou_atualizar(self, objeto):
        self.banco.criar_ou_atualizar(data=objeto)
