def main():
    print("=== Jogo: Qual é a Palavra? ===")
    palavra = input("Digite a palavra secreta (oculta do jogador): ").upper()
    print("\n" * 50)  # Simula esconder a palavra
    jogar(palavra)
def mostrar_letras(palavra, letras_descobertas):
    resultado = ""
    for letra in palavra:
        achou = False
        for l in letras_descobertas:
            if l == letra:
                achou = True
                break
        if achou:
            resultado += letra
        else:
            resultado += "_"
    return resultado

def verificar_todas_descobertas(palavra, letras_descobertas):
    for letra in palavra:
        achou = False
        for l in letras_descobertas:
            if l == letra:
                achou = True
                break
        if not achou:
            return False
    return True

def jogar(palavra):
    letras_descobertas = []
    tentativas_chute = 3
    pontuacao = 100

    for rodada in range(10):
        print("Palavra:", mostrar_letras(palavra, letras_descobertas))
        print("1 - Perguntar letra (-10 pontos)\n2 - Chutar palavra (-20 pontos por erro)")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            letra = input("Digite uma letra: ").upper()
            letra_na_palavra = False
            for l in palavra:
                if l == letra:
                    letra_na_palavra = True
                    break
            if letra_na_palavra:
                letras_descobertas.append(letra)
                print("Letra correta!")
            else:
                pontuacao -= 10
                print("Letra errada! -10 pontos")

        elif opcao == "2":
            if tentativas_chute == 0:
                print("Você usou todos os seus chutes.")
                continue

            chute = input("Digite seu chute: ")()
            if chute == palavra:
                print("Parabéns! Você acertou.")
                print("Pontuação final:", pontuacao)
                return
            else:
                tentativas_chute -= 1
                pontuacao -= 20
                print("Errou o Chute ! Tentativas restantes:", tentativas_chute)

        if verificar_todas_descobertas(palavra, letras_descobertas):
            print("Parabéns! Você acertou todas as letras.Desite da escola vira jogador")
            print("Pontuação final:", pontuacao)
            return

    print("Fim do jogo. A palavra era:", palavra)
    print("Pontuação final:", pontuacao)

