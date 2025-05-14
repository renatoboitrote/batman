def inicio():
    numero_secreto = 7
    tentativa = 0
    contagem_tentativas = 0

    print("**** Jogo de Adivinhação ****")
    print("\nTente adivinhar o número secreto de 1 a 10.")

    while tentativa != numero_secreto:
        tentativa = int(input("\nDigite sua tentativa: "))
        contagem_tentativas += 1

        if tentativa != numero_secreto:
            print("Você errou, tente novamente.")
        else:
            print("\nVocê acertou, parabéns!")
            print("Foram feitas", contagem_tentativas, "tentativas.")

# Inicia o programa
inicio()
