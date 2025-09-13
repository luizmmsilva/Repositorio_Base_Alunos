# Mètodo PATCH (atualização parcial)

import requests
url = "https://jsonplaceholder.typicode.com/posts/7"

atualizacao = {
    "tittle":"Título atualizado no exercíco"
}

#Criando a requisição 
response = requests.patch(url, json=atualizacao)

print("Status codae:",response.status_code)
print("Resposta da Api:", response.json())