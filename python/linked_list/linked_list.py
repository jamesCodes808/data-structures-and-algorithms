class Node:
    """
    A node in a singly-linked list

    Attributes:
        value (any): The value that is stored in the node.
        next (Node): The next node in the list.
    """

    def __init__(self, value=None, _next=None):
        self.value = value
        self._next = next

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
                print(current_node)
                current_value = current_node.value
                list_of_nodes.append('{{ {} }}'.format(current_value))
                current_node = current_node.next
            list_of_nodes.append(str(None))
            return ' -> '.join(list_of_nodes)

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node



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


class TargetError:
    """

    """
    pass

if __name__ == '__main__':
    test_linked_list = LinkedList()
    # print(test_linked_list.head)
    # head_value = test_linked_list.head.value
    # print(head_value)
    test_linked_list.insert('2')
    str(test_linked_list)

    test_linked_list.insert('1')
    str(test_linked_list)
    test_linked_list.insert('0')
    print(str(test_linked_list))
    test_linked_list.insert('0')
    print(str(test_linked_list))
    test_linked_list.insert('0')
    print(str(test_linked_list))
    test_linked_list.insert('0')
    print(str(test_linked_list))
    test_linked_list.insert('0')
    print(str(test_linked_list))
    test_linked_list.insert('0')
    print(str(test_linked_list))
    test_linked_list.insert('0')
    print(str(test_linked_list))

