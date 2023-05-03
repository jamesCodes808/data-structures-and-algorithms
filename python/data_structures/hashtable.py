class Node:
    """
    Properties
    key = default: None, holds the key of the pair
    value = default: None, holds the value of the pair
    """

    def __init__(self, key=None, value=None, _next=None):
        self.key = key
        self.value = value
        self._next = _next

    def display(self):
        collection = []
        current = self
        while current:
            if current.value is not None:
                collection.append([current.key, current.value])
            current = current._next
        return collection


class Hashtable:
    """
    Properties
    _size = specifies the _size of the list
    buckets = list with predetermined _size from _size property, contains key/value pairs
    """

    def __init__(self, _size=1024):
        self._size = _size
        self._buckets = _size * [None]

    def hash(self, key):
        """
        Hashes the given key and returns an index into the hashtable.
        """
        if isinstance(key, int):
            key = str(key)
        sum = 0
        for char in key:
            sum += ord(char)
        primed = sum * 599
        index = primed % self._size
        return index

    def set(self, key, value):
        """
        Associates the given key with the given value in the hashtable.
        """
        index = self.hash(key)
        if not self._buckets[index]:
            self._buckets[index] = Node(key, value)
        else:
            current = self._buckets[index]
            while current._next:
                if current.key == key:
                    current.value = value
                    return
                current = current._next
            if current.key == key:
                current.value = value
                return
            current._next = Node(key, value)

    def get(self, key):
        """
        Returns the value associated with the given key in the hashtable, or None if the key is not in the hashtable.
        """
        index = self.hash(key)
        current = self._buckets[index]
        while current:
            if current.key == key:
                return current.value
            current = current._next
        return None

    def keys(self):
        """
        Returns a list of all the keys in the hashtable.
        """
        key_list = []
        for bucket in self._buckets:
            if bucket:
                current = bucket
                while current:
                    key_list.append(current.key)
                    current = current._next
        return key_list

    def has(self, key):
        """
        Returns True if the given key is in the hashtable, False otherwise.
        """
        index = self.hash(key)
        current = self._buckets[index]
        while current:
            if current.key == key:
                return True
            current = current._next
        return False



if __name__ == '__main__':
    test_ht = Hashtable(3)
    test_ht.set("test1", 12345)
    # test_ht.set("test2", 65483)
    # test_ht.set("test3", 98752)
    # actual = []
    # for item in test_ht._buckets:
    #     if item is not None:
    #         actual.append(item.display())
    # print(actual)
    # print(test_ht.hash('test1'))
    print(test_ht.keys())
    # print(test_ht.has("test3"))
