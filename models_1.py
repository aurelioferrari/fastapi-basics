from typing import Optional

from pydantic import BaseModel

class Pokemon(BaseModel):
    id: Optional[int] = None,
    name: str
    special_at: str



pokemons = [
    Pokemon(id=1, name="Charmander", special_at="Fireball"),
    Pokemon(id=2, name="Chameleon", special_at="Super Fireball")
]

