# Crie um programa que solicite 3 notas do aluno
# faça o calculo da media
# e informe se o aluno está aprovado(>=7), de recuperação (>5) ou reprovado 

# Etapas
# 1) Solicitar 3 notas para o aluno
nome = input("Digite seu nome: ")
nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
nota3 = float(input("digite a terceira nota: "))
# 2) somar as notas
soma= nota1 + nota2 + nota3
# 3) fazer o calculo da média
media= soma/ 3
# 4) fazer a verficação das notas
if  media>= 7:
    print (f"status aprovado, media {media:.2f}")
elif media >= 4:
    print (f"status recuperação, media {media:.2f}")
else: 
    print (f"status reprovado, media {media:.2f}")


# 5) informar a média e o status do aluno
