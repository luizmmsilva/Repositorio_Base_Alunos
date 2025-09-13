# Abrir e ler o arquivo

arquivo =  open('hello.txt','r', encoding='utf-8') # abrindo arquivo
conteudo = arquivo.read() # lendo o arquivo
print(conteudo)
arquivo.close()

# Retorna o tamanho do arquivo wm bytes

import os 
print(os.path.getsize('hello.txt'), "bytes")

# Listar todos os arquivos e pastas de um diretorio
#não iremos importar a biblioteca os por que já fizemos isso nesse script(arquivo)
print(os.listdir(".")) # lista todo o conteudo da pasta atual

# Separar os diretoris
# não iremos importar a biblioteca os por que já fizemos isso nesse script(arquivo)
caminho = "/home/user/documentos/arquivo.txt"
print(os.path.dirname(caminho)) # home/user/documentos
print(os.path.basename(caminho)) #arquivo .txt