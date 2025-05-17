altura = float(input("Digite sua altura (em metros): "))
peso = float(input("Digite seu peso (em kg): "))

imc = peso / (altura * altura)
print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 24.9:
    print("Peso normal")
elif 25.0 <= imc < 29.9:
    print("Sobrepeso")
else:1.68
print("Obesidade")