opcao = -1

while opcao != 0:
    print("\n--- Conversão de Temperaturas ---")
    print("1 - Celsius para Fahrenheit")
    print("2 - Celsius para Kelvin")
    print("0 - Sair")

    try:
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            temp_celsius = float(input("Digite a temperatura em Celsius: "))
            fahrenheit = (temp_celsius * 9 / 5) + 32
            print(f"O valor em Fahrenheit é: {fahrenheit:.2f}°F")

        elif opcao == 2:
            temp_celsius = float(input("Digite a temperatura em Celsius: "))
            kelvin = temp_celsius + 273.15
            print(f"O valor em Kelvin é: {kelvin:.2f}K")

        elif opcao == 0:
            print("Saindo do programa...")

        else:
            print("Opção inválida!")
            
    except ValueError:
        print("Erro: digite um número válido.")


