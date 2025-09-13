# Crie um programa utilizando o while
# calcule a porcentagem de um número

letra = "s"

while letra == "s":
    n1 = float(input("Digite um numero: "))
    n2 = float(input("Digite a porcentagem que deseja descobrir: "))
    # cálculo da porcentagem
    porcentagem = (n1*n2)/100
    #apresenta o resultado
    print(f"{n2} % do numero {n2} é igual a {porcentagem}.")
    # condição para o código repetir ou não (sair do loop)
    letra = input("Deseja continuar (s/n): "). strip().lower()