from pymongo import MongoClient, errors
import pandas as pd


client = MongoClient('mongodb://localhost:27017/')
client.admin.command('ping')

table = pd.read_csv('pokemons.csv')
table.columns = ['Russian','Type1','Type2','English','Japan', 'Url']
print(table.head())

pokemons_db = client.pokemons
