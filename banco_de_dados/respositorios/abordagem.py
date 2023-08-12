from modelo.abordagem import Abordagem
from .abstrato import AbstratoRespoitorio


class AbordagemRepositorio(AbstratoRespoitorio):

    def __init__(self, abordagem: Abordagem):
        super().__init__(objeto=abordagem)

    def criar(self):
        self.objeto = self.banco.criar(self.objeto)

        abordados = []
        for abordado in self.objeto.abordados:
            abord = self.banco.criar(abordado)
            self.banco.criar_relacao(self.objeto.id, abord.id, _type="ABORDAGEM_ABORDOU")
            abordados.append(abord)

        i = 0
        j = 0
        while i < len(abordados):
            while j < len(abordados):
                if i != j:
                    self.banco.criar_relacao(abordados[i].id, abordados[j].id, _type="ABORDADO_PARCEIRO")
                j += 1
            i += 1

        self.objeto.abordados = abordados

        self.objeto.local = self.banco.criar(self.objeto.local)
        self.banco.criar_relacao(self.objeto.id, self.objeto.local.id, is_unique=True, _type="ABORDAGEM_LOCAL")

        self.objeto.veiculo = self.banco.criar(self.objeto.veiculo)
        self.banco.criar_relacao(self.objeto.id, self.objeto.veiculo.id, _type="ABORDAGEM_VEICULO_AVERIGUADO")

        self.objeto.boletim_ocorrencia = self.banco.criar(self.objeto.boletim_ocorrencia)
        self.banco.criar_relacao(self.objeto.id, self.objeto.boletim_ocorrencia.id, _type="ABORDAGEM_TEM_BO")
