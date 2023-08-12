
from typing import List
from datetime import datetime

from .abordado import Abordado
from .veiculo_abordado import VeiculoAbordado
from .boletim_ocorrencia import BoletimOcorrencia
from .local import Local
from .viatura import Viatura
from . import Modelo


class Abordagem(Modelo):
    PARAMETROS_DE_IDENTIDADE = ["data", "viatura"]

    def __init__(self,
                 data: datetime,
                 viatura: Viatura,
                 local: Local,
                 abordados: List[Abordado],
                 veiculo: VeiculoAbordado = None,
                 boletim_ocorrencia: BoletimOcorrencia = None):

        self.viatura = viatura
        self.local = local
        self.data = data
        self.abordados = abordados
        self.veiculo = veiculo
        self.boletim_ocorrencia = boletim_ocorrencia
