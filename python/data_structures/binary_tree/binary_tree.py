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
            else:
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
            else:
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
            else:
                walk(input_node.left, value_list)
                walk(input_node.right, value_list)
                value_list.append(input_node.value)
        walk(self.root, values)
        return values

    def find_maximum_value(self):

        def walk(node):
            # if we hit null value go back to prev iteration
            # stopping case returns something early
            if not node:
                return
            current_value = node.value
            # base case, does all the work until we reach a stopping case
            left_value = walk(node.left)
            right_value = walk(node.right)

            # algorithm/functionality, what will happen once we have all values we need from recursive calls
            if left_value is not None and left_value > current_value:
                current_value = left_value

            if right_value is not None and right_value > current_value:
                current_value = right_value

            return current_value
        return walk(self.root)

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

    # tree.root = Node("a")
    # tree.root = Node(10)
    # tree.root.left = Node(30)
    # tree.root.right = Node(-7)

    # print(tree.post_order())
    print(tree.find_maximum_value())
