import json

from swapi import SWAPI


def main():
    api = SWAPI()
    people = api.get_people()
    with open('tests/people.json', 'w') as f:
        json.dump([person.__dict__ for person in people ], f)

if __name__ == "__main__":
    main()