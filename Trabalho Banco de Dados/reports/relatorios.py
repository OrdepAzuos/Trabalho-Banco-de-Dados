from conexion.oracle_queries import OracleQueries

class Relatorio:
    def __init__(self):
        with open("sql/relatorio_cliente.sql") as f:
            self.query_relatorio_cliente = f.read()


        with open("sql/relatorio_funcionario.sql") as f:
            self.query_relatorio_funcionario = f.read()


        with open("sql/relatorio_livro.sql") as f:
            self.query_relatorio_livro = f.read()


        with open("sql/relatorio_aluguel.sql") as f:
            self.query_relatorio_aluguel = f.read()


    def get_relatorio_cliente(self):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_relatorio_cliente))
        input("Pressione Enter para Sair do Relatório de Clientes")

    def get_relatorio_funcionario(self):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_relatorio_funcionario))
        input("Pressione Enter para Sair do Relatório de Fucionarios")

    def get_relatorio_livro(self):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_relatorio_livro))
        input("Pressione Enter para Sair do Relatório de Livros")

    def get_relatorio_aluguel(self):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_relatorio_aluguel))
        input("Pressione Enter para Sair do Relatório de Alugueis")
