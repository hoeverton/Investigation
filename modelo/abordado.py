
from . import Modelo


class Abordado(Modelo):
    PARAMETROS_DE_IDENTIDADE = ["rg"]

    def __init__(self,
                 nome: str,
                 apelido: str,
                 rg: str,
                 foto: str = None):

        self.nome = nome
        self.apelido = apelido
        self.rg = rg
        self.foto = foto

