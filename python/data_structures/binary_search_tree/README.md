# Binary Search Tree

### Node
Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.

### Binary Search Tree
Create a Binary Search Tree class
- This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following

- additional methods:

  - add()
    - Arguments: value
    - Return: nothing
    - Adds a new node with that value in the correct location in the binary search tree.

  - contains()
    - Argument: value
    - Returns: boolean indicating whether or not the value is in the tree at least once.


## Whiteboard Process

NA

## Approach & Efficiency

The Big O time complexity of a Binary Search Tree’s insertion and search operations is O(h), or O(height). In the worst case, we will have to search all the way down to a leaf, which will require searching through as many nodes as the tree is tall.

In a balanced (or “perfect”) tree, the height of the tree is log(n). In an unbalanced tree, the worst case height of the tree is n

The Big O space complexity of a BST search would be O(1). During a search, we are not allocating any additional space.

The time and space complexity for traversing the binary tree in a depth first method:
Time: O(log n)
Space: O(1)

## Solution

to run the code just enter
```   python3 -m data_structures.binary_search_tree.binary_search_tre ```
into the terminal.

To create a BinarySearchTree:
```python
    tree = BinarySearchTree()
```
To add a new node to the BinarySearchTree:
```python
    tree.add(10)
```
To check if BinarySearchTree contains a value:
```python
tree.contains(10)
```
