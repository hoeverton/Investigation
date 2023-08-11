

class Abordado:

    def __init__(self,
                 nome: str,
                 apelido: str,
                 rg: str,
                 foto: str = None):

        self.nome = nome
        self.apelido = apelido
        self.rg = rg
        self.foto = foto

    def __dict__(self):
        return {
            "nome": self.nome,
            "apelido": self.apelido,
            "rg": self.rg,
            "foto": self.foto
        }
