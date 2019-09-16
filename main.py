from logging import getLogger, StreamHandler, INFO
from sys import stdout

from swapi import SWAPI, PeopleAPI, FilmsAPI


def main():
    api = SWAPI()

    logger = getLogger()
    handler = StreamHandler(stream=stdout)
    handler.setLevel(INFO)
    logger.addHandler(handler)
    people_api = PeopleAPI(api)
    films_api = FilmsAPI(api)
    people = people_api.get_people()

    films = films_api.get_films()


if __name__ == "__main__":
    main()
