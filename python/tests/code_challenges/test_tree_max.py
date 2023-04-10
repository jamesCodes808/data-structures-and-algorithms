import pytest
from data_structures.binary_tree.binary_tree import BinaryTree, Node


# @pytest.mark.skip("TODO")
def test_max_val():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(30)
    tree.root.right = Node(-7)

    actual = tree.find_maximum_value()
    expected = 30

    assert actual == expected

def test_empty_max_val():
    tree = BinaryTree()
    actual = tree.find_maximum_value()
    expected = None
    assert actual == expected

def test_one_max_val():
    tree = BinaryTree()
    tree.root = Node(10)
    actual = tree.find_maximum_value()
    expected = 10
    assert actual == expected
