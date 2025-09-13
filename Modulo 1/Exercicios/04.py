# LER LINHA POR LINHA E MOSTRAR COMO LISTA
with open("pessoa.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        print(linha.strip())