# Crie um programa para verificar se uma pessoa pode dirgir 

# Etapas 
# 1) Solicite o nome e idade 
# 2) Apresente o resdultado e status ao usuário

nome= input("Digite seu nome:")
idade = int(input("Digite sua Idade:"))

if idade >= 18:
    print("Você não pode dirigir")  
else:
    print("Fora da lei")


