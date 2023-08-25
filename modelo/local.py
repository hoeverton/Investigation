from . import Modelo


class Local(Modelo):
    PARAMETROS_DE_IDENTIDADE = ["rua", "bairro", "cidade", "numeral"]

    def __init__(self,
                 cidade: str,
                 bairro: str,
                 rua: str,
                 numeral: str,
                 id=None):

        super().__init__(id=id)
        self.cidade = cidade
        self.bairro = bairro
        self.rua = rua
        self.numeral = numeral