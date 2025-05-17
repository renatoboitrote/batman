opcao = -1

while opcao != 0:
    print("\n=== Locadora de Carros ===")
    print("1 - Ver Tabela de Preços")
    print("2 - Calcular valor do aluguel")
    print("0 - Sair")

    try:
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            print("\n--- Tabela de Preços ---")
            print("R$ 90,00 por dia alugado")
            print("R$ 0,20 por Km rodado")

        elif opcao == 2:
            dias = int(input("Digite a quantidade de dias que o carro foi alugado: "))
            kms = float(input("Digite a quantidade de Km percorridos: "))

            preco_dias = dias * 90
            preco_kms = kms * 0.20
            total = preco_dias + preco_kms

            print("\n--- Recibo ---")
            print(f"Dias alugados: {dias} x R$ 90,00 = R$ {preco_dias:.2f}")
            print(f"Km percorridos: {kms:.2f} x R$ 0,20 = R$ {preco_kms:.2f}")
            print("----------------------------")
            print(f"Total a pagar: R$ {total:.2f}")

        elif opcao == 0:
            print("Encerrando o programa.")

        else:
            print("Opção inválida! Tente novamente.")

    except ValueError:
        print("1digite um número válido.")