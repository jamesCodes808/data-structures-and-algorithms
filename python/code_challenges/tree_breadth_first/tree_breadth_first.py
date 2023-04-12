from data_structures.binary_tree.binary_tree import BinaryTree, Node as Tree_Node
from data_structures.queue.queue import Queue, Node as Queue_Node

def breadth_first(tree):

    if tree.root is None:
        return []

    breadth = Queue()
    breadth.enqueue(tree.root)
    values = []

    while not breadth.is_empty():
        current = breadth.dequeue()
        values.append(current.value)

        if current.left:
            breadth.enqueue(current.left)
        if current.right:
            breadth.enqueue(current.right)
    return values


# if __name__ == '__main__':
#     tree = BinaryTree()
#     node1 = Tree_Node('apples')
#     print(breadth_first(tree))
