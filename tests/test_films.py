def test_get_all_films(all_films, all_films_stored):
    assert len(all_films) == len(all_films_stored)
    for i in range(len(all_films)):
        assert all_films[i].__dict__ == all_films_stored[i]


def test_get_film(three_films, all_films_stored):
    film0, film1, film_none = three_films
    assert film0.__dict__ == all_films_stored[0]
    assert film1.__dict__ == all_films_stored[1]
    assert film_none is None
