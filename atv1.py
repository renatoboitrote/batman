def inicio():
    km = int(input("Digite os km consumidos: "))
    litros = int(input("Digite os litros consumidos: "))
    consumo = km / litros
    print(f"O valor foi de {consumo:.2f} km/l")
inicio()
