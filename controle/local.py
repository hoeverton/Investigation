from modelo.local import Local
from banco_de_dados import Database

class LocalControle:

     def __init__(self):
        pass

     @staticmethod
     def criar(cidade:str,
              bairro:str,
              rua:str,
              numeral:str)->Local:

       local = Local(cidade = cidade,   #
                     bairro = bairro,
                     rua = rua,
                     numeral = numeral) 

       Database.atualizar(local)

     @staticmethod
     def remover(rua:str):

      local = Database.listar(local, f"rua == '{rua}'")[0]  
      Database.remover(local)

     @staticmethod
     def atualizar(cidade = cidade,   #
                    bairro = bairro,
                    rua = rua,
                    numeral = numeral): 
         
         local: Local = Database.listar(Abordado, f"rua == '{rua}'")[0]
         local.cidade = cidade
         local.bairro = bairro
         local.rua = rua
         local.numeral = numeral

         Database.atualizar(local)
