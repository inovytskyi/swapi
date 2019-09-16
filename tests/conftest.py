import pytest
from swapi import SWAPI, FilmsAPI
from swapi import PeopleAPI
import json


@pytest.fixture(scope='session')
def all_people():
    api = SWAPI()
    people_api = PeopleAPI(api)
    return people_api.get_people()


@pytest.fixture(scope='session')
def all_films():
    api = SWAPI()
    films_api = FilmsAPI(api)
    return films_api.get_films()


@pytest.fixture(scope='session')
def all_people_stored():
    import json
    with open('tests/people.json', 'r') as f:
        data = json.load(f)
    return data


@pytest.fixture(scope='session')
def all_films_stored():
    with open('tests/films.json', 'r') as f:
        data = json.load(f)
    return data


@pytest.fixture(scope='session')
def three_films():
    api = SWAPI()
    films_api = FilmsAPI(api)
    film0 = films_api.get_film(1)
    film1 = films_api.get_film(2)
    film_none = films_api.get_film(89)
    return film0, film1, film_none


@pytest.fixture(scope='session')
def people_pages():
    page1 = SWAPI.get_page('https://swapi.co/api/people')
    page2 = SWAPI.get_page('https://swapi.co/api/people/?page=2')
    page3 = SWAPI.get_page('https://swapi.co/api/people/?page=3')
    page9 = SWAPI.get_page('https://swapi.co/api/people/?page=9')
    return page1, page2, page3, page9


@pytest.fixture(scope='session')
def three_persons():
    from swapi import SWAPI
    api = SWAPI()
    people_api = PeopleAPI(api)
    person0 = people_api.get_person(1)
    person1 = people_api.get_person(2)
    person_none = people_api.get_person(89)
    return person0, person1, person_none


@pytest.fixture(scope='session')
def people_schema():
    with open('tests/people_schema.json', 'r') as f:
        data = json.load(f)
    return data


@pytest.fixture(scope='session')
def films_schema():
    with open('tests/films_schema.json', 'r') as f:
        data = json.load(f)
    return data
