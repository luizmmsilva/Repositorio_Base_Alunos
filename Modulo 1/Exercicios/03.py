# LER E MOSTRAR TODO O CONTEUDO DO ARQWUIVO
with open("pessoa.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)