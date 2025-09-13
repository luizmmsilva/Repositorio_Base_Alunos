# Crie um programa que receba dois números e exiba
# Resultado da soma, subtracao, multiplicacao e divisao entre eles

#etapas
# 1) Solicitar ao usuário 2 numeros
n1 = float(input("Digite o primeiro numero"))
n2 = float(input("Digite o segundo numero"))
# 2) Criar as variaveis que receberão os resultados das operções
soma = n1 +n2
subtracao = n1- n2
multiplicacao = n1 * n2
divisao = n1/n2

# 3) Apresentar o resultado ao usuário
print(f"soma: {soma}")
print(f"subtracao: {subtracao}")
print(f"multiplicacao: {multiplicacao}")

if n2 != 0:
    divisao = n1/n2
    print(f"Divisão:{divisao:.2f}")
else:
    print("Não Existe divisão referente á numero negativo")



