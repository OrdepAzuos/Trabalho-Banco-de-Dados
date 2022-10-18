import random
from livro import Livro
from conexion.oracle_queries import OracleQueries

class Livro:
    def __init__(self):
        pass
        
    def inserir_livro(self) -> Livro:
        
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        cod_livro = random.randint(1,1000)

        if self.verifica_existencia_livro(oracle, cod_livro):
            nome = input("Digite o nome do livro: ") 
            editora = input("Digite o nome da editora do livro: ") 
            genero = input("Digite o gênero do livro: ")
            oracle.write(f"insert into livros values ('{cod_livro}', '{nome}', '{editora}', '{genero}')")
            df_livro = oracle.sqlToDataFrame(f"select cod_livro, nome from livros where cod_livro = '{cod_livro}'")
            novo_livro = Livro(df_livro.cod_livro.values[0], df_livro.nome.values[0], df_livro.editora.values[0], df_livro.genero.values[0])
            print(novo_livro.to_string())
            return novo_livro
        else:
            print(f"O cod_livro {cod_livro} já está cadastrado.")
            return None


    def excluir_livro(self):
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        cod_livro = int(input("Insira o codigo do livro que será excluido: "))        
        if not self.verifica_existencia_livro(oracle, cod_livro):            
            df_livro = oracle.sqlToDataFrame(f"select cod_livro, nome from livros where cod_livro = {cod_livro}")
            oracle.write(f"delete from livros where cod_livro = {cod_livro}")            
            livro_excluido = Livro(df_livro.cod_livro.values[0], df_livro.nome.values[0], df_livro.editora.values[0], df_livro.genero.values[0])
            print("Livro Removido com Sucesso!")
            print(livro_excluido.to_string())
        else:
            print(f"O cod_livro {cod_livro} não existe.")

    def verifica_existencia_livro(self, oracle:OracleQueries, cod_livro:str=None) -> bool:
        df_livro = oracle.sqlToDataFrame(f"select cod_livro, nome from livros where cod_livro = {cod_livro}")
        return df_livro.empty