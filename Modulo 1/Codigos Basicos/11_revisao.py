# Desenvolva um algoritmo que receba um número e
# Verifique se ele é positivo, negativo ou zero

# Etapas
# 1) Solicite ao usuário um número
# 2) Verifique se ele é positivo, negativo ou zero
# 3) mostre o resultado ao usuário

numero = float(input("Digite um número:"))
if numero > 0:
    print(f"{numero} é positivo.")
elif numero < 0:
    print(f"{numero} é negativo.")
else:
    print("O número é zero.")


