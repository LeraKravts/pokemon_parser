import os

from parser import get_pokemons
from save import save_pokemons
from parser import resp1, resp2


PATH_SAVE_DIR = '/Users/valeriya/Desktop/'


def main():

    if os.path.exists(PATH_SAVE_DIR + 'pokemons.csv'):
        os.remove(PATH_SAVE_DIR + 'pokemons.csv')

    save_pokemons(get_pokemons(resp1.text), PATH_SAVE_DIR)
    save_pokemons(get_pokemons(resp2.text), PATH_SAVE_DIR)


if __name__ == '__main__':
    main()
