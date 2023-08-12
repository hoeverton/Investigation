from . import Modelo


class BoletimOcorrencia(Modelo):
    PARAMETROS_DE_IDENTIDADE = ["numero"]

    def __init__(self,
                 numero: str,
                 natureza: str):

        self.numero = numero
        self.natureza = natureza
