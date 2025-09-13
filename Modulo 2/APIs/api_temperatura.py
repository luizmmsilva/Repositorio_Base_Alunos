# 1 Definir chave de API e o linn de requisição 

import requests
api_key = '2a1ac38a32354cb7b19133643251408'
cidade = input('Digite o nome da cidade: ').strip()
url= f'https://api.weatherapi.com/v1/current.json'

# 25. Paramêtros da requisição 
parametros = {
    'key':api_key,
    'q': cidade,
    'lang':'pt'# define a língua da resposta como português
}
# # Fazer a requisição
resposta = requests.get(url, params=parametros)

# 4 Verificar se a requisiãção foi bem sucedida
if resposta.status_code == 200:
    dados = resposta.json() # convertendo a resposta JSON em um dicionario Python
    temperatura = dados['current']['temp_c']
    descricao = dados['current']['condition']['text']
    print(f'Temperatura na cidade {cidade} é {temperatura}°C.')
    print(f'Descrição: {descricao}')
else:
    print(f'Erro na requisição: {resposta.status_code}')
    print(resposta.content)