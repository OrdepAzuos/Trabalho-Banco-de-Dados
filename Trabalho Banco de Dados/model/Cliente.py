from typing_extensions import Self

class Cliente: 
    def __init__(self, 
                 cpf_cliente:str=None, 
                 nome_cliente:str=None,
                 telefone_cliente:str=None
                ):
        self.set_cpf_cliente(cpf_cliente)
        self.set_nome_cliente(nome_cliente)
        self.set_telefone_cliente(telefone_cliente)

    def set_cpf_cliente(self, cpf_cliente:str):
        self.CPF_cliente = CPF_cliente

    def set_nome_cliente(self, nome_cliente:str):
        self.nome_cliente = nome_cliente

    def set_telefone_cliente(self, telefone_cliente:str):
        self.telefone_cliente = telefone_cliente

    def get_cpf_cliente(self) -> str:
        return self.cpf_cliente

    def get_nome_cliente(self) -> str:
        return self.nome_cliente
    
    def get_telefone_cliente(self) -> str:
        return self.telefone_cliente

    def to_string(self) -> str:
        return f"CPF do cliente: {self.get_cpf_cliente()} | Nome: {self.get_nome_cliente()} | Telefone: {self.get_telefone_cliente()}"
