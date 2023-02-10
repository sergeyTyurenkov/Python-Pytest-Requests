import requests
import json

token = '221153b872e272631456d5541b36c0bb'

response = requests.post('https://pokemonbattle.me:5000/pokemons', headers = {'Content-Type': 'application/json', 'trainer_token': token},
json = {
    "name": "Domesty",
    })

pokemon_id = response.json()['id']

response_change = requests.put('https://pokemonbattle.me:5000/pokemons', headers = {'Content-Type': 'application/json', 'trainer_token': token},
json = {
    "pokemon_id": pokemon_id,
    "name": "Somestry"
    })

response_catch = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball', headers = {'Content-Type': 'application/json', 'trainer_token': token},
json = {
    "pokemon_id": pokemon_id,
    })

print(response.json())
print(response_change.json())
print(response_catch.json())