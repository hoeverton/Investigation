from ..modelo.abordagem import Abordado


class AbordadoControle:

    @staticmethod
    def criar(nome: str,
              apelido: str,
              rg: str,
              foto: str = None) -> Abordado:

        # todo - utilizar método upinsert no banco de dados

        return Abordado(nome=nome,
                        apelido=apelido,
                        rg=rg,
                        foto=foto)
