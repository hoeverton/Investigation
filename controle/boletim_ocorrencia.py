from modelo.boletim_ocorrencia import BoletimOcorrencia
from banco_de_dados import Database


class BoletimOcorrenciaControle:

    def __init__(self):
        pass

    @staticmethod
    def criar(numero:str, natureza:str) ->BoletimOcorrencia: 

        boletimOcorrencia = BoletimOcorrencia(numero=numero,
                                              natureza=natureza )

        Database.atualizar(boletimOcorrencia)

        return boletimOcorrencia

    @staticmethod
    def remover(numero:str):
        boletimOcorrencia = Database.listar(BoletimOcorrencia, f"numero == '{numero}'")[0]
        Database.remover(boletimOcorrencia)

    @staticmethod
    def atualizar(numero:str, natureza:str):
        
        boletimOcorrencia: BoletimOcorrencia = Database.listar(BoletimOcorrencia, f"numero == '{numero}'")[0]
        boletimOcorrencia.numero = numero
        boletimOcorrencia.natureza = natureza

        Database.atualizar(boletimOcorrencia)

        