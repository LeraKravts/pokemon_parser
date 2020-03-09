import requests
import os

from parser import get_pokemons
from save import save_pokemons

BASE_URL = 'https://pokemon.fandom.com/ru/wiki/Поколение_I'
PATH_SAVE_DIR = '/Users/valeriya/Desktop/'

resp1 = requests.get(BASE_URL)
resp2 = requests.get(BASE_URL+'I')

if os.path.exists(PATH_SAVE_DIR + 'pokemons.csv'):
    os.remove(PATH_SAVE_DIR + 'pokemons.csv')


save_pokemons(get_pokemons(resp1.text), PATH_SAVE_DIR)
save_pokemons(get_pokemons(resp2.text), PATH_SAVE_DIR)
