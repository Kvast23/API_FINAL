def main():
    print("=== Avaliação de Risco de Crédito ===")
    renda = input("Renda mensal (em R$): ")
    score = input("Histórico de crédito (0 a 1000): ")
    risco = classificao_risco_credito(renda, score)
    print("Resultado:", risco)

def classificao_risco_credito(renda_mensal, score_credito):
    try:
        renda_mensal = float(renda_mensal)
         score_credito = int(score_credito)
    except:
        return "Dados não aceitos"

    if score_credito >= 800 and renda_mensal >= 5000:
        return "Risco Muito Baixo"
    elif score_credito >= 700 and renda_mensal >= 3000:
        return "Baixo Risco "
    elif (500 <= score_credito <= 699 and renda_mensal >= 2000) or renda_mensal >= 4000:
        return "Risco Moderado"
    elif 300 <= score_credito <= 499 or (1000 <= renda_mensal <= 1999):
        return " Alto Risco"
    else:
        return "Risco Muito Alto"

