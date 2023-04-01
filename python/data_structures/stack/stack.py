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

class Stack:
    """
    Stack that consists of nodes.

    Attributes:
        top: Is a node, has value and only aware of next node in stack
    """

    def __init__(self, top=None):
        self.top = top

    # pushes node on stack
    def push(self, val):
        new_node = Node(val)
        if self.top is None:
            self.top = new_node
            return

        if self.top is not None:
            new_node._next = self.top
            self.top = new_node

    # pops node off top of stack
    def pop(self):
        try:
            temp = self.top
            self.top = self.top._next
            temp._next = None
            return temp.value
        except Exception:
            raise InvalidOperationError('Method not allowed on empty collection')

    def peek(self):
        try:
            return self.top.value
        except Exception:
            raise InvalidOperationError('Method not allowed on empty collection')

    def is_empty(self):
        return self.top is None

if __name__ == '__main__':
    test_stack = Stack()
    test_stack.push('thing')
    print(test_stack.is_empty())
