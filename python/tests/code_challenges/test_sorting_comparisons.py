import pytest

from code_challenges.sorting_comparisons.movies import movies
from code_challenges.sorting_comparisons.sorting_comparisons import sort_compare_alphabetical, \
    sort_compare_year



def test_sort_compare_year_first():
    expected = 'The Intouchables'
    list = sort_compare_year(movies)
    actual = []
    for movie in list:
        actual.append(movie['title'])
    assert actual[0] == expected

def test_sort_compare_year_last():
    expected = 'The Cotton Club'
    list = sort_compare_year(movies)
    actual = []
    for movie in list:
        actual.append(movie['title'])
    assert actual[-1] == expected

def test_sort_compare_alphabet_first():
    expected = 'Beetlejuice'
    list = sort_compare_alphabetical(movies)
    actual = []
    for movie in list:
        actual.append(movie['title'])
    assert actual[0] == expected


def test_sort_compare_alphabet_last():
    expected = 'Valkyrie'
    list = sort_compare_alphabetical(movies)
    actual = []
    for movie in list:
        actual.append(movie['title'])
    assert actual[-1] == expected

def test_sort_compare_alphabet_whole():
    expected = ["Beetlejuice", "City of God", "The Cotton Club", "Crocodile Dundee", "The Intouchables", "Memento",
                "Ratatouille", "The Shawshank Redemption", "Stardust", "Valkyrie"]
    list = sort_compare_alphabetical(movies)
    actual = []
    for movie in list:
        actual.append(movie['title'])
    assert actual == expected

def test_sort_compare_year_whole():
    expected = ["The Intouchables", "Valkyrie", "Stardust", "Ratatouille", "City of God", "Memento", "The Shawshank Redemption", "Beetlejuice", "Crocodile Dundee", "The Cotton Club"]
    list = sort_compare_year(movies)
    actual = []
    for movie in list:
        actual.append(movie['title'])
    assert actual == expected
