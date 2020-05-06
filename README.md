# pokemon_parser

Парсим покемонов 1 и 2 поколения с сайта https://pokemon.fandom.com/ru/wiki/Поколение_I, используя бибилиотеку Parsel.
Модуль main сохраняет данные в json. Moдули save_to_mongo, save_to_psql сохраняют данные в БД.

Cache_deco.py декоратор, который хранит кэш в течение n секунд.

Logger_deco.py декоратор, который записывает в файл logs.log информацию о том, сколько выполнялась функция

