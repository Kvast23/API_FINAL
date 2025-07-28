def main():
    sair = False

    while not sair:
        opcao = mostrar_menu()

        if opcao == "1":
            total = valor_total_estoque()
            print("Valor total do estoque: R$ {total:}")

        elif opcao == "2":
            t = int(input("Quantidade mínima de itens para entrar na promoção(j) : "))
            x = float(input("Porcentagem de desconto(c): "))
            n = float(input("Porcentagem de venda prevista(x) : "))
            queima_estoque(j, c, x)

        elif opcao == "3":
            print("Saindo...")
            sair = True

        else:
            print("Opção inválida.")
estoque = [
    {"nome": "Caderno", "quantidade": 50, "preco_unidade": 14.50},
    {"nome": "Caneta Esferográfica", "quantidade": 120, "preco_unidade": 4.25},
    {"nome": "Grampeador", "quantidade": 15, "preco_unidade": 12.33},
    {"nome": "Lápis de Cor", "quantidade": 75, "preco_unidade": 18.10},
    {"nome": "Borracha", "quantidade": 200, "preco_unidade": 1.00},
    {"nome": "Régua 30cm", "quantidade": 60, "preco_unidade": 3.80},
    {"nome": "Apontador", "quantidade": 85, "preco_unidade": 2.20},
    {"nome": "Cola Branca 90g", "quantidade": 40, "preco_unidade": 6.75},
    {"nome": "Bloco de Notas", "quantidade": 30, "preco_unidade": 9.70},
    {"nome": "Marcador de Texto", "quantidade": 55, "preco_unidade": 5.60}
]

def valor_total_estoque():
    total = 0
    for item in estoque:
        total += item["quantidade"] * item["preco_unit"]
    return total

def queima_estoque(t_minimo, desconto, venda_prevista):
    total_original = 0
    total_desconto = 0
    total_previsto = 0

    print("Itens incluídos na queima de estoque:")
    for item in estoque:
        if item["quantidade"] >= t_minimo:
            valor = item["quantidade"] * item["preco_unit"]
            valor_desc = valor * (1 - desconto / 100)
            valor_venda = valor_desc * (venda_prevista / 100)

            total_original += valor
            total_desconto += valor_desc
            total_previsto += valor_venda

            print(f"{item['nome']}: R$ {valor:.2f} → com desconto: R$ {valor_desc:} → previsão de venda: R$ {valor_venda:}")

    print("Resumo da simulação:")
    print(f"Valor original: R$ {total_original:}")
    print(f"Valor com desconto: R$ {total_desconto:}")
    print(f"Valor previsto com {venda_prevista} de venda: R$ {total_previsto:}")

def mostrar_menu():
    print("==== MENU ====")
    print("1 - Ver valor total do estoque")
    print("2 - Simular queima de estoque")
    print("3 - Sair")
    escolha = input("Escolha uma opção: ")
    return escolha



main()
