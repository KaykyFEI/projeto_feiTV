# Esse módulo contém as funções de cadastro, login e redefinação de senha

import os
import json

arquivo = ".\dados\usuarios.json"

def validarEmail(email):
    pass

def carregarUsuarios():
    if not os.path.exists(arquivo):
        return []
    with open(arquivo, "r", encoding="utf-8") as arq:
        try:
            return json.load(arq)
        except json.JSONDecodeError:
            return[]


def verificarDuplicata(valor, campo):
    usuarios = carregarUsuarios()
    for usuario in usuarios:
        if usuario.get(campo) == valor:
            return True
    return False

def salvarUsuario(novoUsuario):
    usuarios = carregarUsuarios()
    usuarios.append(novoUsuario)
    with open(arquivo, "w", encoding="utf-8") as arq:
        json.dump(usuarios, arq, indent=4, ensure_ascii=False)