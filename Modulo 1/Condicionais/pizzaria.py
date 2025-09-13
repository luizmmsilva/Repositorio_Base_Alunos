print("Menu da Pizzaria")
print("1 - Franbacon")
print("2 - Calabresa")
print("3 - Americana")
print("4 - Mexicana")
print("5 - 4 Queijos")
print("0 - SAIR, volte sempre")

while True:
    try:
        # Solicitar o código do produto ao usuário
        codigo = int(input("Digite o código da pizza desejada: "))

        # Usar match-case para mostrar o preço com base  no códgio
        match codigo:
            case 1:
                print("Pizza Franbacon - Preço: R$ 40,00")
            case 2:
                print("Pizza Calabresa - Preço: R$ 42,00")
            case 3:
                print("Pizza Americana  - Preço: R$ 39,00")
            case 4:
                print("Pizza Mexicana - Preço: R$ 43,00")
            case 5: 
                print("Pizza 4 Queijos - Preço: R$ 45,50")
            case 0:
                print("Saindo, volte sempre........")
                break
            case _:
                print("Código inválido. Por gentileza tente novamente")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
