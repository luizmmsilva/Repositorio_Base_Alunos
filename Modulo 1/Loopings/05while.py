# Crie um código que faça a conversão de moeda dd real para dólar e vice-versas

# Etapas
# 1) Criar uma variavel chamada de cotação 
# 2) Solicitar ao usuário a opcçao de conversão desejada
# 3) Apresentar o resultado ao usuário se ele deseja continuar a conversão

letra = "s"
while letra == "s":
    cotacao =  float(input("Digite a cotação do dolar USD: "))

    print("-"*50)
    print("-"*15, "Escolha uma Opção","-"*15)
    print("-"*50)

    opcao = int(input("1 - Converter dolar para real | 2 - Converter real para dolar: "))

    if opcao == 1:
        valor = float(input("Digite o valor em dolar a ser convertido para real é R$ "))
        resultado = valor * cotacao
        print(f"O valor em reais é R$ {resultado:.2f}.")
    elif opcao == 2:
        valor = float(input("Digite o valor em real a ser convertida para dolar é USD "))
        resultado = valor / cotacao
        print(f"O valor em dolar é US {resultado:.2f}. ")
    else:
        print("Digite uma opção válida")

    letra = input("Deseja continuar (s/n) ? : ").strip().lower()
