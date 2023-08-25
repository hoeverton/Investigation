from datetime import datetime
from simple_graph_sqlite.visualizers import graphviz_visualize
from simple_graph_sqlite import database as db

if __name__ == "__main__":
    from controle.abordagem import AbordagemControle
    from controle.abordado import AbordadoControle
    from banco_de_dados.respositorios.abordagem import AbordagemRepositorio

    abordado1 = AbordadoControle.criar(
        nome='felipe',
        apelido='fe',
        rg="1234556",
    )

    abordado2 = AbordadoControle.criar(
        nome='hoeverton',
        apelido='eto',
        rg="133323",
    )

    abordado3 = AbordadoControle.criar(
        nome='priscila',
        apelido='pri',
        rg="1212312",
    )

    abordagem = AbordagemControle.criar(
        cidade="Curitiba",
        bairro="CIC",
        rua="R. das Flores",
        numeral="10107777",
        abordados=[abordado1, abordado2],
        veiculo_cor='preto',
        veiculo_modelo='passat',
        veiculo_placa='aaa333',
        veiculo_proprietario='karen',
        veiculo_ano='1999',
        veiculo_tipo='passeio',
        bo_numero='1234',
        bo_natureza='2345',
        data=datetime(2023, 8, 12))

    repo = AbordagemRepositorio()
    repo.criar_ou_atualizar(objeto=abordagem)

    abordagem2 = AbordagemControle.criar(
        cidade="Curitiba",
        bairro="CIC",
        rua="R. das Flores",
        numeral="107750",
        abordados=[abordado2, abordado3],
        veiculo_cor='preto',
        veiculo_modelo='passat',
        veiculo_placa='aab233',
        veiculo_proprietario='karen',
        veiculo_ano='1999',
        veiculo_tipo='passeio',
        bo_numero='599595',
        bo_natureza='2345',
        data=datetime(2023, 7, 12))

    repo = AbordagemRepositorio()
    repo.criar_ou_atualizar(objeto=abordagem2)

    nodes = [abordado2.id]
    graphviz_visualize('investigation.graph', 'investigation.dot', nodes, hide_edge_key=True)
    graphviz_visualize('investigation.graph', 'investigation.dot', nodes, hide_edge_key=True, format='pdf')
