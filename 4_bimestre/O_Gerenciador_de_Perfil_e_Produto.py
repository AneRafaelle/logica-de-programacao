produto = {
    "codigo": 101,
    "nome": "Teclado Mecânico Gamer",
    "preco": 250.0,
    "estoque": 14
}

print("=== Produto Cadastro ===")
print(produto)
print(f"Nome do produto: {produto['nome']}")
print(f"Preço Unitário: R$ {produto['preco']}")
print("-" * 40)

produto["preco"] = 220.0
produto["estoque"] = produto["estoque"] + 6
produto["categoria"] = "Periféricos"

print("=== Produto Atualizado ===")
print(produto)
print(f"Novo preço: R$ {produto['preco']}")
print(f"Novo estoque: {produto['estoque']}")
print("-" * 40)

usuario = {
    "nome": "Carlos Eduardo",
    "nivel": "Administrador",
    "ativo": True
}

print("=== Cadastro do Usuário ===")
print(usuario)

print("Chaves do usuário:")
print(usuario.keys())

print("Valores do usuário:")
print(usuario.values())
print("-" * 40)
