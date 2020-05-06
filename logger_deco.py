import logging
import sys
import os
from time import time, sleep
from functools import wraps


logging.basicConfig(level=logging.INFO,
                    handlers=[
                        logging.StreamHandler(stream=sys.stdout),
                        logging.FileHandler(os.path.join(os.path.dirname(__file__), 'logs.log'))
                    ],
                    format='%(levelname)8s LINE: %(lineno)d %(asctime)s | %(module)s %(funcName)s | %(message)s',   # funcName wrapper
                    datefmt='%d/%b/%y %H:%M:%S'
                    )


def collect_logs(metric_name):
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            time_start = time()
            result = func(*args, **kwargs)
            time_finish = time()
            logger = logging.getLogger('working_time')
            logger.info('{}: {}, func: {}'.format(metric_name, time_finish - time_start, func.__name__))

            return result
        return wrapper
    return inner


@collect_logs('working time')
def sleep_random(some_time):
    sleep(some_time)
    return 'hello'


print(sleep_random(4))
