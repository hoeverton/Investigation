from datetime import datetime
from typing import List

from ..modelo.abordagem import (Abordagem,
                                Local,
                                Abordado,
                                VeiculoAbordado,
                                BoletimOcorrencia)


class AbordagemControle:

    def __init__(self):
        pass

    @staticmethod
    def criar(cidade: str,
              bairro: str,
              rua: str,
              numeral: str,
              abordados: List[Abordado],
              veiculo_cor: str,
              veiculo_modelo: str,
              veiculo_placa: str,
              veiculo_proprietario: str,
              veiculo_tipo: str,
              bo_numero: str = None,
              bo_natureza: str = None) -> Abordagem:

        bo = None
        if bo_numero is not None:
            assert bo_natureza is not None, "bo_natureza deve ser especificado"
            bo = BoletimOcorrencia(numero=bo_numero, natureza=bo_natureza)

        local = Local(cidade=cidade,
                      bairro=bairro,
                      rua=rua,
                      numeral=numeral)

        veiculo = VeiculoAbordado(cor=veiculo_cor,
                                  modelo=veiculo_modelo,
                                  placa=veiculo_placa,
                                  proprietario=veiculo_proprietario,
                                  tipo=veiculo_tipo)

        return Abordagem(data=datetime.now(),
                         local=local,
                         abordados=abordados,
                         veiculo=veiculo,
                         boletim_ocorrencia=bo)

    @staticmethod
    def atualizar():
        pass