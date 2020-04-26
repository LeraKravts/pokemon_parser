from pymongo import MongoClient, errors

from engine import get_pokemons, resp1


client = MongoClient('mongodb://localhost:27017/')
client.admin.command('ping')

db = client.pokemons
collection = db.pokemons

posts = get_pokemons(resp1.text)
collection.insert_many(posts)


def main():
    """Data is already loaded to Mongo"""
    pass


if __name__ == '__main__':
    pass
