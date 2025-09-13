# Crie um program que consulte os preços do produtos 
# e saia do programa quando solicitado pelo usuário

print("Códigos de Produtos")
print("1 - Gin")
print("2 - Doritos")
print("3 - Hambúrguer")
print("4 - Miojo")
print("5 - Perfume")
print("0 - SAIR")

while True:
    try:
        # Solicitar o código do produto ao usuário
        codigo = int(input("Digite o código do produto: "))

        # Usar match-case para mostrar o preço com base  no códgio
        match codigo:
            case 1:
                print("Produto Gin - Preço: R$ 25,00")
            case 2:
                print("Produto Doritos - Preço: R$ 9,50")
            case 3:
                print("Produto Hambúrguer  - Preço: R$ 15,00")
            case 4:
                print("Produto Miojo - Preço: R$ 5,00")
            case 5: 
                print("Produto Perfume - Preço: R$ 25,00")
            case 0:
                print("Saindo do programa........")
                break
            case _:
                print("Código inválido. Por gentileza tente novamente")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

