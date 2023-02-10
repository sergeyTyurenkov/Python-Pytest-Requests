import requests

token = '221153b872e272631456d5541b36c0bb'

response = requests.post('https://pokemonbattle.me:5000/pokemons/kill', headers = {'Content-Type': 'application/json', 'trainer_token': token},
json = {
    "pokemon_id": 5507
    })

print(response.json())