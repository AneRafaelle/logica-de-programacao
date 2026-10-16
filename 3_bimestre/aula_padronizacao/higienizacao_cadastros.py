nome = " joão pedro da silva "
email = " JOAO.SILVA@Escola.COM "

nome = nome.strip().upper()
email = email.strip().lower()

print("Nome higienizado:", nome)
print("E-mail higienizado:", email)

cpf = " 123.456.789-00 "
telefone = "(11) 99999-8888"

cpf = cpf.strip().replace(".", "").replace("-", "").replace(" ", "")
telefone = telefone.strip().replace(".", "").replace("-", "").replace("(", "").replace(")", "").replace(" ", "")

print("CPF limpo:", cpf)
print("Telefone limpo:", telefone)

codigo = " prod-1024-br-sp "

codigo = codigo.strip().upper().replace("-", "_")

print("Código formatado:", codigo)

print("\n--- RESULTADOS ---")
print("Nome higienizado: JOÃO PEDRO DA SILVA")
print("E-mail higienizado: joao.silva@escola.com")
print("CPF limpo: 12345678900")
print("Telefone limpo: 11999998888")
print("Código formatado: PROD_1024_BR_SP")
