import pytest


@pytest.fixture(scope='module')
def all_people():
    from swapi import SWAPI
    api = SWAPI()
    return api.get_people()


@pytest.fixture(scope='module')
def all_people_stored():
    import json
    with open('tests/people.json', 'r') as f:
        data = json.load(f)
    return data


@pytest.fixture(scope='module')
def people_pages():
    from swapi import SWAPI
    api = SWAPI()
    page1 = SWAPI.get_page('https://swapi.co/api/people')
    page2 = SWAPI.get_page('https://swapi.co/api/people/?page=2')
    page3 = SWAPI.get_page('https://swapi.co/api/people/?page=3')
    page9 = SWAPI.get_page('https://swapi.co/api/people/?page=9')
    return page1, page2, page3, page9


@pytest.fixture(scope='module')
def three_persons():
    from swapi import SWAPI
    api = SWAPI()
    person0 = api.get_person(1)
    person1 = api.get_person(2)
    person_none = api.get_person(89)
    return person0, person1, person_none
