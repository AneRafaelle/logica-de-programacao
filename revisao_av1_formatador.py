def formatar_citacao(nome_completo):
    partes= nome_completo.strip().split()
    sobrenome= partes[-1].upper()
    primeiro_nome= "".join(partes[:-1])
    return sobrenome + ","+ primeiro_nome
def gerar_codigo(ano,cp):
    cpf_limpo= cpf_limpo[0:3]
    return "ALU-"+ str(ano)+ "-"+ cpf_limpo
autor= "Sophia de Jesus"
citacao_formatada= formatar_citacao(autor)
print("Citação Biografia:", citacao_formatada)
matricula= gerar_codigo("2026","456.876.123-00")
print("Matrícula Gerada:", matricula)