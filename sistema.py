from biblioteca import *

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
                input("Pressione Enter para continuar...")
            case "2":
                limpar_tela()
                exibir_titulo("fazer login")
                logando = False
                executa_programa = True
                input("Pressione Enter para continuar...")
            case "3":
                limpar_tela()
                exibir_titulo("apagar usuário existente")
                input("Pressione Enter para continuar...")

    while executa_programa:
        limpar_tela()
        exibir_titulo("painel administrador auralis")
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