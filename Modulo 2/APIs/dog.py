# Api que apresenta imagens aleatorias de cachorro

import requests
url = 'https://dog.ceo/api/breeds/image/random'

response = requests.get(url)

print("Link de imagem: ", response.json()['message'])