from modelo.boletim_ocorrencia import BoletimOcorrencia

class BoletimOcorrencia_Controle:

    def __init__(self):
        pass

    @staticmethod
    def criar(numero:str, natureza:str) ->bo:

        return bo(numero=numero,
                        natureza=natureza )