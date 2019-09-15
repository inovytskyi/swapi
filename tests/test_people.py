def test_get_all_people(all_people, all_people_stored):
    assert len(all_people) == len(all_people_stored)
    for i in range(len(all_people)):
        assert all_people[i].__dict__ == all_people_stored[i]


def test_get_person(three_persons, all_people_stored):
    person0, person1, person_none = three_persons
    assert person0.__dict__ == all_people_stored[0]
    assert person1.__dict__ == all_people_stored[1]
    assert person_none is None
