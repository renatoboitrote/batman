def inicio():
    while True:
        try:
            compra = float(input("Digite o valor total da compra: "))
            valor_total = compra / 5
            print(f"O valor de cada parcela foi R$ {valor_total:.2f}\n")
        except ValueError:
            print("Digite um número válido\n")

inicio()

    