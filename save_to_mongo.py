from pymongo import MongoClient, errors

from engine import get_pokemons, resp1


client = MongoClient('mongodb://localhost:27017/')
client.admin.command('ping')


def save_to_mongo():
    db = client.pokemons
    collection = db.pokemons
    posts = get_pokemons(resp1.text)
    collection.insert_many(posts)


def main():
    pass


if __name__ == '__main__':
    main()
