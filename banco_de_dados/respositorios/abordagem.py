from modelo.abordagem import Abordagem
from .abstrato import AbstratoRespoitorio


class AbordagemRepositorio(AbstratoRespoitorio):

    def __init__(self, abordagem: Abordagem):
        super().__init__(objeto=abordagem)

    def criar(self):
        pass