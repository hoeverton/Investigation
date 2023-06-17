
from typing import List
from datetime import datetime

from .abordado import Abordado
from .veiculo_abordado import VeiculoAbordado
from .boletim_ocorrencia import BoletimOcorrencia
from .local import Local


class Abordagem:

    def __init__(self,
                 data: datetime,
                 local: Local,
                 abordados: List[Abordado],
                 veiculo: VeiculoAbordado = None,
                 boletim_ocorrencia: BoletimOcorrencia = None):

        self.local = local
        self.data = data
        self.abordados = abordados
        self.veiculo = veiculo
        self.boletim_ocorrencia = boletim_ocorrencia
