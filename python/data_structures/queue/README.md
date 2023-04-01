# Queue

### Node
Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node

### Queue
- Create a Queue class that has a front property. It creates an empty Queue when instantiated.
- This object should be aware of a default empty value assigned to front when the queue is created.

- The class should contain the following basic methods:
- enqueue()
  - Arguments: value
  - adds a new node with that value to the back of the queue with an O(1) Time performance.
- dequeue()
  - Arguments: none
    - Returns: the value from node from the front of the queue
    - Removes the node from the front of the queue
    - Should raise exception when called on empty queue
- peek()
  - Arguments: none
  - Returns: Value of the node located at the front of the queue
  - Should raise exception when called on empty stack
- is_empty()
  - Arguments: none
  - Returns: Boolean indicating whether or not the queue is empty


## Whiteboard Process

NA

## Approach & Efficiency

I took a TDD approach towards creating the Queue class. Ensuring that
all tests passed as I was creating the code for each function.

The time and space complexity for all of the basic Stack methods are:
Time: O(1)
Space: O(1)

## Solution

to run the code just enter
```   python data_structures/queue/queue.py ```
into the terminal.

To create a Queue:
```python
new_queue = Queue()
```
To add a new node on to rear of a Queue:
```python
new_queue.enqueue('apple')
```
To remove the node from the front of a Queue:
```python
new_queue.dequeue()
```
To view the front of a Queue:
```python
new_queue.peek()
```

To check if Queue is empty:
```python
new_queue.is_empty()
```
