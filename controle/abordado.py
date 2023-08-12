from modelo.abordagem import Abordado
from banco_de_dados import Database


class AbordadoControle:

    @staticmethod
    def criar(nome: str,
              apelido: str,
              rg: str,
              foto: str = None) -> Abordado:
        abordado = Abordado(nome=nome,
                            apelido=apelido,
                            rg=rg,
                            foto=foto)

        # Database.atualizar(abordado)
        return abordado

    @staticmethod
    def remover(rg: str):
        abordado = Database.listar(Abordado, f"rg == '{rg}'")[0]
        Database.remover(abordado)

    @staticmethod
    def atualizar(rg: str,
                  nome: str,
                  apelido: str,
                  foto: str = None):
        abordado: Abordado = Database.listar(Abordado, f"rg == '{rg}'")[0]
        abordado.nome = nome
        abordado.apelido = apelido
        abordado.foto = foto

        Database.atualizar(abordado)
