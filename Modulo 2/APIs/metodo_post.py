# Método post (adicionar/criar)

import requests
url = "https://jsonplaceholder.typicode.com/posts"

novo_post = {
    "tittle":"Meu primeiro POST",
    "body":"Estou aprendendo a enviar dados com Phyton",
    "userId": 10
}
# Criando a requisição
response = requests.post(url, json=novo_post)

print("Status Code: ", response.status_code)
print("Resposta da API:", response.json())
