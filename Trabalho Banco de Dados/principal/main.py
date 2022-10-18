from utils import config
from utils.splash_screen import SplashScreen
from reports.relatorios import Relatorio
from controller.controller_livro import Controller_Livro
from controller.controller_cliente import Controller_Cliente
from controller.controller_funcionario import Controller_Funcionario
from controller.controller_aluguel import Controller_Aluguel

tela_inicial = SplashScreen()
relatorio = Relatorio()
ctrl_livro = Controller_Livro()
ctrl_cliente = Controller_Cliente()
ctrl_funcionario = Controller_Funcionario()
ctrl_aluguel = Controller_Aluguel()

def reports(opcao_relatorio:int=0):

    if opcao_relatorio == 1:
        relatorio.get_relatorio_cliente()            
    elif opcao_relatorio == 2:
        relatorio.get_relatorio_funcionario()
    elif opcao_relatorio == 3:
        relatorio.get_relatorio_livro()
    elif opcao_relatorio == 4:
        relatorio.get_relatorio_aluguel()

def inserir(opcao_inserir:int=0):

    if opcao_inserir == 1:                               
        novo_livro = ctrl_livro.inserir_livro()
    elif opcao_inserir == 2:
        novo_cliente = ctrl_cliente.inserir_cliente()
    elif opcao_inserir == 3:
        novo_funcionario = ctrl_funcionario.inserir_funcionario()
    elif opcao_inserir == 4:
        novo_aluguel = ctrl_aluguel.inserir_aluguel()

def atualizar(opcao_atualizar:int=0):

    if opcao_atualizar == 1:
        relatorio.get_relatorio_livro()
        produto_atualizado = ctrl_livro.atualizar_livro()
    elif opcao_atualizar == 2:
        relatorio.get_relatorio_cliente()
        cliente_atualizado = ctrl_cliente.atualizar_cliente()
    elif opcao_atualizar == 3:
        relatorio.get_relatorio_funcionario()
        funcionario_atualizado = ctrl_funcionario.atualizar_funcionario()
    elif opcao_atualizar == 4:
        relatorio.get_relatorio_aluguel()
        aluguel_atualizado = ctrl_aluguel.atualizar_aluguel()

def excluir(opcao_excluir:int=0):

    if opcao_excluir == 1:
        relatorio.get_relatorio_livro()
        ctrl_livro.excluir_livro()
    elif opcao_excluir == 2:                
        relatorio.get_relatorio_cliente()
        ctrl_cliente.excluir_cliente()
    elif opcao_excluir == 3:                
        relatorio.get_relatorio_funcionario()
        ctrl_funcionario.excluir_funcionario()
    elif opcao_excluir == 4:                
        relatorio.get_relatorio_aluguel()
        ctrl_aluguel.excluir_aluguel()

def run():
    print(tela_inicial.get_updated_screen())
    config.clear_console()

    while True:
        print(config.MENU_PRINCIPAL)
        opcao = int(input("Escolha uma opção [1-5]: "))
        config.clear_console(1)
        
        if opcao == 1:
            
            print(config.MENU_RELATORIOS)
            opcao_relatorio = int(input("Escolha uma opção [0-5]: "))
            config.clear_console(1)

            reports(opcao_relatorio)

            config.clear_console(1)

        elif opcao == 2:
            
            print(config.MENU_ENTIDADES)
            opcao_inserir = int(input("Escolha uma opção [1-4]: "))
            config.clear_console(1)

            inserir(opcao_inserir=opcao_inserir)

            config.clear_console()
            print(tela_inicial.get_updated_screen())
            config.clear_console()

        elif opcao == 3:

            print(config.MENU_ENTIDADES)
            opcao_atualizar = int(input("Escolha uma opção [1-4]: "))
            config.clear_console(1)

            atualizar(opcao_atualizar=opcao_atualizar)

            config.clear_console()

        elif opcao == 4:

            print(config.MENU_ENTIDADES)
            opcao_excluir = int(input("Escolha uma opção [1-4]: "))
            config.clear_console(1)

            excluir(opcao_excluir=opcao_excluir)

            config.clear_console()
            print(tela_inicial.get_updated_screen())
            config.clear_console()

        elif opcao == 5:

            print(tela_inicial.get_updated_screen())
            config.clear_console()
            print("Obrigado por utilizar o nosso sistema.")
            exit(0)

        else:
            print("Opção incorreta.")
            exit(1)

if __name__ == "__main__":
    run()