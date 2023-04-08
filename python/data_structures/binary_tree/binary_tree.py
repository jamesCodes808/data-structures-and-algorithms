class BinaryTree:
    """
    Tree that consists of nodes and is only aware of the root node

    Attributes:
        root: Is a node, has value and only aware left and right child nodes, can change through traversal
    """

    def __init__(self, root=None):
        self.root = root


    def pre_order(self, values=[]):
        # root >> left >> right
        def walk(input_node, value_list):
            if not input_node:
                return
            value_list.append(input_node.value)
            walk(input_node.left, value_list)
            walk(input_node.right, value_list)
        walk(self.root, values)
        return values

    def in_order(self, values=[]):
        # left >> root >> right
        def walk(input_node, value_list):
            if not input_node:
                return
            walk(input_node.left, value_list)
            value_list.append(input_node.value)
            walk(input_node.right, value_list)
        walk(self.root, values)
        return values

    def post_order(self, values=[]):
        # left >> right >> root
        def walk(input_node, value_list):
            if not input_node:
                return
            walk(input_node.left, value_list)
            walk(input_node.right, value_list)
            value_list.append(input_node.value)
        walk(self.root, values)
        return values

class Node:
    """
    Node consists of a value, aware of left and right child nodes

    Attributes:
        value: contains data
        left: contains pointer to child node on the left
        right: contains pointer to child node on the right
    """
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

if __name__ == '__main__':
    tree = BinaryTree()

    tree.root = Node("a")
    tree.root.left = Node("b")
    tree.root.right = Node("c")
    tree.root.left.left = Node("d")
    tree.root.left.right = Node("e")
    tree.root.right.left = Node("f")
    tree.root.right.right = Node("g")

    print(tree.post_order())
