import pytest
from code_challenges.sorting.merge.merge_sort import merge, merge_sort

def test_merge_sort_empty():
    lst = []
    expected_output = []
    merge_sort(lst)
    assert lst == expected_output

def test_merge_sort_single():
    lst = [5]
    expected_output = [5]
    merge_sort(lst)
    assert lst == expected_output

def test_merge_sort_even():
    lst = [5, 2, 9, 1, 7, 4]
    expected_output = [1, 2, 4, 5, 7, 9]
    merge_sort(lst)
    assert lst == expected_output

def test_merge_sort_odd():
    lst = [3, 6, 1, 8, 4, 9, 2, 5, 7]
    expected_output = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    merge_sort(lst)
    assert lst == expected_output
