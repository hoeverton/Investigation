from typing import Union

from .abordado import Abordado
from . import Modelo


class VeiculoAbordado(Modelo):
    PARAMETROS_DE_IDENTIDADE = ["placa"]

    def __init__(self,
                 tipo: str,
                 placa: str,
                 modelo: str,
                 ano:str,
                 cor: str,
                 proprietario: Union[str, Abordado]):

        self.tipo = tipo
        self.placa = placa
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.proprietario = proprietario
        self.obs = []

    def add_observation(self, message):
        self.obs.append(message)


