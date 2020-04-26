import argparse as argparse
import psycopg2


if __name__ == '__main__':

    conn = psycopg2.connect(host='0.0.0.0',
                            port=5432,
                            user='postgres',
                            password=' ',
                            )

    parser = argparse.ArgumentParser()
    parser.add_argument('select',
                        type=str,
                        help='''Write SQL query in string format. 
                                Table name: my_pokemons. 
                                Dy default 10 rows will be displayed.
                                If you want to display 5 rows(for example), type: --limit "limit 5"''',
                        )

    parser.add_argument('--limit', default='limit 10;', help='limit number of rows')
    args = parser.parse_args()

    with conn.cursor() as cur:
        cur.execute(f'{args.select} {args.limit}')
        resp = cur.fetchall()
