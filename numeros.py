def inicio():
    ano_atual = 2025  # Ano fixo para a verificação

    ano_nascimento = int(input("Digite o seu ano de nascimento: "))
    idade = ano_atual - ano_nascimento

    print(f"Você tem {idade} anos.\n")

    if idade < 16:
        print("Você NÃO é elegível para votar.\n")
    elif (16 <= idade <= 17) or (idade > 70):
        print("Seu voto é FACULTATIVO.\n")
    else:  # idade entre 18 e 70 inclusive
        print("Seu voto é OBRIGATÓRIO.\n")

# Executa o programa
inicio()
