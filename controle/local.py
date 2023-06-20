from modelo.local import Local


class LocalControle:

     def __init__(self):
        pass

     @staticmethod
     def criar(cidade:str,
              bairro:str,
              rua:str,
              numeral:str)->Local:

       return  Local(cidade = cidade,
                     apelido = apelido,
                     rg = rg,
                     foto = foto)        