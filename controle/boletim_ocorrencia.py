from modelo.boletim_ocorrencia import BoletimOcorrencia
from banco_de_dados import Database


class BoletimOcorrenciaControle:

    def __init__(self):
        pass

    @staticmethod
    def criar(numero:str, natureza:str) ->BoletimOcorrencia: 

        BoletimOcorrencia(numero=numero,
                        natureza=natureza )

        Database.atualizar(BoletimOcorrencia)

        return BoletimOcorrencia

    @staticmethod
    def remover(numero:str):
        pass     