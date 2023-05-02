class Node:
    """
    A node in a singly-linked list

    Attributes:
        value (any): The value that is stored in the node.
        next (Node): The next node in the list.
    """

    def __init__(self, value, _next=None):
        self.value = value
        self.next = _next


class LinkedList:
    """
    A singly-linked list.

    Attributes:
        head (Node): First node in the linked list
    """

    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        current_node = self.head
        list_of_nodes = []

        if self.head is None:
            return str(None)
        else:
            while current_node is not None:
                current_value = current_node.value
                list_of_nodes.append('{{ {} }}'.format(current_value))
                current_node = current_node.next
            list_of_nodes.append(str(None))
            return ' -> '.join(list_of_nodes)

    def display(self):
        collection = []
        current = self.head
        while current:
            collection.append([current.value[0], current.value[1]])
        return collection

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def append(self, value):
        new_node = Node(value)
        current = self.head
        if current is None:
            self.head = new_node
            return

        while current:
            if current.next is None:
                current.next = new_node
                break
            else:
                current = current.next

    def insert_before(self, reference, value):
        try:
            current = self.head
            temp = None
            new_node = Node(value)
            while current.value is not reference:
                temp = current
                current = current.next
            new_node.next = current
            if temp:
                temp.next = new_node
            else:
                self.head = new_node
        except Exception:
            raise TargetError

    def insert_after(self, reference, value):
        try:
            current = self.head
            temp = current.next
            new_node = Node(value)
            while current.value is not reference:
                temp = current.next
                current = current.next
            current.next = new_node
            new_node.next = temp
        except Exception:
            raise TargetError

    def kth_from_end(self, k):
        try:
            if k < 0:
                raise TargetError
            else:
                current = self.head
                reversed = []
                while current:
                    reversed.append(current.value)
                    current = current.next
                reversed.reverse()
                return reversed[k]
        except Exception:
            raise TargetError

    @staticmethod
    def zip_lists(list_a, list_b):
        try:
            new_list = LinkedList()
            current_a = list_a.head
            current_b = list_b.head

            while current_a is not None and current_b is not None:
                new_list.append(current_a.value)
                new_list.append(current_b.value)
                current_a = current_a.next
                current_b = current_b.next

            # Add any remaining nodes from list_a
            while current_a is not None:
                new_list.append(current_a.value)
                current_a = current_a.next

            # Add any remaining nodes from list_b
            while current_b is not None:
                new_list.append(current_b.value)
                current_b = current_b.next

            return new_list
        except Exception:
            raise Exception


def traverse_list(self):
    current_node = self.head
    list_of_nodes = []
    while current_node is not None:
        if current_node is None:
            return None
        list_of_nodes.append(current_node)
        current_node = current_node.next
    return list_of_nodes


def includes(self, value):
    temp = self.head
    list_of_node_values = []

    while temp:
        list_of_node_values.append(temp.value)
        temp = temp.next

    if value in list_of_node_values:
        return True
    else:
        return False


class TargetError(AttributeError):
    pass


if __name__ == '__main__':
    # test_linked_list = LinkedList()

    list_a = LinkedList()
    for value in reversed([1, 2, 3]):
        list_a.insert(value)

    list_b = LinkedList()
    for value in reversed(["a", "b", "c"]):
        list_b.insert(value)

    print(list_a)
    print(list_b)

    print(LinkedList.zip_lists(list_a, list_b))
