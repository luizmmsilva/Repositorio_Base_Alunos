import requests

print("Bem- vindo ao BUSQUE SEU CEP")

cep = input("Digite seu CEP (Somente números): ")

url = f'https://viacep.com.br/ws/{cep}/json/'

resposta = requests.get(url) # AQUI ESTAMOS FAZENDO REQUISIÇÃO

if resposta.status_code == 200:
    dados = resposta.json()
    if 'erro' not in dados:
        print(f'CEP: {dados['cep']}')
        print(f'Logradouro: {dados['logradouro']}')
        print(f'Bairro: {dados['bairro']}')
        print(f'Cidade: {dados['localidade']}')
        print(f'Estado: {dados['uf']}')
    else:
        print('CEP não foi encontrado')
else:
    print(f'Erro na requisição: {resposta.status_code}')
    print(resposta.content)

