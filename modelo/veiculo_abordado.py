from typing import Union

from .abordado import Abordado


class VeiculoAbordado:

    def __init__(self,
                 tipo: str,
                 placa: str,
                 modelo: str,
                 cor: str,
                 proprietario: Union[str, Abordado]):

        self.tipo = tipo
        self.placa = placa
        self.modelo = modelo
        self.cor = cor
        self.proprietario = proprietario
        self.obs = []

    def add_observation(self, message):
        self.obs.append(message)


