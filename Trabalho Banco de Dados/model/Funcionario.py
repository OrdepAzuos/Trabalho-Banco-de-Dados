class Funcionario:
    def __init__(self, 
                 matricula:str=None, 
                 nome_funcionario:str=None, 
                 telefone_funcionario:str=None
                 ):
        self.set_matricula(matricula)
        self.set_nome_funcionario(nome_funcionario)
        self.set_telefone_funcionario(telefone_funcionario)

    def set_matricula(self, matricula:str):
        self.matricula = matricula

    def set_nome_funcionario(self, nome_funcionario:str):
        self.nome_funcionario = nome_funcionario

    def set_telefone_funcionario(self, telefone_funcionario:str):
        self.telefone_funcionario = telefone_funcionario

    def get_matricula(self) -> str:
        return self.matricula

    def get_nome_funcionario(self) -> str:
        return self.nome_funcionario

    def get_telefone_funcionario(self) -> str:
        return self.telefone_funcionario

    def to_string(self) -> str:
        return f"matricula: {self.get_matricula()} | nome funcionario: {self.get_nome_funcionario()} | telefone funcionario: {self.get_telefone_funcionario()}"