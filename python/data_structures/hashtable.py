class Node:
    """
    Properties
    key = default: None, holds the key of the pair
    value = default: None, holds the value of the pair
    """
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

    def display(self):
        collection = []
        collection.append(self.key)
        collection.append(self.value)
        return collection

class Hashtable:
    """
    Properties
    size = specifies the size of the list
    buckets = list with predetermined size from size property, contains key/value pairs
    """

    def __init__(self, size=1024):
        self._size = size
        self._buckets = size * [Node()]

    def set(self, key, value):
        pair = Node(key, value)
        index = self.hash(key)
        self._buckets.insert(index, pair)


    def get(self, key):
        if self.has(key):
            index = self.hash(key)
            pair = self._buckets[index]
            return pair.value
        else:
            return None

    def has(self, key):
        index = self.hash(key)
        if self._buckets[index].value:
            return True
        else:
            return False


    def keys(self):
        key_collection = []
        for i in self._buckets:
            key_collection.append(i.key)
        return key_collection


    def hash(self, key):
        hash_total = 0
        # Add each ASCII value from key together
        for char in key:
            hash_total += ord(char)
        # Multiply it by a prime number
        primed_number = hash_total * 599
        # Use modulo against size of array and get remainder, assign that to index in hash table
        index = primed_number % self._size
        return index

if __name__ == '__main__':
    test_ht = Hashtable(1024)
    test_ht.set("test1", 12345)
    actual = []
    for item in test_ht._buckets:
        if item.value:
            actual.append(item.display())
    # print(actual)
    print(test_ht.hash('test1'))
