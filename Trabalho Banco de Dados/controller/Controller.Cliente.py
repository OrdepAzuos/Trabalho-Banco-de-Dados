from clientes import Cliente
from conexion.oracle_queries import OracleQueries

class Cliente:
    def __init__(self):
        pass
        
    def inserir_cliente(self) -> Cliente:
      
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        cpf = input("Insira o CPF: ")

        if self.verifica_existencia_cliente(oracle, cpf):
            nome_cliente = input("Insira o nome: ") 
            telefone_cliente = input("Insira o telefone: ")
            oracle.write(f"insert into clientes values ('{cpf}', '{nome_cliente}', '{telefone_cliente}')")
            df_cliente = oracle.sqlToDataFrame(f"select cpf, nome from clientes where cpf = '{cpf}'")
            novo_cliente = Cliente(df_cliente.cpf.values[0], df_cliente.nome_cliente.values[0], df_cliente.telefone_cliente.values[0])
            print(novo_cliente.to_string())
            return novo_cliente
        else:
            print(f"O CPF {cpf} já está cadastrado.")
            return None

    def atualizar_cliente(self) -> Cliente:
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        cpf = int(input("Digite o CPF do cliente que terá o nome alterado: "))

       
        if not self.verifica_existencia_cliente(oracle, cpf):
            novo_nome_cliente = input("Insira o novo nome: ")
            novo_telefone_cliente = input("Insira o novo telefone: ")
            oracle.write(f"update clientes set nome = '{novo_nome_cliente}', set telefone = '{novo_telefone_cliente}', where cpf = {cpf}")
            df_cliente = oracle.sqlToDataFrame(f"select cpf, nome from clientes where cpf = {cpf}")
            cliente_atualizado = Cliente(df_cliente.cpf.values[0], df_cliente.nome_cliente.values[0], df_cliente.telefone_cliente.values[0])
            print(cliente_atualizado.to_string())
            return cliente_atualizado
        else:
            print(f"O CPF {cpf} não existe.")
            return None

    def excluir_cliente(self):
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        cpf = int(input("Insira o CPF do cliente que será excluido: "))        
        if not self.verifica_existencia_cliente(oracle, cpf):            
            df_cliente = oracle.sqlToDataFrame(f"select cpf, nome from clientes where cpf = {cpf}")
            oracle.write(f"delete from clientes where cpf = {cpf}")            
            cliente_excluido =Cliente(df_cliente.cpf.values[0], df_cliente.nome_cliente.values[0], df_cliente.telefone_cliente.values[0])
            print("Cliente Removido com Sucesso!")
            print(cliente_excluido.to_string())
        else:
            print(f"O CPF {cpf} não existe.")

    def verifica_existencia_cliente(self, oracle:OracleQueries, cpf:str=None) -> bool:
        df_cliente = oracle.sqlToDataFrame(f"select cpf, nome from clientes where cpf = {cpf}")
        return df_cliente.empty