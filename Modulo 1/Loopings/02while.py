# Crie um program que soma a média do aluno usando letra 

letra = "s"

while letra == "s":
    #solicite ao usuário nome e 3 notas
    nome = input("Digite seu Nome:")
    n1 = float(input("Digite a primeira nota:"))
    n2 = float(input("Digite a segunda nota:"))
    n3 = float(input("Digite a terceira nota:"))

    # realizar calculo da media 
    soma = n1 + n2 + n3 # calculo da soma
    media = soma / 3 # calculo da média
    # outra maneira de escrever a média =(n1+n2+n3)

    print(f"A média do aluno(a) {nome} é {round(media)}.") # esse print apresenta o nome do aluno e a média
    # essa condicional analisa a média e informa o status dele
if media >= 7:
    print (f"status aprovado, media {media:.2f}")
elif media >= 5:
    print (f"status recuperação, media {media:.2f}")
else: 
    print (f"status reprovado, media {media:.2f}")

letra = input("Deseja continuar? (s/n): ").strip().lower() # regra para o sistema repetir o código ou parar
