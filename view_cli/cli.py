from controle.abordagem import AbordagemControle
from controle.abordado import AbordadoControle


class CLI:

    @staticmethod
    def boas_vindas():
        msg = ("Ola, escolha a opção desejada: \n"
               "    1 - criar abordagem\n"
               "    2 - listar abordagens")

        opcao = input(msg)
        map_opcoes = {
            "1": CLI.criar_abordagem,
            "2": CLI.listar_abordagens
        }
        map_opcoes[opcao]()

    @staticmethod
    def criar_abordagem():

        print("Informe os abordados:")
        tem_abordado: bool = True
        abordados = []

        while tem_abordado:
            abordado = AbordadoControle.criar(nome=input("nome: "),
                                              apelido=input("apelido: "),
                                              rg=input("rg: "))
            abordados.append(abordado)

            tem_abordado: str = input("Tem mais abordado? [s/n]")
            tem_abordado: bool = (tem_abordado.lower() == 's')

        tem_veiculo = input("Tem veiculo na abordagem? [s/n]")
        veiculo_props = {}
        if tem_veiculo.lower() == 's':
            veiculo_props = {"veiculo_cor": input("cor: "),
                             "veiculo_modelo": input("modelo: "),
                             "veiculo_placa":  input("placa: "),
                             "veiculo_ano":  input("ano: "),# add input
                             "veiculo_proprietario":  input("proprietario: "),
                             "veiculo_tipo":  input("tipo: ")}

        tem_bo = input("tem BO? [s/n]")
        bo_props = {}
        if tem_bo.lower() == 's':
            bo_props = {"bo_numero": input("numero: "),
                        "bo_natureza": input("natureza: ")}

        print(AbordagemControle.criar(cidade=input("cidade: "),
                                      bairro=input("bairro: "),
                                      rua=input("rua: "),
                                      numeral=input("numero: "),
                                      abordados=abordados,
                                      **veiculo_props,
                                      **bo_props).__dict__)


    @staticmethod
    def listar_abordagens():
        pass