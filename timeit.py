import time
from functools import wraps
from logging import getLogger
logger = getLogger('SWAPI')


def timeit(as_result_time_tuple=False, log=True):
    def timeit_decorator(method):
        @wraps(method)
        def timed_method(*args, **kwargs):
            star_time = time.time()
            res = method(*args, **kwargs)
            end_time = time.time()
            executed_time = end_time - star_time
            if log:
                logger.info("method {} was executed for {:.2f}s".format(method.__name__, executed_time))
            return res if not as_result_time_tuple else res, executed_time
        return timed_method
    return timeit_decorator
