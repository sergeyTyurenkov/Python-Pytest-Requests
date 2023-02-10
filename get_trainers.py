import requests

token = '221153b872e272631456d5541b36c0bb'

response = requests.get('https://pokemonbattle.me:5000/trainers', params = {'trainer_id': '2151'})

print(response.json())