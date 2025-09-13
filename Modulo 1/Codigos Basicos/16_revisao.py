# Crie um programa que receba uma temperatura 
# em Celsius e a converta para Fahrenheit (F = C * 9/5 + 32)
# ou vice-versa, dependendo da escolha do usuário

escolha = input("Digite 'C' para converter de Fahrenheit para Celsius ou 'F' para converter de Celsius para Fahrenheit:").upper()

if escolha == 'C': # executa esse trecho se a pessoa escolheu C
    temp = float(input("DIgite a temperatura em Fahrenheit: "))
    resultado = (temp - 32 ) * 5/9
    print(f"{temp} °F equivale a {resultado:.1f}°C")
elif escolha == 'F': # executa esse trecho se a pessoa escolheu F
    temp = float(input("Digite a temperatura em Celsius: "))
    resultado = temp * 9/5 + 32
    print(f"{temp} °C equivale a {resultado:.1f} °F")
else: # executa esse trecho se a pessoa digitou errado 
    print("Opção inválida")