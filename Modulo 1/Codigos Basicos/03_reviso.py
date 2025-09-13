# Crie um programa que forneça nota do aluno
# faça o calculo da nota
# apresente o resultado ao usuário

# Etapas
# 1) Solicitar 3 notas ao aluno 
nome = input("Digite seu nome e série:")
n1 = float(input("Digite a primeira nota:"))
n2 = float(input("Digite a segunda nota:"))
n3 = float(input("Digite a terceira nota:"))
# 2) Calcular a media 
media = (n1 + n2 + n3)/3
# 3) Apresentar o resultado ao usuario
    
if media >= 7:
    print(f"sua média é {media} e você foi aprovado Parabéns")
elif 5 <= media < 7:
    print (f"sua média é média {media} e você está de recuperação")
else:
    print(f"sua média é media {media:.2f} e você infelizmente reprovou!")


 