from biblioteca import *
from crud_usuarios import *

while True:

    logando = True
    executa_programa = False

    limpar_tela()

    while logando:
        limpar_tela()
        exibir_titulo("menu de login")
        opcao = input("""Cadastrar novo usuário ou fazer login com usuário existente?

[1] - Cadastrar novo usuário
[2] - Logar com usuário existente
[3] - Apagar usuário existente
[0] - Sair          
                    
-> """)

        match opcao:
            case "1":
                limpar_tela()
                exibir_titulo("cadastrar novo usuário")
                email = input("Email: ")
                senha = input("Senha: ")
                if cadastrar_usuario(email, senha):
                    print("Usuário cadastrado com sucesso!")
                else:
                    print("Erro: Usuário já existe.")
                input("Pressione Enter para continuar...")
            case "2":
                while True:
                    limpar_tela()
                    exibir_titulo("fazer login")
                    email = input("Email: ")
                    senha = input("Senha: ")
                    usuario_logado_id = verificar_login(email, senha)
                    if usuario_logado_id:
                        print("Login bem-sucedido!")
                        logando = False
                        executa_programa = True
                        break
                    else:
                        print("Email ou senha incorretos. Tente novamente.")
                    input("Pressione Enter para continuar...")
            case "3":
                limpar_tela()
                exibir_titulo("apagar usuário existente")
                email = input("Email: ")
                senha = input("Senha: ")
                try:
                    if apagar_usuario(email, senha):
                        print("Usuário apagado com sucesso.")
                    else:
                        print("Erro: Usuário não encontrado ou senha incorreta.")
                except Exception as e:
                    exibir_titulo(f"erro: {e}")
            case "0":
                limpar_tela()
                exibir_titulo("saindo do sistema...")
                exit()
            case _:
                print("Opção inválida. Tente novamente.")

        input("Pressione Enter para continuar...")

    while executa_programa:
        limpar_tela()
        exibir_titulo("painel administrativo auralis")
        print("""1 - Adicionar registro diário
2 - Visualizar registros diários
3 - Enviar feedback
4 - Visualizar feedbacks
5 - Ativar notificações
6 - Voltar para menu de login
0 - Sair""")
        
        escolha = input("-> ")

        match escolha:
            case "1":
                limpar_tela()
                exibir_titulo("adicionar registro diário")
                input("Pressione Enter para continuar...")
            case "2":
                limpar_tela()
                exibir_titulo("visualizar registros diários")
                input("Pressione Enter para continuar...")
            case "3":
                limpar_tela()
                exibir_titulo("enviar feedback")
                input("Pressione Enter para continuar...")
            case "4":
                limpar_tela()
                exibir_titulo("visualizar feedbacks")
                input("Pressione Enter para continuar...")
            case "5":
                limpar_tela()
                exibir_titulo("ativar notificações")
                input("Pressione Enter para continuar...")
            case "6":
                executa_programa = False
            case "0":
                limpar_tela()
                exibir_titulo("saindo do sistema...")
                exit()
            case _:
                print("Opção inválida. Tente novamente.")
                input("Pressione Enter para continuar...")