def test_get_all_people(all_people, all_people_stored):
    assert len(all_people) == len(all_people_stored)
    for i in range(len(all_people)):
        assert all_people[i].__dict__ == all_people_stored[i]


def test_get_person(three_persons, all_people_stored):
    person0, person1, person_none = three_persons
    assert person0.__dict__ == all_people_stored[0]
    assert person1.__dict__ == all_people_stored[1]
    assert person_none is None


def test_people_page(all_people, people_pages):
    page1, page2, page3, page9 = people_pages
    # count
    assert page1[3] == len(all_people)
    assert page2[3] == len(all_people)
    assert page3[3] == len(all_people)
    assert page9[3] == len(all_people)
    # previous page
    assert page1[2] is None
    assert page2[2] == 'https://swapi.co/api/people/?page=1'
    assert page3[2] == 'https://swapi.co/api/people/?page=2'
    assert page9[2] == 'https://swapi.co/api/people/?page=8'
    # next page
    assert page1[1] == 'https://swapi.co/api/people/?page=2'
    assert page2[1] == 'https://swapi.co/api/people/?page=3'
    assert page3[1] == 'https://swapi.co/api/people/?page=4'
    assert page9[1] is None
