soma = 0
numero = 1
while numero !=0:
    numero = int(input("Digite um número (digite 0 para sair)"))
    soma = soma+numero
    if numero !=0:
        print (f"A soma até o momento é {soma}")
print (f"A soma dos numeros digitados é {soma}")
