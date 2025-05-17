frances = integral = doce_liso = doce_farofa = forma = numero = 0
valor_frances = valor_integral = valor_doce_liso = valor_doce_farofa = valor_forma = 0.0

while numero !=6:
    print("------------PADARIA------------")
    print("[1] Pão Francês")
    print("[2] Pão Integral")
    print("[3] Pão Doce Liso")
    print("[4] Pão Doce Farofa")
    print("[5] Pão de Forma")
    print("[6] Fim da compra")
    print("-------------------------------")
    opcao = int(input("Escolha sua opção: "))

    if opcao == 1:
        frances = int(input("Digite a quantidade de pão francês que você quer: "))
        valor_frances = frances * 1.04
    elif opcao == 2:
        integral = int(input("Digite a quantidade de pão integral que você quer: "))
        valor_integral = integral * 1.04
    elif opcao == 3:
        doce_liso = int(input("Digite a quantidade de pão doce liso que você quer: "))
        valor_doce_liso = doce_liso * 1.08
    elif opcao == 4:
        doce_farofa = int(input("Digite a quantidade de pão doce farofa que você quer: "))
        valor_doce_farofa = doce_farofa * 1.11
    elif opcao == 5:
        forma = int(input("Digite a quantidade de pão de forma que você quer: "))
        valor_forma = forma * 0.95
    elif opcao == 6:
        print("SAINDO..")
        break

print("\n----------- RECIBO -----------")
total = valor_frances + valor_integral + valor_doce_liso + valor_doce_farofa + valor_forma
if frances > 0:
    print(f"Pão Francês: {frances} unidade(s) - R$ {valor_frances:.2f}")
if integral > 0:
    print(f"Pão Integral: {integral} unidade(s) - R$ {valor_integral:.2f}")
if doce_liso > 0:
    print(f"Pão Doce Liso: {doce_liso} unidade(s) - R$ {valor_doce_liso:.2f}")
if doce_farofa > 0:
    print(f"Pão Doce Farofa: {doce_farofa} unidade(s) - R$ {valor_doce_farofa:.2f}")
if forma > 0:
    print(f"Pão de Forma: {forma} unidade(s) - R$ {valor_forma:.2f}")
print("-------------------------------")
print(f"TOTAL A PAGAR: R$ {total:.2f}")