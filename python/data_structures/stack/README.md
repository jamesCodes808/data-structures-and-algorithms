# Stack

### Node
Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node

### Stack
- Create a Stack class
- Within your Stack class, include a top property.
  - Upon instantiation, an empty Stack will be created, unless a Node is passed in during instantiation

- The class should contain the following basic methods:
  - push()
    - Arguments: value
    - adds a new node with that value to the top of the stack with an O(1) Time performance.
  - pop()
    - Arguments: none
    - Returns: the value from node from the top of the stack
    - Removes the node from the top of the stack
    - Should raise exception when called on empty stack
  - peek()
    - Arguments: none
    - Returns: Value of the node located at the top of the stack
    - Should raise exception when called on empty stack
  - is_empty()
    - Arguments: none
    - Returns: Boolean indicating whether or not the stack is empty.


## Whiteboard Process

NA

## Approach & Efficiency

I took a TDD approach towards creating the Stack class. Ensuring that
all tests passed as I was creating the code for each function.

The time and space complexity for all of the basic Stack methods are:
Time: O(1)
Space: O(1)

## Solution

to run the code just enter
```  python data_structures/stack/stack.py ```
into the terminal.

To create a Stack:
```python
new_stack = Stack()
```
To add a new node on top of a Stack:
```python
new_stack.push('apple')
```
To print the top value in the Stack:
```python
new_stack.peek()
```
To check if Stack is empty:
```python
new_stack.is_empty()
```
