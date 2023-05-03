import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable


# @pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_internals():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    actual = []

    # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
    for item in hashtable._buckets:
        if item is not None:
            actual.append(item.display())

    expected = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]
    print('actual',actual)
    print('expected', expected)
    assert actual == expected

def test_hashtable_get_none():
    test_ht = Hashtable(1024)
    test_ht.set("test1", 12345)
    expected = None
    actual = test_ht.get("test2")
    assert actual == expected

def test_hashtable_keys_get_unique_keys():
    test_ht = Hashtable(3)
    test_ht.set('test1', 12345)
    expected = ['test1']
    actual = test_ht.keys()
    assert actual == expected

def test_hashtable_collision_linked_list():
    test_ht = Hashtable(3)
    test_ht.set('test1', 12345)
    test_ht.set('test1', 54321)
    expected = 54321
    actual = test_ht.get('test1')
    assert actual == expected

def test_hashtable_hash():
    test_ht = Hashtable(1024)
    hash_idx = test_ht.hash('test1')
    if hash_idx in range(0,1024):
        assert True
    else:
        assert False
