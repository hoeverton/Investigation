from modelo.abordagem import Abordado
from banco_de_dados.mockdb import MockDB

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

        MockDB.upinsert(abordado)
        return abordado

    @staticmethod
    def remover(rg: str):
        abordados = MockDB.lista(Abordado)
        abordado = [ a for a in abordados if a.rg == rg][0]
        MockDB.remove(abordado)

    @staticmethod
    def atualizar(rg: str,
                nome: str,
                apelido: str,
                foto: str = None):
        pass
