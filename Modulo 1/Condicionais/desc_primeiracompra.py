# Crie um programa que pergunte se é a primeira compra do usuário e valor total da compra 
# Se for a primeira commpra e sua compra for maior que 500,00
# Informe que o cliente ganhou um brinde e imprima duma mensagem de boas vindas
# caso contrário imprima uma mensagem de agradecimento

# Etapas
# Pergunte ao usuário se é a primeira compra
primeira_compra =input ("È sua primeira compra conosco? (sim/não): ").strip().lower()

# Pergunte ao ususário o total da compra 
valor_compra = float(input("informe o valor total da sua compra? R$"))

# Verificação da condicional para receber o brinde
if primeira_compra == "sim" and valor_compra > 500:
    print("mgs store agradece sua compra retire seu brinde e volte sempre tamo junto!!!")
else:
    print("obrigado pela sua compra e volte sempre")
