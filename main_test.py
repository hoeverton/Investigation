from datetime import datetime


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

    abordagem = AbordagemControle.criar(
        cidade="Curitiba",
        bairro="CIC",
        rua="R. das Flores",
        numeral="1010",
        abordados=[abordado1, abordado2],
        veiculo_cor='preto',
        veiculo_modelo='passat',
        veiculo_placa='aaa333',
        veiculo_proprietario='karen',
        veiculo_ano='1999',
        veiculo_tipo='passeio',
        bo_numero='1234',
        bo_natureza='2345',
        data=datetime(2023, 8, 12)
    )

    repo = AbordagemRepositorio(abordagem)
    repo.criar()

