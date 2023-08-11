from simple_graph_sqlite import database as db
from uuid import uuid4

class GraphDB:
    DB_NAME = "investigation.graph"
    DB_CONNECTION = db.initialize(DB_NAME)

    @staticmethod
    def atualizar(objeto):
        GraphDB.criar(objeto)

    @staticmethod
    def remover(objeto):
        pass

    @staticmethod
    def criar(objeto):
        db.atomic(GraphDB.DB_NAME,
                  db.add_node(objeto.__dict__(), str(uuid4())))

    @staticmethod
    def listar(tipo, filtro=None) -> list:
        pass