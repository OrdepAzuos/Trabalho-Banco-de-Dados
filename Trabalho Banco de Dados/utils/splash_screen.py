from conexion.oracle_queries import OracleQueries
from utils import config

class SplashScreen:

    def __init__(self):
        self.qry_total_livros = config.QUERY_COUNT.format(tabela="livros")
        self.qry_total_clientes = config.QUERY_COUNT.format(tabela="clientes")
        self.qry_total_funcionarios = config.QUERY_COUNT.format(tabela="funcionarios")
        self.qry_total_pedidos = config.QUERY_COUNT.format(tabela="alugueis")

        self.created_by = "Alcides Souza Mergulhão\n"+"Bruno Barbosa Fernandes\n"+"Filipe Freitas Alves Rosa\n"+"Pedro Henrique de Souza Almeida"
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2022/2"

    def get_total_livros(self):
        oracle = OracleQueries()
        oracle.connect()
        return oracle.sqlToDataFrame(self.qry_total_livros)["total de livros"].values[0]

    def get_total_clientes(self):
        oracle = OracleQueries()
        oracle.connect()
        return oracle.sqlToDataFrame(self.qry_total_clientes)["total de clientes"].values[0]

    def get_total_funcionarios(self):
        oracle = OracleQueries()
        oracle.connect()
        return oracle.sqlToDataFrame(self.qry_total_funcionarios)["total_funcionarios"].values[0]

    def get_total_alugueis(self):
        oracle = OracleQueries()
        oracle.connect()
        return oracle.sqlToDataFrame(self.qry_alugueis)["total de alugueis"].values[0]

    def get_updated_screen(self):
        return f"""
        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        |                     Biblioteca                       |
        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++                                                       
        | REGISTROS:                                    
        |     1 - LIVROS:           {str(self.get_total_produtos()).rjust(5)}
        |     2 - CLIENTES:         {str(self.get_total_clientes()).rjust(5)}
        |     3 - FUNCIONARIOS:     {str(self.get_total_funcionarios()).rjust(5)}
        |     4 - ALUGUEIS:         {str(self.get_total_alugueis()).rjust(5)}
        |
        |  CRIADO POR: {self.created_by}
        |
        |  PROFESSOR:  {self.professor}
        |
        |  DISCIPLINA: {self.disciplina}
        |              {self.semestre}
        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        """

  
