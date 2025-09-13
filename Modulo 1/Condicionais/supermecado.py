# Crie um programa que  contabilize os produtos comprados e informe o valor total da compra

# Criado das variaveis
valor_total_compra = 0 
valor_nescau =  10.50
valor_cocacola = 5.00
valor_doritos = 7.50

# Solicitar o código do produto
produto = input("Digite o nome do produto (nescau cocacola ou doritos)").strip().lower()

# Verificação
if produto == "nescau":
    valor_total_compra += valor_nescau
elif produto == "cocacola":
    valor_total_compra += valor_cocacola
elif produto == "doritos":
     valor_total_compra += valor_doritos
else:
    print("Produto não reconhecido. ")
    valor_total_compra = 0

# Exibição valor final
if valor_total_compra > 0:
    print(f"o valor total da compra é: R$ {valor_total_compra: 2f}")






