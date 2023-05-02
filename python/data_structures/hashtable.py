class Node:
    """
    Properties
    key = default: None, holds the key of the pair
    value = default: None, holds the value of the pair
    """
    def __init__(self, value=None, _next=None):
        self.value = value
        self._next = _next

    def display(self):
        collection = []
        if self.value is not None:
            collection.append([self.value[0], self.value[1]])
        return collection


class Hashtable:
    """
    Properties
    size = specifies the size of the list
    buckets = list with predetermined size from size property, contains key/value pairs
    """

    def __init__(self, size=1024):
        self._size = size
        self._buckets = size * [None]

    def set(self, key, value):
        index = self.hash(key)
        bucket = self._buckets[index]
        if bucket is None:
            self._buckets[index] = Node([key, value])
            # self._buckets[index].append([key,value])
            return
        prev = bucket
        while bucket is not None:
            prev = bucket
            bucket = bucket._next
        prev._next = Node([key, value])


    def get(self, key):
        index = self.hash(key)
        bucket = self._buckets[index]
        while bucket is not None and bucket.value[0] != key:
            bucket = bucket._next
        if bucket is None:
            return None
        else:
            return bucket.value[1]


    def has(self, key):
        index = self.hash(key)
        bucket = self._buckets[index]
        while bucket is not None and bucket.value[0] != key:
            bucket = bucket._next

        if bucket is None:
            return False
        if bucket.value[0] == key:
            return True



    def keys(self):
        key_collection = []
        for i in range(0, len(self._buckets)):
            if self._buckets[i] is not None:
                key_collection.append(self._buckets[i].value[0])
            else:
                key_collection.append(None)
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
