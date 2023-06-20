from .veiculo_abordado import VeiculoAbordado


class VeiculoAbordado_Controle:

    def __init__(self):
        pass

    @staticmethod
    def criar(tipo: str,
                 placa: str,
                 modelo: str,
                 ano:str,
                 cor: str,
                 proprietario: Union[str, Abordado]) ->VeiculoAbordado:

        return VeiculoAbordado(placa = placa,
                            modelo = modelo,
                            ano = ano,cor =cor,
                            proprietario = proprietario)