from datetime import datetime
from typing import List

from modelo.abordagem import (Abordagem,
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
              veiculo_cor: str = None,
              veiculo_modelo: str = None,
              veiculo_placa: str = None,
              veiculo_ano: str = None,
              veiculo_proprietario: str = None,
              veiculo_tipo: str = None,
              bo_numero: str = None,
              bo_natureza: str = None) -> Abordagem:

        bo = None
        if bo_numero is not None:
            assert bo_natureza is not None, "bo_natureza deve ser especificado"
            bo = BoletimOcorrencia(numero=bo_numero, natureza=bo_natureza)

        veiculo = None
        if veiculo_placa is not None:
            assert veiculo_cor is not None, "veiculo_cor deve ser especificado"
            assert veiculo_tipo is not None, "veiculo_tipo deve ser especificado"
            assert veiculo_ano is not None, "veiculo_ano deve ser especificado"
            assert veiculo_proprietario is not None, "veiculo_proprietario deve ser especificado"
            assert veiculo_modelo is not None, "veiculo_modelo deve ser especificado"

            veiculo = VeiculoAbordado(cor=veiculo_cor,
                                      modelo=veiculo_modelo,
                                      placa=veiculo_placa,
                                      ano =ano,
                                      proprietario=veiculo_proprietario,
                                      tipo=veiculo_tipo)
        local = Local(cidade=cidade,
                      bairro=bairro,
                      rua=rua,
                      
                      numeral=numeral)

        return Abordagem(data=datetime.now(),
                         local=local,
                         abordados=abordados,
                         veiculo=veiculo,
                         boletim_ocorrencia=bo)

    @staticmethod
    def atualizar():
        pass