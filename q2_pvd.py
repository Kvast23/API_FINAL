def main():
    itens = []
    sair = 0

    while  == 0:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do Produto: ")
            categoria = input("Categoria (Eletrônicos, Alimentos, Vestuário): ")
            valor = float(input("Valor unitário: "))
            quantidade = int(input("Quantidade: "))

            total_item = calcular_valor_total_item(valor, quantidade)

            item = {
                "nome": nome,
                "categoria": categoria,
                "valor_unitario": valor,
                "quantidade": quantidade,
                "total_item": total_item
            }

            itens.append(item)
            print("Item adicionado com sucesso.")

        elif opcao == '2':
            total_geral = 0
            i = 0
            while i != contar_itens(itens):
                total_geral = total_geral + itens[i]["total_item"]
                i = i + 1

            print(f"Total da compra: R$ {total_geral:.2f}")
            pagamento = input("Forma de pagamento (PIX, Débito, Crédito): ")

            total_com_desconto = colocar_desconto(total_geral, pagamento)
            print(f"Total com desconto: R$ {total_com_desconto:.2f}")

            if pagamento == 'Crédito':
                opcoes_parcelas = calcular_parcelas(total_com_desconto)
                if contar_itens(opcoes_parcelas) != 0:
                    print("Opções de parcelamento:")
                    j = 0
                    while j != contar_itens(opcoes_parcelas):
                        qtd = opcoes_parcelas[j]
                        valor_parcela = total_com_desconto / qtd
                        print(str(qtd) + "x de R$ " + str(round(valor_parcela, 2)))
                        j = j + 1
                    parcelas = int(input("Escolha a quantidade de parcelas: "))
                    print("Você escolheu parcelar em " + str(parcelas) + "x de R$ " + str(round(total_com_desconto / parcelas, 2)))
                else:
                    print("Valor muito alto para parcelamento. Pagamento à vista.")

            print("Compra finalizada.")
            sair = 1

        elif opcao == '3':
            print("Encerrando o sistema.")
            sair = 1

        else:
            print("Opção não aceita.")
