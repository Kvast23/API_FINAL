def main():
    print("=== Avaliação de Risco de Crédito ===")
    renda = input("Renda mensal (em R$): ")
    score = input("Histórico de crédito (0 a 1000): ")
    risco = classificar_risco_credito(renda, score)
    print("Resultado:", risco)

def classificar_risco_credito(renda_mensal, historico_credito_score):
    try:
        renda_mensal = float(renda_mensal)
        historico_credito_score = int(historico_credito_score)
    except:
        return "Dados inválidos"

    if historico_credito_score >= 800 and renda_mensal >= 5000:
        return "Risco Muito Baixo"
    elif historico_credito_score >= 700 and renda_mensal >= 3000:
        return "Risco Baixo"
    elif (500 <= historico_credito_score <= 699 and renda_mensal >= 2000) or renda_mensal >= 4000:
        return "Risco Moderado"
    elif 300 <= historico_credito_score <= 499 or (1000 <= renda_mensal <= 1999):
        return "Risco Alto"
    else:
        return "Risco Muito Alto"

