from datetime import date
from clientes import Cliente
from funcionario import Funcionario
from livro import Livro

class Pedido:
    def __init__(self, 
                 cod_emprestimo:str=None,
                 livro:Livro=None,
                 data_emprestimo:date=None,
                 data_devolucao:date=None,
                 cliente:Cliente= None,
                 funcionario:Funcionario=None
                 ):
        self.set_cod_emprestimo(cod_emprestimo)
        self.set_livro(livro)
        self.set_data_emprestimo(data_emprestimo)
        self.set_data_devolucao(data_devolucao)
        self.set_cliente(cliente)
        self.set_funcionario(funcionario)

    def set_cod_emprestimo(self, cod_emprestimo:str):
        self.cod_emprestimo = cod_emprestimo
    
    def set_livro(self, livro:Livro):
        self.livro = livro

    def set_data_emprestimo(self, data_emprestimo:date):
        self.data_emprestimo = data_emprestimo
    
    def set_data_devolucao(self, data_devolucao:date):
        self.data_devolucao = data_devolucao

    def set_cliente(self, cliente:Cliente):
        self.cliente = cliente

    def set_funcionario(self, funcionario: Funcionario):
        self.funcionario = funcionario

    def get_cod_emprestimo(self) -> str:
        return self.cod_emprestimo
      
    def get_livro(self) -> Livro:
        return self.livro

    def get_data_emprestimo(self) -> date:
        return self.data_emprestimo

    def get_data_devolucao(self) -> date:
        return self.data_devolucao

    def get_cliente(self) -> Cliente:
        return self.cliente

    def get_funcionario(self) -> Funcionario:
        return self.funcionario

    def to_string(self) -> str:
        return f"Codigo do Emprestimo: {self.get_cod_emprestimo()} | Codigo do livro: {self.get_livro().get_cod_livro()} | Data de Emprestimo: {self.get_data_emprestimo()} | Data de Devolucao: {self.get_data_devolucao()} | Cliente: {self.get_cliente().get_CPF_cliente()} | Funcionario: {self.get_funcionario().get_CPF_func()}"