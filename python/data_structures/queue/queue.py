from data_structures.invalid_operation_error import InvalidOperationError

class Node:
    """
    Node

   Attributes:
    value: data type value, can be int, string
    _next: only aware of node next to this node
    """

    def __init__(self, value, _next=None):
        self.value = value
        self._next = _next

class Queue:
    """
    Queue that consists of nodes.

    Attributes:
        front: Is a node, is the front of the queue, has value and only aware of next node in queue
        back: Is a node, is the rear of the queue, has value and only aware of next node in queue
    """

    def __init__(self, front=None):
        self.front = front
        self.rear = None

    # adds node to rear of queue
    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:
            self.rear = new_node
            self.front = new_node
        self.rear._next = new_node
        self.rear = new_node


    # removes node from front of queue
    def dequeue(self):
        try:
            temp = Node(self.front.value)
            self.front = self.front._next
            temp._next = None
            return temp.value
        except Exception:
            raise InvalidOperationError

    def peek(self):
        try:
            return self.front.value
        except Exception:
            raise InvalidOperationError

    def is_empty(self):
        return self.front is None
