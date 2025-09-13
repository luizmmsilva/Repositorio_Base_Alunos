# Método GET utilizando  uma api de teste
# Esse métdo busca (get) alguma informaçã/coisa

import requests
url = 'https://jsonplaceholder.typicode.com/posts/5'
response = requests.get(url)

print("Status:", response.status_code)
print("Titulo do post:" ,response.json()['title'])
