# Crie um programa que verifique a idade permitida para votar

# Etapas 
# 1)  Solicite a idade
# 2) verifique se pode votar

idade = int(input("Digite sua idade: "))
if idade < 16:
    print("Você não tem idade para votar")
elif (idade >= 16 and idade < 18) or (idade >70):
    print("Você pode votar, porém o voto é facultativo.")
else:
    print("Você pode votar e o voto é obrigatório")