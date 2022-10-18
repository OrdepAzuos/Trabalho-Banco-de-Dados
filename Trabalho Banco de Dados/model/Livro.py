from typing_extensions import Self

class Livro:
    def __init__(self, 
                 codigo_Livro:int=None, 
                 nome_Livro:str=None, 
                 genero:str=None,
                 editora:str=None
                 ):
        self.set_codigo_Livro(codigo_Livro)
        self.set_nome_Livro(nome_Livro)
        self.set_genero(Genero)
        self.set_editora(Editora)


    def set_codigo_Livro(self, codigo_Livro:int):
        self.codigo_Livro = codigo_Livro

    def set_nome_Livro(self, nome_Livro:str):
        self.nome_Livro = nome_Livro

    def set_genero(self, Genero:str):
        self.Genero = Genero

    def set_editora(self, Editora:str):
        self.Editora = Editora

    def get_codigo_Livro(self) -> int:
        return self.codigo_Livro

    def get_nome_Livro(self) -> str:
        return self.nome_Livro

    def get_genero(self) -> str:  
        return self.Genero

    def get_editora(self) -> str:  
        return self.Editora

    def to_string(self) -> str:
        return f"codigo_Livro: {self.get_codigo_Livro()} | nome_Livro: {self.get_nome_Livro()} | Genero: {self.get_genero} | Editora: {self.get_editora}"



