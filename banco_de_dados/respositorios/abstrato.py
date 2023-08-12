from banco_de_dados.conectores.graph import GraphDB
from banco_de_dados.conectores.mockdb import MockDB
from uuid import uuid4
import re

from modelo import Modelo



class BancoDeDados:
    _CONECTORES = [GraphDB, MockDB]
    _CONECTORES_GRAFO = [GraphDB]


    @staticmethod
    def listar(tipo, filtro):
        return GraphDB.listar(tipo, filtro)

    @staticmethod
    def criar(data: Modelo):
        if isinstance(data, Modelo):

            for conector in BancoDeDados._CONECTORES:
                conector.criar(data)
        return data


    @staticmethod
    def criar_relacao(id_origem, id_destino, **params):
        for conector in BancoDeDados._CONECTORES_GRAFO:
            conector.criar_relacao(id_origem, id_destino, **params)


class AbstratoRespoitorio:

    def __init__(self, objeto):
        self.objeto = objeto
        self.banco = BancoDeDados

    def atualizar(self):
        pass

    def remover(self):
        pass

    def carregar(self):
        filtro = f"id == '{self.objeto.id}'"
        data = self.banco.listar(tipo=type(self.objeto), filtro=filtro)
        print(data)

    def criar(self):
        self.banco.criar(data=self.objeto)
