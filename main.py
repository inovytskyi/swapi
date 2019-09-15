from swapi import SWAPI


def main():
    api = SWAPI()
    people = api.get_people()
    films = api.get_films()


if __name__ == "__main__":
    main()
