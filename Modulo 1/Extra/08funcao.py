# crie uma função que calcule o volume de um aquario 
# através de uma função e apresente o resultado 

# Entrada de dados
altura = float(input("Digite a altura (cm): "))
largura = float(input("Digite a largura em (cm): "))
profundidade = float(input("Digite a profundidade em (cm): "))

# Criação da função
def calculator_volume_cm3(altura,largura,profundidade):
    # cálculo do volume do recipiente
    return altura * largura * profundidade

volume_cm3 = calculator_volume_cm3(altura,largura,profundidade)
# variavel volume_cm3
# print () para pular uma linha

print(f"\n as medidas do aquario são: ")
print(f"Altura: {altura} cm")
print(f"Largura: {largura} cm")
print(f"Profundidade: {profundidade} cm ")
print(f"Portanto, seu volume é {volume_cm3:.2f} cm3 ou ({volume_cm3/1000:.2f} Litros.)")

