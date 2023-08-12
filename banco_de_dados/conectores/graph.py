from simple_graph_sqlite import database as db
from modelo import Modelo
from datetime import datetime
import re
import copy
from sqlite3 import IntegrityError
from simple_graph_sqlite.visualizers import graphviz_visualize


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
    def listar(tipo, filtro=None) -> list:
        type_name = re.sub(r"(?!^[A-Za-z]*)([A-Z]+)", r"_\1", tipo.__name__).lower()

        padrao_regex = r"([a-z_]*) (==|>=|<=|<|>){1} [\'|\"]([0-9:A-Z\-_\.,a-z_ ]*)[\'|\"]"
        parametro, operador, valor = re.match(padrao_regex,
                                              filtro).groups()
        operador_mapper = {
            "==": "=",
            ">=": ">",
            "<=": "<"
        }
        operador = operador_mapper.get(operador, operador)

        return db.atomic(
            GraphDB.DB_NAME,
            db.find_nodes([
                db._generate_clause(key=parametro, predicate=operador),
                db._generate_clause(key="_type", predicate="=", joiner="AND")],
                (valor, type_name)))

    @staticmethod
    def criar(objeto):
        type_name = re.sub(r"(?!^[A-Za-z]*)([A-Z]+)", r"_\1", type(objeto).__name__).lower()
        data = {"_type": type_name, **copy.deepcopy(objeto.__dict__)}

        remove_keys = []
        for key in data:
            if isinstance(data[key], datetime):
                data[key] = data[key].strftime("%Y-%m-%d %H:%M:%S")
            elif isinstance(data[key], Modelo):
                remove_keys.append(key)
            elif isinstance(data[key], list):
                model_to_id = []
                for item in data[key]:
                    if isinstance(item, Modelo):
                        model_to_id.append(item.__dict__)
                if len(model_to_id) > 0:
                    remove_keys.append(key)

        for key in remove_keys:
            del data[key]
        try:
            db.atomic(GraphDB.DB_NAME,
                      db.upsert_node(data["id"], data))
        except IntegrityError as e:
            if "UNIQUE constraint failed" in str(e):
                print(e, str(data))

    @staticmethod
    def criar_relacao(source_id, target_id, **params):
        try:
            db.atomic(GraphDB.DB_NAME,
                      db.connect_nodes(source_id=str(source_id), target_id=str(target_id), properties=params))
        except IntegrityError as e:
            if "UNIQUE constraint failed" in str(e):
                print(e, source_id, target_id)
