 # Crie uma programa que indique a temperatura 

temperatura = float(input("Digite a temperatqura em Celsius:"))

if temperatura >= 30:
    print("Está quente!")
elif temperatura >= 22:
    print("Está agrádavel")
elif temperatura >= 10:
    print("Está frio!")
else:
    print("Está muito frio")