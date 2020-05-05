import logging
import sys
from time import sleep, time
from functools import wraps

logging.basicConfig(level=logging.INFO,
                    handlers=[
                        logging.StreamHandler(stream=sys.stdout),
                        logging.FileHandler('logs.log')
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
            logger.info('{}: {}, func {}'.format(metric_name, time_finish - time_start, func.__name__))
            return result
        return wrapper
    return inner


@collect_logs('working_time')
def mult(n1, n2):
    sleep(4)
    return n1+n2


mult(4, 5)