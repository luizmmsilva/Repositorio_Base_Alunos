import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

atualizacao = {
    "id":1,
    "tittle":  "Titulo totalmente atualizado com PUT",
    "body":"Agora este post doi substituido por um novo contéudo!",
    "usrId" :1
}

response = requests.put(url,json=atualizacao)