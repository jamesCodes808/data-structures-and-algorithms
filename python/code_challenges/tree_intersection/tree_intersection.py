from data_structures.hashtable import Hashtable
from data_structures.binary_tree.binary_tree import BinaryTree


def tree_intersection(tree1, tree2):
    # Use hashmap implementation
    hash_table = Hashtable(1024)
    duplicates = set()

    if tree1.root:
        values1 = tree1.pre_order()
        for value in values1:
            hash_table.set(value, value)

    if tree2.root:
        values2 = tree2.pre_order()
        for value in values2:
            if hash_table.has(value) and value not in duplicates:
                duplicates.add(value)

    return list(duplicates)


    # def walk(node, ht, dupes):
    #
    #     while node:
    #         if ht.has(node.value):
    #             dupes.append(node.value)
    #         else:
    #             ht.set(node.value, node.value)
    #         walk(node.left, ht, dupes)
    #         walk(node.right, ht, dupes)
    #
    # if tree1.root:
    #     walk(tree1.root, hash_table, duplicates)
    #
    # if tree2.root:
    #     walk(tree2.root, hash_table, duplicates)
    #
    # return duplicates

    # for value in values1:
    #     hash_table.set(value, value)
    #
    # for value in values2:
    #     if hash_table.has(value):
    #         duplicates.append(value)
    #     else:
    #         hash_table.set(value, value)
    #
    # print('dupes',duplicates)
    # return duplicates
    # return a set of values found in both trees


# used different way to populate the binary tree

if __name__ == '__main__':
    pass



