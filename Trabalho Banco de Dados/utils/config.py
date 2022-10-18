MENU_PRINCIPAL = """
+-------------------------+
|     Menu Principal      |
+-------------------------+
| (1) Relatórios          |
| (2) Inserir Registros   |
| (3) Atualizar Registros |
| (4) Remover Registros   |
| (5) Sair                |
+-------------------------+
"""

MENU_RELATORIOS = """
+-------------------------------------------------------+
|                       Relatórios                      |
+-------------------------------------------------------+
| (1) Relatório de Clientes                             |
| (2) Relatório de Funcionarios                         |
| (3) Relatório de Livros                               |
| (4) Relatório dos Alugueis                            |
| (5) Sair                                              |
+-------------------------------------------------------+
"""

MENU_ENTIDADES = """
+-------------------------------------------------------+
|                       Entidades                       |
+-------------------------------------------------------+
| (1) Livros                                            |
| (2) Clientes                                          |
| (3) Funcionarios                                      |
| (4) Alugueis                                          |
+-------------------------------------------------------+
"""

QUERY_COUNT = 'select count(1) as total_{tabela} from {tabela}'

def clear_console(wait_time:int=3):
    '''
       Esse método limpa a tela após alguns segundos
       wait_time: argumento de entrada que indica o tempo de espera
    '''
    import os
    from time import sleep
    sleep(wait_time)
    os.system("clear")