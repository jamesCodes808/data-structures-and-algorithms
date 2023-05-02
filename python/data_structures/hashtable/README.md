# Hash Table

Datastructure that holds nodes at hashed indexes in table for quick and efficient lookup.

## Methods

- set()
  - Arguments: key, value
  - Returns: nothing
  - This method hashes the key, and sets the key and value pair into a Node, then into the Hashtable,
  - Should a given key already exist, replace its value from the value argument given to this method.

- get()
  - Arguments: key
  - Returns: Value associated with that key in the table
  - Hashes the key to find index in Hashtable, checks if key exists, retrieves value

- has()
  - Arguments: key
  - Returns: Boolean, indicating if the key exists in the table already.
  - Hashes key to find index, checks hashtable with index if key exists in hashtable

- keys()
  - Returns: Collection of keys

- hash()
  - Arguments: key
  - Returns: Index in the collection for that key
  - Performs algorithm to hash key into index in the range of hashtable size


# Node

Node for Hashtable, has a key and value pair

Properties
- key
- value

## Methods

- display()
- Arguments: None
- Returns: key value pair


## References

Tyler Huntley - Helping me understand this better and explaining how they got the get and set method working with
LinkedList
