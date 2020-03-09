from parsel import Selector
from pokemon import Pokemon


def get_pokemons(html: str) -> list:
    sel = Selector(text=html)
    pokemon_table = sel.css('table[class="wikitable sortable"]')
    pokemons = []
    for row in pokemon_table.css('tr')[1:]:
        elements = row.css('td')
        name = elements[2].css('a::text').get().strip()
        type1 = elements[3].css('a::text').get().strip()
        type2 = elements[4].css('a::text').get()
        if type2 is not None:
            type2 = type2.strip()
        english = elements[5].css('::text').get().strip()
        japan = elements[6].css('::text').get().strip()
        pokemons.append(Pokemon(name, type1, type2, english, japan))
    return pokemons

