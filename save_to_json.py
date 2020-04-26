def save_pokemons(pokemon_list, path_save_dir):
    with open(path_save_dir + '/pokemons.json', 'a', encoding='utf8') as f:
        for pokemon in pokemon_list:
            f.write(str(pokemon)+'\n')
