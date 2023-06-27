from modelo.veiculo_abordado import VeiculoAbordado
from banco_de_dados import Database

class VeiculoAbordadoControle:

    def __init__(self):
        pass

    @staticmethod
    def criar(tipo: str,
                 placa: str,
                 modelo: str,
                 ano:str,
                 cor: str,
                 proprietario: Union[str, Abordado]) ->VeiculoAbordado: #
        #add variavel vaiculoAbordado obs "v" minusculo    
        veiculoAbordado = VeiculoAbordado(placa = placa,
                        modelo = modelo,
                        ano = ano,cor =cor,
                        proprietario = proprietario)

        Database.atualizar(veiculoAbordado)
        return(veiculoAbordado)
        

    @staticmethod
    def remover(placa:str):                        
        veiculoAbordado = Database.listar(VeiculoAbordado)
        Database.remover(veiculoAbordado)

    @staticmethod
    def atualizar(tipo: str,
                  placa: str,
                  modelo: str,
                  ano:str,
                  cor: str,
                  proprietario: str): #duvida se deixa assim ou com lista[Abordado]

         veiculoAbordado: VeiculoAbordado = Database.listar(VeiculoAbordado, f"placa =='{placa}'")[0]        
         veiculoAbordado.tipo = tipo
         veiculoAbordado.placa = placa
         veiculoAbordado.modelo = modelo
         veiculoAbordado.ano = ano
         veiculoAbordado.cor = cor
         veiculoAbordado.proprietario = proprietario

         Database.atualizar(veiculoAbordado)