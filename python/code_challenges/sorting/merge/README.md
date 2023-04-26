# Merge Sort

Merge Sort is a popular sorting algorithm that uses the divide and conquer technique to sort an array. It works by breaking down the array into smaller and smaller sub-arrays until the sub-arrays are small enough to be sorted easily. Then it merges the sub-arrays back together, sorting them in the process. The algorithm has a time complexity of O(n*log(n)).

### Pseudo Code Implementation:

```
ALGORITHM merge_sort(lst)
    DECLARE n <-- lst.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- lst[0...mid]
      DECLARE right <-- lst[mid...n]
      // sort the left side
      merge_sort(left)
      // sort the right side
      merge_sort(right)
      // merge the sorted left and right sides together
      merge(left, right, lst)

ALGORITHM merge(left, right, lst)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            lst[k] <-- left[i]
            i <-- i + 1
        else
            lst[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in lst to remaining values in right
    else
       set remaining entries in lst to remaining values in left

```

## How it works:

### Input:

- Sample List: `[5, 2, 9, 1, 7, 4]`

## First recursive call to merge_sort

The `merge_sort` function is called with the input list. The length of the list is greater than 1, so we continue with the algorithm. We split the list into two sub-lists of equal size:

```python
left = [5, 2, 9]
right = [1, 7, 4]
```

We make recursive calls to merge_sort with left and right:



### Recursive call with `left`

The `merge_sort` function is called with the list `[5, 2, 9]`. The length of the list is greater than 1, so we continue with the algorithm. We split the list into two sub-lists of equal size:

```python
left: [5]
right: [2, 9]

```

We make recursive calls to `merge_sort` with `left` and `right`:

#### Recursive call with `left`
The `merge_sort` function is called with the list `[5]`. The length of the list is less than or equal to 1, so we do not make any further recursive calls. The list is already sorted.

#### Recursive call with `right`
The `merge_sort` function is called with the list `[2, 9]`. The length of the list is greater than 1, so we continue with the algorithm. We split the list into two sub-lists of equal size:

```python
left: [2]
right: [9]

```
We make recursive calls to `merge_sort` with `left` and `right`:

#### Recursive call with `left`

The `merge_sort` function is called with the list `[2]`. The length of the list is less than or equal to 1, so we do not make any further recursive calls. The list is already sorted.

#### Recursive call with `right`

The `merge_sort` function is called with the list `[9]`. The length of the list is less than or equal to 1, so we do not make any further recursive calls. The list is already sorted.

We now have two sorted sub-lists:

```python
left: [5]
right: [2, 9]

```

We call the `merge` function with these sub-lists and the original list:

```python
merge([5], [2, 9], [5, 2, 9])

```

## First call to merge

The `merge` function is called with the sub-lists `[5]` and `[2, 9]` and the original list `[5, 2, 9]`. We initialize variables `i`, `j`, and `k` to `0`. We enter the while loop and compare `left[i]` and `right[j]`. Since `left[i]` is less than or equal to `right[j]`, we set `lst[k]` to `left[i]` and increment `i` and `k`. We continue this process until `i` is equal to the length of `left`.

```python
lst: [5, 2, 9]
left: [5]
right: [2, 9]
i: 1
j: 0
k: 1

```

We exit the while loop and set the remaining entries in `lst` to the remaining values in `right`:

```python
lst: [5, 2, 9, 1, 7, 4]
left: [5]
right: [2, 9]
i: 1
j: 2
k: 3

```

We have now merged the two sub-lists `[5]` and `[2, 9]` into the sorted list `[2, 5, 9]`.

## Second call to merge_sort

We return to the previous call to `merge_sort` with the sub-lists `[2, 5, 9]` and `[1, 7, 4]`. We initialize variables `i`, `j`, and `k` to 0. We enter the while loop and compare `left[i]` and `right[j]`. Since `right[j]` is less than `left[i]`, we set `lst[k]` to `right[j]` and increment `j` and `k`. We continue this process until `j` is equal to the length of `right`.

```python
lst: [2, 5, 9, 1, 7, 4]
left: [2, 5, 9]
right: [1, 7, 4]
i: 0
j: 3
k: 0

```

We exit the while loop and set the remaining entries in `lst` to the remaining values in `left`:

```python
lst: [1, 2, 4, 5, 7, 9]
left: [2, 5, 9]
right: [1, 7, 4]
i: 3
j: 3
k: 3

```

We have now merged the two sub-lists `[2, 5, 9]` and `[1, 7, 4]` into the sorted list `[1, 2, 4, 5, 7, 9]`.

## Output

The final output is the sorted list `[1, 2, 4, 5, 7, 9]`.


### Here's how the data changes throughout the algorithm:

At each step, the list is split into two sub-lists, which are recursively sorted until they can be merged back together in the correct order.

```

[5, 2, 9, 1, 7, 4]

[5, 2, 9]   [1, 7, 4]

[5]  [2, 9]   [1]  [7, 4]

[5]  [2]  [9]  [1]  [7]  [4]

[2, 5, 9]    [1, 4, 7]

[1, 2, 4, 5, 7, 9]


```


### Python Implementation:

```python
def merge_sort(lst):
    n = len(lst)

    if n > 1:
        mid = n // 2
        left = lst[:mid]
        right = lst[mid:]

        # sort the left side
        merge_sort(left)

        # sort the right side
        merge_sort(right)

        # merge the sorted left and right sides together
        merge(left, right, lst)


def merge(left, right, lst):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            lst[k] = left[i]
            i += 1
        else:
            lst[k] = right[j]
            j += 1
        k += 1

    # set remaining entries in lst to remaining values in left or right
    while i < len(left):
        lst[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        lst[k] = right[j]
        j += 1
        k += 1


```

Usage Example:

```python
# Example usage
lst = [5, 2, 9, 1, 7, 4]
merge_sort(lst)
print(lst)  # Output: [1, 2, 4, 5, 7, 9]
```
