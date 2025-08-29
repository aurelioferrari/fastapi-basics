Pokémon API

A RESTful API built with FastAPI to manage a Pokémon list. It allows you to list, add, update, retrieve, and delete Pokémon.

🚀 Technologies Used

FastAPI

Uvicorn

📌 Features

GET /pokemons – Returns the list of all registered Pokémon.

GET /pokemons/{id} – Retrieves details of a specific Pokémon by its ID.

POST /pokemons – Adds a new Pokémon to the list.

PUT /pokemons/{id} – Updates an existing Pokémon.

DELETE /pokemons/{id} – Deletes a Pokémon from the list by its ID.

🛠 How to Run

Clone this repository:

git clone https://github.com/your-username/your-repository.git
cd your-repository


Install dependencies:

pip install fastapi uvicorn


Start the server:

uvicorn main:app --reload


Access the interactive documentation:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

🧩 Project Structure
.
├── main.py              # Main API code
├── models_1.py          # Pokémon model and initial list

📄 Example Request

POST /pokemons

{
  "name": "Charmander",
  "special_at": "Flamethrower"
}


Response:

[
  {
    "id": 1,
    "name": "Pikachu",
    "special_at": "Thunder Shock"
  },
  {
    "id": 2,
    "name": "Charmander",
    "special_at": "Flamethrower"
  }
]

⚠ Error Handling

Returns 404 Not Found when a Pokémon ID is invalid.

Provides clear messages when trying to delete or fetch a non-existing Pokémon.
