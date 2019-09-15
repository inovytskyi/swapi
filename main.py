from swapi import SWAPI


def main():
    api = SWAPI()
    people = api.get_people()

if __name__ == "__main__":
    main()