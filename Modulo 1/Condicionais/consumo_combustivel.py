# Crie um programa que verifique o desempenho de um carro
# Solicite ao usuário a distância percorrida, a quantidade de combustível gasta
# Calcule o consumo médio e informe o desempenho do veículo

distancia_percorrida = float(input("Digite a distância percorrida em KM: "))
combustivel_gasto = float(input(" Digite a quantidade de combustível gasto em litros: "))

# Calculo do consumo médio
consumo_medio = distancia_percorrida/combustivel_gasto

# Classificação do consumo
match consumo_medio:
    case valor if valor < 8:
        print("Consumo menor que 8Km/L -  Desempenho ruim. ")
    case valor if valor < 12:
        print("Consumo menor que 12Km/L -  Desempenho médio. ")
    case _:
        print("Consumo maior ou igual a 12Km/L -  Otimo desempenho. ")