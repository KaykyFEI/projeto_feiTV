def telaMenuPrincipal():
    # Exibe as opcoes do menu inicial
    print(
        "\nSelecione uma das opções abaixo:",
        "1) Criar uma nova conta",
        "2) Fazer login",
        "3) Buscar vídeo",
        "4) Favoritos",
        "5) Lista de Reprodução",
        "6) Fazer login como admin",
        "7) Sair",
        sep="\n\n",
        end="\n\n",
    )
    # Declaracao da variavel opcao.
    opcao = 0
    # Laco de repeticao para entrada da opcao e verificacao do valor
    while True:
    # Entrada do valor
        entrada = input("Digite uma opção: ")
    # Tratamento de excecao com a instrucao try.
        try:
            opcao = int(entrada)
            if 1 <= opcao <= 7:
                break
            else:
                print("\nOpção inválida. Tente novamente.\n")
                opcao = 0
        except ValueError:
            print("Opção inválida. Tente novamente.\n")
    # Execucao da opcao escolhida
    if opcao == 1:
        email = ""
        usuario = ""
        senha = ""
        dica = ""

        email = input("Digite o seu email: ")
