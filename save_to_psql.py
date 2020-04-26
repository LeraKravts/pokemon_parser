import psycopg2
from psycopg2.extras import execute_values
import pandas as pd

conn = psycopg2.connect(host='0.0.0.0',
                        port=5432,
                        user='postgres',
                        password=' ',
                        )

# create_query = """
# CREATE TABLE my_pokemons (
#     id SERIAL PRIMARY KEY,
#     type1 varchar(100) NOT NULL,
#     type2 varchar(100),
#     name varchar(100) NOT NULL,
#     english varchar(100) NOT NULL,
#     japan varchar(100) NOT NULL,
#     url varchar(100) NOT NULL
# );
# """
# with conn.cursor() as cur:
#     cur.execute(create_query)

table = pd.read_csv('pokemons.csv', header=None)

table.columns = ['Russian', 'Type1', 'Type2', 'English', 'Japan', 'Url']
type1 = table.Type1.unique()
type2 = table.Type2.unique()
name = table.Russian.unique()
english = table.English.unique()
japan = table.Japan.unique()
url = table.Url

with conn, conn.cursor() as cur:
       execute_values(
           cur,
           'INSERT INTO my_pokemons(type1, type2, name, english, japan, url) VALUES %s',
           table.to_dict('records'),
           template='(%(Type1)s, %(Type2)s, %(Russian)s, %(English)s, %(Japan)s, %(Url)s)'
       )
