def cadastro(usuario, email, senha, dica):
    novo_usuario = {
        "usuario": usuario,
        "email": email,
        "senha": senha,
        "dica": dica
    }

    print(f"Usuário {usuario} cadastrado com sucesso!")
    return novo_usuario