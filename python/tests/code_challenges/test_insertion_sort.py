from code_challenges.sorting.insertion.insertion_sort import insert, insertion_sort
import pytest

def test_Insert():
    sorted_list = [1, 3, 5]
    insert(sorted_list, 4)
    assert sorted_list == [1, 3, 4, 5]

    sorted_list = [1, 3, 5]
    insert(sorted_list, 0)
    assert sorted_list == [0, 1, 3, 5]

    sorted_list = [1, 3, 5]
    insert(sorted_list, 6)
    assert sorted_list == [1, 3, 5, 6]

def test_InsertionSort():
    input_list = [4, 2, 7, 1, 3]
    assert insertion_sort(input_list) == [1, 2, 3, 4, 7]

    input_list = [1, 2, 3, 4, 5]
    assert insertion_sort(input_list) == [1, 2, 3, 4, 5]

    input_list = [5, 4, 3, 2, 1]
    assert insertion_sort(input_list) == [1, 2, 3, 4, 5]
