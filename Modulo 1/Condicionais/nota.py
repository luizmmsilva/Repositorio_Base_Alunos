# Crie um programa  que solicite a nota do aluno e informe o conceito recebido

# Etapas 
# 1) Criar uma variavel que irá armazenar a nota
nota = float(input( "DIgite sua nota: "))
# 2) Verificar a condiconal
# 3) Apresentar o resultado para o usuário
if nota >= 9:
    print ( "Conceito A- Excelente")
elif nota >= 8:
    print ("Conceito B- Muito Bom")
elif nota >= 7:
    print ( "Conceito C- Bom")
elif nota >= 6:
    print( "Conceito D- Regular")
else:
    print ("Conceito E- Insuficiente")

