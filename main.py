import uvicorn
from fastapi import FastAPI
from models_1 import Pokemon, pokemons
from fastapi import HTTPException, status
from fastapi.responses import PlainTextResponse

app = FastAPI()

# vai no endpoint pokemons e retorna a lista de pokemons que vem do models_1
@app.get('/pokemons')
async def get_pokemons():
    return pokemons

# vai no endpoint pokemons e retorna o item na posição id
@app.get('/pokemons/{id}', response_class=PlainTextResponse)
async def get_pokemon(id: int):
    for item in pokemons:
        if item.id == id:
            return f"Nome: {item.name}\nAtaque especial: {item.special_at}"
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id de pokémon inválido")
        


@app.put('/pokemons/{id}')
async def update_pokemon(id: int, pokemon: Pokemon):
    for index, item in enumerate(pokemons):
        if item.id == id:
            pokemon.id = id
            pokemons[index] = pokemon
            return pokemon

@app.post('/pokemons')
async def adiciona_pokemon(pokemon: Pokemon):
    lista_ids = []
    for item in pokemons:
        lista_ids.append(item.id)
    novo_id = max(lista_ids) + 1
    pokemon.id = novo_id
    pokemons.append(pokemon)
    return pokemons

@app.delete('/pokemons/{id}')
async def deleta_pokemon(id: int):
    for index, item in enumerate(pokemons):
        if item.id == id:
            pokemons.remove(pokemons[index])
            return pokemons
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Esse pokemon não está na lista.")

if __name__ == "__main__":
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)