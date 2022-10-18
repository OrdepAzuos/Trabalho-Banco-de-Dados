from funcionario import Funcionario
from conexion.oracle_queries import OracleQueries

class Funcionario:
    def __init__(self):
        pass
        
    def inserir_funcionario(self) -> Funcionario:
        ''' Ref.: https://cx-oracle.readthedocs.io/en/latest/user_guide/plsql_execution.html#anonymous-pl-sql-blocks'''
        
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        matricula = input("Matricula (Novo): ")

        if self.verifica_existencia_funcionario(oracle, matricula):
            nome_funcionario = input("Entre com o nome do funcionario: ") 
            telefone_funcionario = input("Entre com o telefone do funcionario: ") 
            oracle.write(f"insert into funcionarios values ('{matricula}', '{nome_funcionario}, '{telefone_funcionario}')")
            df_funcionario = oracle.sqlToDataFrame(f"select matricula, nome from funcionarios where matricula = '{matricula}'")
            novo_funcionario = Funcionario(df_funcionario.matricula.values[0], df_funcionario.nome_funcionario.values[0], df_funcionario.telefone_funcionario.values[0])
            print(novo_funcionario.to_string())
            return novo_funcionario
        else:
            print(f"A matricula {matricula} já está cadastrado.")
            return None

    def atualizar_funcionario(self) -> Funcionario:
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        matricula = int(input("Digite a matricula do funcionario que terá o nome alterado: "))

       
        if not self.verifica_existencia_funcionario(oracle, matricula):
            novo_nome_func = input("Insira o novo nome: ")
            novo_telefone_func = input("Insira o novo nome: ")
            oracle.write(f"update funcionarios set nome = '{novo_nome_func}', set telefone = '{novo_telefone_func}' where matricula = {matricula}")
            df_funcionario = oracle.sqlToDataFrame(f"select matricula, nome from funcionarios where matricula = {matricula}")
            funcionario_atualizado = Funcionario(df_funcionario.matricula.values[0], df_funcionario.nome.values[0], df_funcionario.telefone_func.values[0])
            print(funcionario_atualizado.to_string())
            return funcionario_atualizado
        else:
            print(f"A matricula {matricula} não existe.")
            return None

    def excluir_funcionario(self):
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        matricula = int(input("Insira a matricula do funcionario que será excluido: "))        
        if not self.verifica_existencia_funcionario(oracle, matricula):            
            df_funcionario = oracle.sqlToDataFrame(f"select matricula, nome from funcionarios where matricula = {matricula}")
            oracle.write(f"delete from funcionarios where matricula = {matricula}")            
            funcionario_excluido = Funcionario(df_funcionario.matricula.values[0], df_funcionario.nome_funcionario.values[0], df_funcionario.telefone_funcionario.values[0])
            print("Funcionario Removido com Sucesso!")
            print(funcionario_excluido.to_string())
        else:
            print(f"A matricula {matricula} não existe.")

    def verifica_existencia_funcionario(self, oracle:OracleQueries, matricula:str=None) -> bool:
        df_funcionario = oracle.sqlToDataFrame(f"select matricula, nome from funcionarios where matricula = {matricula}")
        return df_funcionario.empty