def inicio():
    while True:
        try:
            nome = input("Digite o nome do vendedor: ")
            salario_fixo = float(input("Digite o salário fixo do vendedor: R$ "))
            total_vendas = int(input("Digite o total de vendas efetuadas: "))

            if total_vendas >= 20:
                bonus = salario_fixo * 0.15
                salario_recebido = salario_fixo + bonus
                print(f"\nVendedor: {nome}")
                print(f"Salário fixo: R$ {salario_fixo:.2f}")
                print("Meta atingida!")
                print(f"Bônus de 15%: R$ {bonus:.2f}")
                print(f"Salário final com bônus: R$ {salario_recebido:.2f}")
            else:
                print(f"\nVendedor: {nome}")
                print(f"Salário fixo: R$ {salario_fixo:.2f}")
                print("Meta não atingida.")

        except ValueError:
            print("Erro: digite valores numéricos válidos.\n")

inicio()



