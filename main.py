import requests


token = 'c1e184f84554fb57e6506a15892b8c13'
base_url = 'https://pokemonbattle.me:9104/'

response_add_pokemon = requests.post(f'{base_url}pokemons', headers={"trainer_token" : token}, json={
    "name": "Турбозавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
})
print(response_add_pokemon.text)





import requests
token = 'c1e184f84554fb57e6506a15892b8c13'
base_url = 'https://pokemonbattle.me:9104/'
response_add_pokeball = requests.post(f'{base_url}trainers/add_pokeball', headers={"trainer_token" : token}, json={
    "pokemon_id": "9323"
})
print(response_add_pokeball.text)




import requests
token = 'c1e184f84554fb57e6506a15892b8c13'
base_url = 'https://pokemonbattle.me:9104/'
response = requests.put(f'{base_url}pokemons', headers={"trainer_token" : token}, json={
    "pokemon_id": "9323",
    "name": "Турбозавр111",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"

})
print(response.text)
