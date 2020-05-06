from time import time


def save_cache(time_in_sec):
    def inner(func):
        cache_saver = dict()

        def wrapper(*args):
            currect_time = time()
            old_keys = []
            for key in cache_saver:
                if currect_time - cache_saver[key][1] > time_in_sec:
                    old_keys.append(key)
            for key in old_keys:
                cache_saver.pop(key)

            if args in cache_saver:
                result = cache_saver[args]
            else:
                result = func(*args)
                cache_saver[args] = [result, time()]
            return result
        return wrapper
    return inner
