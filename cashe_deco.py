from time import time, sleep


def save_cashe(time_in_sec):
    def inner(func):
        cashe_saver = dict()

        def wrapper(*args):
            currect_time = time()
            old_keys = []
            for key in cashe_saver:
                if currect_time - cashe_saver[key][1] > time_in_sec:
                    old_keys.append(key)
            for key in old_keys:
                cashe_saver.pop(key)

            if args in cashe_saver:
                result = cashe_saver[args]
            else:
                result = func(*args)
                cashe_saver[args] = [result, time()]
            return result
        return wrapper
    return inner


@save_cashe(5)
def print_words(some_text):
    print(some_text)
    return len(some_text)


