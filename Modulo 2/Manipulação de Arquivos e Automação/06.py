nome_alvo = input("Nome a editar: ")
novo_email = input("Novo e-mail: ")

with open("pessoa.txt" ,"r") as arquivo:
    linhas = arquivo.readlines()

with open("pessoa.txt" , "w") as arquivo:
    for linha in linhas:
        if nome_alvo in linha:
            nome = linha.split(" | ")[0]
            nova_linha = nome + " | " + novo_email + "\n"
            arquivo.write(nova_linha)
    else:
        arquivo.write(linha)
