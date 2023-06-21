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

        Database.atualizar(abordado)
        return abordado

    @staticmethod
    def remover(rg: str):
        abordado = Database.lista(Abordado, f"rg == {rg}")[0]
        Database.remove(abordado)

    @staticmethod
    def atualizar(rg: str,
                nome: str,
                apelido: str,
                foto: str = None):

        instancia: Abordado = Database.lista(Abordado, f"rg == {rg}")[0]
        instancia.nome = nome
        instancia.apelido = apelido
        instancia.foto = foto

        Database.atualizar(instancia)