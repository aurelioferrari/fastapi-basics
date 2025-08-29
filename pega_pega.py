import requests
from models_1 import pokemons

url = 'http://localhost:8000/pokemons'
url_put = 'http://localhost:8000/pokemons/1'

dado = {
    "name": "Teste 2",
    "special_at": "Teste de fogo 2"
}

dado_delete = {
    "id": 1

}


# resposta = requests.get(url)
# resposta_put = requests.put(url_put, json=dado)
# resposta_delete = requests.delete(url_put)
resposta_post = requests.post(url, json=dado)

# print(resposta.json())
# print(resposta_put.json())
print(pokemons)