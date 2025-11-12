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
                if not validar_campo("email", email):
                    print("Erro: Email inválido.")
                    input("Pressione Enter para continuar...")
                    continue
                elif not verificar_usuario_novo(email):
                    print("Erro: Usuário já existe.")
                    input("Pressione Enter para continuar...")
                    continue
                senha = input("Senha: ")
                if not validar_campo("senha", senha):
                    print("Erro: Senha inválida. A senha deve ter pelo menos 6 caracteres.")
                    input("Pressione Enter para continuar...")
                    continue
                nome_usuario = input("Nome: ")
                if not validar_campo("nome", nome_usuario):
                    print("Erro: Nome inválido. O nome deve ter pelo menos 2 caracteres.")
                    input("Pressione Enter para continuar...")
                    continue
                genero = input("Gênero ( [M]asculino, [F]eminino, [O]utro ): ")
                if not validar_campo("genero", genero):
                    print("Erro: Gênero inválido. Use M, F ou O.")
                    input("Pressione Enter para continuar...")
                    continue
                data_nascimento = "placeholder"
                while not validar_campo("data_nascimento", data_nascimento):
                    data_nascimento = input("Data de Nascimento (DD/MM/AAAA): ")
                    if not validar_campo("data_nascimento", data_nascimento):
                        print("Erro: Data de nascimento inválida.")
                        input("Pressione Enter para continuar...")
                if cadastrar_usuario(email, senha, nome_usuario, genero, data_nascimento):
                    print("Usuário cadastrado com sucesso!")
                else:
                    print("Erro ao cadastrar usuário.")
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
                input("Pressione Enter para continuar...")
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