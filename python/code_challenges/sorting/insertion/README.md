# Insertion Sort

The concept behind insertion sort in lists is to divide the list into a sorted part and an unsorted part, and then insert each unsorted element into its correct position in the sorted part.

## Pseudocode Example

```python

Insert(int[] sorted, int value)
  initialize i to 0
  WHILE value > sorted[i]
    set i to i + 1
  WHILE i < sorted.length
    set temp to sorted[i]
    set sorted[i] to value
    set value to temp
    set i to i + 1
  append value to sorted

InsertionSort(int[] input)
  LET sorted = New Empty Array
  sorted[0] = input[0]
  FOR i from 1 up to input.length
    Insert(sorted, input[i])
  return sorted

```

### Trace

Sample list: `[5, 2, 8, 4, 7]`

### What you need:

- An unsorted list of elements
- A for loop
- A while loop
- A temporary variable
- Knowledge of recursive functions

## Step 1: Define the Insert function

The `insert` function takes a sorted list `sorted_list` and a value, named `value`, as input and inserts the value in
the correct
position in the sorted list. Here's the Python code for the `insert` function:

```python
def insert(sorted_list, value):
    i = 0
    while i < len(sorted_list) and value > sorted_list[i]:
        i += 1
    sorted_list.insert(i, value)

```

The `insert` function starts by initializing `i` to 0, which represents the position in the sorted list where the `value`
will be inserted. The function then enters a loop that iterates over the sorted list until it finds the correct position for the value.

If the current value in the sorted list is less than the value being inserted, the loop continues to the next index in the list. Once the loop has found the correct position for the value, it uses the `insert` method to insert the value at that position.

## Step 2: Define the InsertionSort function

The `insertion_sort` function takes an unsorted input list `input_list` as input and returns the sorted list. Here's the
Python code for the `insertion_sort` function:


```python

def insertion_sort(input_list):
    sorted_list = [input_list[0]]
    for i in range(1, len(input_list)):
        insert(sorted_list, input_list[i])
    return sorted_list

```

The `insertion_sort` function starts by creating a new list called `sorted_list` and initializing it with the first
element from the input list. The function then enters a loop that iterates over the remaining elements in the input list.

For each element, the function calls the `insert` function to insert the element in the correct position in the
sorted list. Finally, the function returns the sorted list.

### Step 3: Test the InsertionSort function

To test the `insertion_sort` function, you can create an unsorted input list and call the function with this list.
Here's the Python code to do this:


```python

input_list = [5, 2, 8, 4, 7]
sorted_list = insertion_sort(input_list)
print(sorted_list)


```

When you run this code, you should see the following output:

```python
[2, 4, 5, 7, 8]

```

This output confirms that the `insertion_sort` function correctly sorted the input list using the insertion sort
algorithm.


Complete implementation:

```python

def insert(sorted_list, value):
    i = 0
    while i < len(sorted_list) and value > sorted_list[i]:
        i += 1
    sorted_list.insert(i, value)

def insertion_sort(input_list):
    sorted_list = [input_list[0]]
    for i in range(1, len(input_list)):
        insert(sorted_list, input_list[i])
    return sorted_list

```

Hope this helps you understand the insertion sort algorithm using lists in python!

By: James Ian R. Solima
