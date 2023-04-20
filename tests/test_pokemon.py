import requests 
import pytest

def test_status_code():
    response = requests.get('https://pokemonbattle.me:9104/trainers')
    assert response.status_code == 200



def test_piece_body():
    response = requests.get('https://pokemonbattle.me:9104/trainers', params={'trainer_id' : 4050})
    assert response.json()['trainer_name'] == 'Турбозавр'     
    
 
@pytest.mark.parametrize('key, value', [('trainer_name', 'Турбозавр')])  
 
def test_piece_body(key, value):
    response = requests.get('https://pokemonbattle.me:9104/trainers', params = {'trainer_id' : 4050})    
    assert response.json()[key] == value                  