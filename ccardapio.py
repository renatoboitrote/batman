opcao = 0
while opcao !=5:
    
    print("------CARDÁPIO------")
    print("1-Hamburguer")
    print("2-Pizza")
    print("3-Salada") 
    print("4-Refrigerante")
    print("5-Sair")
    
    opcao = int(input("Escolha uma opção do menu:"))
    if opcao == 1:
        print("Você escolheu o hambúrguer")
    elif opcao == 2:
        print("Você escolheu a pizza")
    elif opcao == 3:
        print("Você escolheu a salada")
    elif opcao == 4:
        print("Você escolheu a refrigetante")
    elif opcao == 5:
        print("Saindo do cardápio...")
        break