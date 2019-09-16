from functools import wraps
from urllib.parse import urljoin
from logging import getLogger, INFO
import requests

from entity import Entity
from timeit import timeit

logger = getLogger('SWAPI')
logger.setLevel(INFO)


def sw_timeit(method):
    timed_method = timeit(as_result_time_tuple=True, log=False)(method)

    @wraps(timed_method)
    def wrapper(*args, **kwargs):
        result, executed_time = timed_method(*args, **kwargs)
        entity_type = kwargs.get('entity_type', None)
        url = kwargs.get('url', None)
        if entity_type and url:
            log_message = "{} were get from {} for {:.2f}s".format(entity_type, url, executed_time)
        elif url:
            log_message = "{} was fetch for {:0.2f}s".format(url, executed_time)
        else:
            log_message = "method {} was executed for {:.2f}s".format(method.__name__, executed_time)
        logger.info(log_message)
        return result
    return wrapper


class EntityAPI:
    def __init__(self, swapi):
        self.swapi = swapi


class PeopleAPI(EntityAPI):
    ENTITY_NAME = 'people'

    def get_people(self):
        return self.swapi.get_entities(self.ENTITY_NAME)

    def get_person(self, id):
        return self.swapi.get_entity(id, self.ENTITY_NAME)


class FilmsAPI(EntityAPI):
    ENTITY_NAME = 'films'

    def get_films(self):
        return self.swapi.get_entities(self.ENTITY_NAME)

    def get_film(self, id):
        return self.swapi.get_entity(id, self.ENTITY_NAME)


class SWAPI:
    OK_CODE = 200

    def __init__(self, baseurl=None):
        self.base_url = baseurl if baseurl else 'https://swapi.co/api/'

    def get_entities(self, entity_type):
        url = urljoin(self.base_url, entity_type)
        return SWAPI.get_all_pages(url=url, entity_type=entity_type)

    def get_entity(self, id, entity_type):
        url = '{}/{}'.format(urljoin(self.base_url, entity_type), id)
        person = None
        response = requests.get(url)
        if response.status_code == SWAPI.OK_CODE:
            person = Entity(response.json(), entity_type)
        return person

    @staticmethod
    @sw_timeit
    def get_all_pages(url, entity_type):
        all_results = list()
        result, next_url, _, _ = SWAPI.get_page(url=url)
        all_results.extend([Entity(item, entity_type) for item in result])
        while next_url:
            result, next_url, _, _ = SWAPI.get_page(url=next_url)
            all_results.extend([Entity(item, entity_type) for item in result])
        return all_results

    @staticmethod
    @sw_timeit
    def get_page(url):
        result = list()
        next_url = None
        prev_url = None
        count = 0
        response = requests.get(url)
        if response.status_code == SWAPI.OK_CODE:
            data = response.json()
            result = data.get('results', list())
            next_url = data.get('next', None)
            prev_url = data.get('previous', None)
            count = data.get('count', 0)
        return result, next_url, prev_url, count
