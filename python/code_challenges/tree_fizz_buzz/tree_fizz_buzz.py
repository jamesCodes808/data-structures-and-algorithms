import copy

def fizz_buzz_tree(kary_tree):
# check if root of kary tree exists
    if kary_tree.root is None:
        return None

# create a deepcopy of kary_tree
    fizzy_tree = copy.deepcopy(kary_tree)

# create a helper recursive function
    def clone_walk(node):
    # process each node from the deep copy
        if node.value % 3 == 0 and node.value % 5 == 0:
            node.value = 'FizzBuzz'
        elif node.value % 3 == 0:
            node.value = 'Fizz'
        elif node.value % 5 == 0:
            node.value = 'Buzz'
        else:
            node.value = str(node.value)
    # call function recursively on the children of the nodes
        for child in node.children:
            clone_walk(child)

    # initially call the recursive function on the cloned root
    clone_walk(fizzy_tree.root)

    return fizzy_tree


