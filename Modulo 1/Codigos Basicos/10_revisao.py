 # Crie um programa que solicite um número inteiro e calcule e 
 # Exiba a sua raiz quadrada e também se é divisível pelo números de 2 a 9

numero = int(input("Digite um número inteiro positivo: "))
# Etapas
# 1) Solicite um número ao usuário
# 2) Exiba a sua raiz quadrada e também se é divisível pelo números de 2 a 9
# 3) mostre o resultado



# Calculando a raiz quadra
raiz = numero ** 0.5
print(f"A raiz quadrada de {numero} é:{raiz:.2f}")

# Verficando se é divisel pelos números de 2 a 9
print(f"Divisibilidade de {numero}:")
for divisor in range (2,10):
    if numero % divisor == 0:
        print(f"{numero} é divisível por {divisor}")
    else:
        print(f"{numero} não é divisível por {divisor}")