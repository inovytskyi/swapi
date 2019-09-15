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
