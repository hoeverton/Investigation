
from modelo.abordado import Abordado

class Abordagem:

    def __init__(self):
        self.cidade = input('Digite Cidade:')
        self.bairro =  None
        self.rua = None
        self.numeral = None
        self.data = None
        self.acompanhado = self.acompanhado()

    def acompanhado(self):
        self.contador = True

        while self.contador == True:

            self.acompanhado = input('Estava sozinho na hora da abordagem ? [S/N]')
            if self.acompanhado == 'n':
                self.envolvido = Abordado(self.rg)
            self.contador = False
            

      


