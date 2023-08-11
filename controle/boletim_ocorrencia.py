from modelo.boletim_ocorrencia import BoletimOcorrencia


class BoletimOcorrenciaControle:

    def __init__(self):
        pass

    @staticmethod
    def criar(numero: str, natureza: str) -> BoletimOcorrencia:
        return BoletimOcorrencia(numero=numero,
                                 natureza=natureza)
