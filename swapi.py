from urllib.parse import urljoin
import requests

from entity import Entity
from utils import timeit


class SWAPI(object):
    OK_CODE = 200
    PEOPLE = 'people'
    FILMS = 'films'

    def __init__(self, baseurl=None):
        self.base_url = baseurl if baseurl else 'https://swapi.co/api/'

    def get_films(self):
        return self._get_entities(SWAPI.FILMS)

    def get_film(self, id):
        return self._get_entity(id, SWAPI.FILMS)

    def get_people(self):
        return self._get_entities(SWAPI.PEOPLE)

    def get_person(self, id):
        return self._get_entity(id, SWAPI.PEOPLE)

    def _get_entities(self, entity_type):
        url = urljoin(self.base_url, entity_type)
        return SWAPI.get_all_pages(url=url, entity_type=entity_type)

    def _get_entity(self, id, entity_type):
        url = '{}/{}'.format(urljoin(self.base_url, entity_type), id)
        person = None
        response = requests.get(url)
        if response.status_code == SWAPI.OK_CODE:
            person = Entity(response.json(), entity_type)
        return person

    @staticmethod
    @timeit
    def get_all_pages(url, entity_type):
        all_results = list()
        result, next_url, _, _ = SWAPI.get_page(url=url)
        all_results.extend([Entity(item, entity_type) for item in result])
        while next_url:
            result, next_url, _, _ = SWAPI.get_page(url=next_url)
            all_results.extend([Entity(item, entity_type) for item in result])
        return all_results

    @staticmethod
    @timeit
    def get_page(url):
        result = list()
        next_url = None
        response = requests.get(url)
        if response.status_code == SWAPI.OK_CODE:
            data = response.json()
            result = data.get('results', list())
            next_url = data.get('next', None)
            prev_url = data.get('previous', None)
            count = data.get('count', 0)
        return result, next_url, prev_url, count
