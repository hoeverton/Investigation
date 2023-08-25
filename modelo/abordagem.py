
from typing import List
from datetime import datetime

from .abordado import Abordado
from .veiculo_abordado import VeiculoAbordado
from .boletim_ocorrencia import BoletimOcorrencia
from .local import Local
from . import Modelo


class Abordagem(Modelo):
    PARAMETROS_DE_IDENTIDADE = ["data", "local"]

    def __init__(self,
                 data: datetime,
                 local: Local,
                 abordados: List[Abordado],
                 veiculo: VeiculoAbordado = None,
                 boletim_ocorrencia: BoletimOcorrencia = None,
                 id=None):

        super().__init__(id=id)
        self.local = local
        self.data = data
        self.abordados = abordados
        self.veiculo = veiculo
        self.boletim_ocorrencia = boletim_ocorrencia
