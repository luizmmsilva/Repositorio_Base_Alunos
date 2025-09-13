nome = input("Digite seu nome: ")
email = input("Digite o seu e-mail: ")

with open("pessoa.txt", "a") as arquivo:
    arquivo.write(nome + " | "+ email + "\n")
