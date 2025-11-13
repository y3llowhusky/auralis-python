from biblioteca import *
from crud_usuarios import *
from crud_registros import *
from crud_feedbacks import *

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
                cadastrando = True
                while cadastrando:
                    limpar_tela()
                    exibir_titulo("cadastrar novo usuário")
                    email = input("Email (deixe em branco para voltar): ")
                    if email.strip() == "":
                        break
                    if not validar_campo("email", email):
                        print("Erro: Email inválido.")
                        input("\nPressione Enter para continuar...")
                        continue
                    elif not verificar_usuario_novo(email):
                        print("Erro: Já existe um usuário cadastrado com esse email!")
                        input("\nPressione Enter para continuar...")
                        continue
                    senha = input("Senha: ")
                    if not validar_campo("senha", senha):
                        print("Erro: Senha inválida. A senha deve ter pelo menos 6 caracteres.")
                        input("\nPressione Enter para continuar...")
                        continue
                    nome_usuario = input("Nome: ")
                    if not validar_campo("nome", nome_usuario):
                        print("Erro: Nome inválido. O nome deve ter pelo menos 2 caracteres.")
                        input("\nPressione Enter para continuar...")
                        continue
                    genero = input("Gênero ( [M]asculino, [F]eminino, [O]utro ): ")
                    if not validar_campo("genero", genero):
                        print("Erro: Gênero inválido. Use M, F ou O.")
                        input("\nPressione Enter para continuar...")
                        continue
                    data_nascimento = "placeholder"
                    while not validar_campo("data_nascimento", data_nascimento):
                        data_nascimento = input("Data de Nascimento (DD/MM/AAAA): ")
                        if not validar_campo("data_nascimento", data_nascimento):
                            print("Erro: Data de nascimento inválida.")
                            input("\nPressione Enter para continuar...")

                    if cadastrar_usuario(email, senha, nome_usuario, genero, data_nascimento):
                        print("Usuário cadastrado com sucesso!")
                        cadastrando = False
                    else:
                        print("Erro ao cadastrar usuário.")
                        cadastrando = False

            case "2":
                while True:
                    limpar_tela()
                    exibir_titulo("fazer login")
                    print("Digite suas credenciais para fazer login (deixe em branco para retornar ao menu de login).\n")
                    email = input("Email: ")
                    senha = input("Senha: ")
                    if not email and not senha:
                        break
                    usuario_logado_id = verificar_login(email, senha)
                    if usuario_logado_id:
                        usuario["nome"] = executar_comando(
                            "SELECT nome_usuario FROM auralis_usuarios WHERE id_usuario = :1",
                            {"1": usuario_logado_id},
                            fetch=True
                        )[0][0]
                        exibir_titulo("login bem-sucedido!")
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
                input("Pressione Enter para continuar...")
                exit()
            case _:
                print("Opção inválida. Tente novamente.")

        input("\nPressione Enter para continuar...")

    while executa_programa:
        limpar_tela()
        exibir_titulo("painel administrativo auralis")
        print("""\n1 - Adicionar registro diário
2 - Visualizar histórico de registros
3 - Enviar feedback
4 - Visualizar histórico de feedbacks
5 - Ativar / desativar notificações
6 - Alterar senha do usuário             
7 - Voltar para menu de login
0 - Sair\n""")
        
        escolha = input("-> ")

        match escolha:
            case "1":
                limpar_tela()
                exibir_titulo("adicionar registro diário")
                if verificar_registro_hoje(usuario_logado_id):
                    print("Você já adicionou um registro diário hoje. Volte amanhã para manter sua consistência!")
                    input("Pressione Enter para continuar...")
                    continue
                else:
                    preencher_dicionario(registro_diario)
                    if salvar_registro(registro_diario, usuario_logado_id):
                        score_diario = calcular_score(registro_diario)
                        print("Registro diário salvo com sucesso!")
                        exibir_titulo(f"Score do dia: {score_diario}")
                        if score_diario <= 20:
                            print("Seu score do dia está PÉSSIMO. É importante melhorar seus hábitos diários.")
                        elif 20 < score_diario <= 45:
                            print("Seu score do dia está RUIM. Há espaço para melhorias em seus hábitos diários.")
                        elif 45 < score_diario < 65:
                            print("Seu score do dia está REGULAR. Continue se esforçando para melhorar seus hábitos diários.")
                        elif 65 <= score_diario < 85:
                            print("Seu score do dia está BOM. Mas sempre há espaço para melhorias.")
                        else:
                            print("Parabéns! Seu score do dia está EXCELENTE. Continue mantendo seus bons hábitos diários.")
                    else:
                        print("Erro ao salvar registro diário.")
                input("\nPressione Enter para continuar...")

            case "2":
                limpar_tela()
                exibir_titulo("visualizar histórico de registros")
                listar_registros(usuario_logado_id, usuario["nome"])
                input("Pressione Enter para continuar...")

            case "3":
                limpar_tela()
                exibir_titulo("enviar feedback")
                input("Pressione Enter para continuar...")

            case "4":
                limpar_tela()
                exibir_titulo("visualizar histórico de feedbacks")
                input("Pressione Enter para continuar...")

            case "5":
                limpar_tela()
                exibir_titulo("ativar / desativar notificações")
                input("Pressione Enter para continuar...")

            case "6":
                limpar_tela()
                exibir_titulo("alterar senha do usuário")
                senha_atual = input("Senha atual: ")
                nova_senha = input("Nova senha: ")

                if atualizar_senha(usuario_logado_id, senha_atual, nova_senha):
                    print("Senha alterada com sucesso!")
                else:
                    print("Erro ao alterar senha. Verifique a senha atual e tente novamente.")
                input("Pressione Enter para continuar...")

            case "7":
                executa_programa = False
                logando = True

            case "0":
                limpar_tela()
                exibir_titulo("saindo do sistema...")
                input("Pressione Enter para continuar...")
                exit()

            case _:
                print("Opção inválida. Tente novamente.")
                input("Pressione Enter para continuar...")