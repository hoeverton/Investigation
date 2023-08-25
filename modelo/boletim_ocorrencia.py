from . import Modelo


class BoletimOcorrencia(Modelo):
    PARAMETROS_DE_IDENTIDADE = ["numero"]

    def __init__(self,
                 numero: str,
                 natureza: str,
                 id=None):

        super().__init__(id=id)
        self.numero = numero
        self.natureza = natureza
