from data_structures.binary_tree.binary_tree import BinaryTree
from data_structures.binary_tree.binary_tree import Node

class BinarySearchTree(BinaryTree):
    """
    Subclass of BinaryTree
    Has a structure that consists of a root node,
    all values smaller than the root are placed to the left,
    all values larger than the root are placed to the right

    Attributes:
        root: Is a node, has value and only aware left and right child
        nodes, can change with traversal
    """

    def __init__(self, root=None):
        self.root = root

    def add(self, value):
        new_node = Node(value)
        current = self.root

        if current is None:
            self.root = new_node
        else:
            while current:
                if value < current.value:
                    if current.left is None:
                        current.left = new_node
                        return
                    current = current.left
                if value > current.value:
                    if current.right is None:
                        current.right = new_node
                        return
                    current = current.right
        return current


    def contains(self, value):
        current = self.root
        if current is None:
            return False
        else:
            while current:
                if value == current.value:
                    return True
                if value < current.value:
                    if value == current.left:
                        return True
                    current = current.left
                if value > current.value:
                    if value == current.right:
                        return True
                    current = current.right
        return False

if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    print(tree.contains(15))
