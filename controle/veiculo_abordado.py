from .veiculo_abordado import VeiculoAbordado
from .abordado import Abordado
class VeiculoAbordado_Controle:

    def __init__(self):
        pass

    @staticmethod
    def criar(tipo: str,
                 placa: str,
                 modelo: str,
                 ano:str,
                 cor: str,
                 proprietario: Union[str, Abordado]):

        return 