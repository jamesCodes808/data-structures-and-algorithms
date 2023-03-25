# Linked Lists

### Node
Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node

### Linked List
- Create a Linked List class
- Within your Linked List class, include a head property.
  - Upon instantiation, an empty Linked List should be created.

- The class should contain the following methods:
  - insert
    - Arguments: value
    - Returns: nothing
    - Adds a new node with that value to the head of the list with an O(1) Time performance.
  - includes
    - Arguments: value
    - Returns: Boolean
      - Indicates whether that value exists as a Node’s value somewhere within the list.

  - to string
    - Arguments: none
    - Returns: a string representing all the values in the Linked List, formatted as:
    ``` "{ a } -> { b } -> { c } -> NULL" ```

## Whiteboard Process

NA

## Approach & Efficiency

I took a TDD approach towards creating the linked list. Ensuring that
all tests passed as I was creating the code for each function.

Creating the linked list and making it dynamically work for how many nodes were created
took quite a while but in the end I got it all to work using a method of taking
the head's node value and using that to traverse through the linked list going from the
front of the list to the back.

The time complexity of this function is O(1) and the space complexity is O(n)

## Solution

to run the code just enter
``` python linked_list/linked_list.py ```
into the terminal.

To create a linked list:
```python
new_linked = LinkedList()
```
To insert a node into a linked list:
```python
new_linked.insert('apple')
```
To print values in linked list:
```python
print(str(new_linked))
```
To check if linked list includes a value:
```python
new_linked.inlcudes('banana')
```
