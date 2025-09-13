# Crie um programa que verifique infraçoes de trânsitos:  rodízio e velocidade

# Pergunte se hoje é rodízio do carro
rodizio = input ("Hoje é o dia do rodìzio deste carro? (sim/não):"). strip() .lower()

# Pergunte a velocidade do carro 
velocidade = float(input("Qual a velocidade atual do veículo (Km/h)? : "))

# Derfina o limite da via
limite_velocidade = 60

# Verificar as infrações 
if rodizio == "sim" and velocidade > limite_velocidade:
    print("Você está dirigindo no seu dia de rodízio e acima da velociade permitida.\n ")
    print( "Você será atuado  por ambas infrações.")
elif rodizio == "não" and velocidade > limite_velocidade:
    print("Você está dirigindoa acima da velocidade será autuado")
elif rodizio == "sim":
    print("Você está dirigindo acima da velociade permitida e será atuado por excesso de velocidade")
elif velocidade > limite_velocidade:
    print("Você está dirigindo acim da velocdidade permitida e será atuado por excesso de velocidade") 
else :
    print("Tudo certo! você esta dentro da lei. Dirija com Segurança")

          