from modelo.abordagem import *
import json
from .abstrato import AbstratoRespoitorio


class AbordagemRepositorio(AbstratoRespoitorio):

    def criar_ou_atualizar(self, objeto):
        _objeto = self.banco.criar_ou_atualizar(objeto)

        abordados = []
        for abordado in _objeto.abordados:
            abord = self.banco.criar_ou_atualizar(abordado)
            self.banco.criar_ou_atualizar_relacao(_objeto.id, abord.id, _type="ABORDAGEM_ABORDOU")
            abordados.append(abord)

        i = 0
        j = 0
        while i < len(abordados):
            while j < len(abordados):
                if i != j:
                    self.banco.criar_ou_atualizar_relacao(abordados[i].id, abordados[j].id, _type="ABORDADO_PARCEIRO")
                j += 1
            i += 1

        _objeto.abordados = abordados

        _objeto.local = self.banco.criar_ou_atualizar(_objeto.local)
        self.banco.criar_ou_atualizar_relacao(_objeto.id, _objeto.local.id, is_unique=True, _type="ABORDAGEM_LOCAL")

        _objeto.veiculo = self.banco.criar_ou_atualizar(_objeto.veiculo)
        self.banco.criar_ou_atualizar_relacao(_objeto.id, _objeto.veiculo.id, _type="ABORDAGEM_VEICULO_AVERIGUADO")

        _objeto.boletim_ocorrencia = self.banco.criar_ou_atualizar(_objeto.boletim_ocorrencia)
        self.banco.criar_ou_atualizar_relacao(_objeto.id, _objeto.boletim_ocorrencia.id, _type="ABORDAGEM_TEM_BO")

    def carregar(self, abordagem_id) -> Abordagem:
        abordagem_no = self.banco.listar(Abordagem, f"id == '{abordagem_id}'")[0]
        abordagem_edges = self.banco.listar_relacoes(id_no_origem=abordagem_id)

        relacoes = [edge for edge in abordagem_edges if edge[1] == "->"]
        nos = {no for no in abordagem_edges if no[1] == "()"}
        obtem_relacao = lambda tipo: [relacao[0] for relacao in relacoes if tipo == json.loads(relacao[2])["_type"]]
        obtem_no = lambda id: [json.loads(no[2]) for no in nos if id == no[0]][0]
        tira_type = lambda data: {key: data[key] for key in data if key not in ("_type")}

        local_raw = tira_type(obtem_no(obtem_relacao("ABORDAGEM_LOCAL")[0]))
        veiculo_raw = tira_type(obtem_no(obtem_relacao("ABORDAGEM_VEICULO_AVERIGUADO")[0]))
        bo_raw = tira_type(obtem_no(obtem_relacao("ABORDAGEM_TEM_BO")[0]))
        abordados_raw = [tira_type(obtem_no(relacao)) for relacao in obtem_relacao("ABORDAGEM_ABORDOU")]

        local = Local(**local_raw)
        veiculo = VeiculoAbordado(**{key: veiculo_raw[key] for key in veiculo_raw if key != "obs"})
        for obs in veiculo_raw["obs"]:
            veiculo.add_observation(obs)

        bo = BoletimOcorrencia(**bo_raw)
        abordados = [Abordado(**abordado) for abordado in abordados_raw]

        return Abordagem(data=abordagem_no['data'],
                         local=local,
                         veiculo=veiculo,
                         abordados=abordados,
                         boletim_ocorrencia=bo)
