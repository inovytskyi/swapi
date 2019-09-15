import time


def timeit(method):
    def timed_method(*args, **kwargs):
        star_time = time.time()
        res = method(*args, **kwargs)
        end_time = time.time()
        fetched_time = end_time - star_time
        entity_type  = kwargs.get('entity_type', None)
        url = kwargs.get('url', None)
        if entity_type and url:
            log_message = "{} were get from {} for {:.2f}s".format(entity_type, url, fetched_time)
        elif url:
            log_message = "{} was fetch for {:0.2f}s".format(url, fetched_time)
        else:
            log_message = "method {} was executed for {:.2f}s".format(method.__name__, fetched_time)
        print(log_message)
        return res
    return timed_method

