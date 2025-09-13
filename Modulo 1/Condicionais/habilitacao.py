# Crie um programa que peça o nome do usuário, idade e pergunte se ele possui habilitação

# criação das variaveis 
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
possui_habilitacao = input("Possui habilitação?\n (1-sim/2-nâo):")

# Verificação
if idade >= 18:
    if possui_habilitacao == "1":
        print("Pode dirigir. ")
    else:
        print("Não pode dirigir. ")
else:
    print("Menor de idade.")

print("Final de programa, Obrigado!")
