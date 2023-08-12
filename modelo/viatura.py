
from . import Modelo


class Viatura(Modelo):
    PARAMETROS_DE_IDENTIDADE = ['codigo']

    def __init__(self, codigo):
        self.codigo = codigo