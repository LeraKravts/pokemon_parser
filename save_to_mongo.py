from pymongo import MongoClient, errors

from parser import get_pokemons, resp1


client = MongoClient('mongodb://localhost:27017/')
client.admin.command('ping')

db = client.pokemons
collection = db.pokemons

posts = get_pokemons(resp1.text)
collection.insert_many(posts)
