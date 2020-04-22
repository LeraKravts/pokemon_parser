import sys
import psycopg2
from psycopg2.extras import execute_values
import pokemon



create_query = """
CREATE TABLE public.HS_Pokemon
(
    pokemon_id SERIAL PRIMARY KEY,
    type1 TEXT NOT NULL,
    type2 TEXT NOT NULL
);
CREATE TABLE public.HS_Names
(
    name_id SERIAL PRIMARY KEY,
    english_name TEXT NOT NULL,
    japan_name text NOT NULL
);
CREATE TABLE public.LPokemonName
(
    pokemon_id SERIAL PRIMARY KEY,
    name_id int NOT NULL
);
"""
select_all = '''SELECT * FROM HS_Names
'''

insert_info = '''INSERT INTO HS_Pokemon(type1, type2) VALUES('травяной', 'огненный')
'''

conn = psycopg2.connect(host='0.tcp.ngrok.io', port=15912, user='postgres', password='pass')


def insert_names(english_name, japan_name):
    with conn.cursor() as cur:
        cur.execute('INSERT INTO HS_Names(english_name, japan_name) VALUES (%s, %s)', (english_name, japan_name))
        conn.commit()
        hundred = cur.fetchone()[0]
        print(hundred)

        return 0


def insert_new_type(pokemon_id, type1, type2):
    with conn.cursor() as cur:
        cur.execute()
        conn.commit()


def insert_pokemon(name_id):

    with conn.cursor() as cur:
        cur.execute(),
        conn.commit()


def select_type(types):
    with conn.cursor() as cur:
        cur.execute(types)

        resp = cur.fetchall()
        print(resp)


def save_pokemon_to_db(pokemon):
    name_id = insert_names(pokemon.english, pokemon.japan)
    id = insert_pokemon(name_id)
    insert_new_type(id, pokemon.type1, pokemon.type2)


insert_names('pikachu', 'pika')
select_type(select_all)




