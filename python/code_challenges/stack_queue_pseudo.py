from data_structures.stack.stack import Stack

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

class PseudoQueue:
    def __init__(self):
        self.main_stack = Stack()
        self.temp_stack = Stack()

    def enqueue(self, value):
        self.main_stack.push(value)

    def dequeue(self):

        while self.main_stack.top:
            self.temp_stack.push(self.main_stack.pop())

        front_value = self.temp_stack.pop()

        while self.temp_stack.top:
            self.main_stack.push(self.temp_stack.pop())

        return front_value

if __name__ == '__main__':
    pq = PseudoQueue()
    pq.enqueue("apples")
    pq.enqueue("apples")
    pq.enqueue("bananas")

    print('dequeued', pq.dequeue())
