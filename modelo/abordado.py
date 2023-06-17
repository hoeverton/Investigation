from modelo.abordagem import Abordagem

class Abordado:
    def __init__(self, nome, apelido, rg):
        self.nome = nome
        self.apelido = apelido
        self.rg = int()
        self.abordagem = Abordagem()

    def foto(self):
        print('FOTO')
