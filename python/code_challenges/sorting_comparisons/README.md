# Sorting Comparisons

When sorting an array, a key step in the algorithm is determining what their order should be. In the insertion sort algorithm, the insertion phase has a while loop that checks for whether the number to insert is less than the number at the iteration index. The first time the number to insert is greater, the algorithm inserts at the previous index. Merge Sort applies the same logic when recombining sub-arrays, as it needs to choose whether to pull from the left or the right array.

## Sorting Numbers

The comparator function takes `a` and `b`, and returns a number less than zero if `a` should come before `b` when sorting is completed. There are two approaches for numbers to implement such a function. The first uses the < operator, and by convention returns `-1` if `a` < `b`. If `a` > `b`, it returns `1`, and if `a == b`, it returns `0`. While the contract of the comparator function says any number is a valid return so long as the less-than-0 rule holds, by convention we return `-1`, `0`, or `1`

```javascript
function compareNumbers(a, b) {
  if (a == b) return 0;
  if (a < b) return -1;
  if (a > b) return 1;
}

```

## Sorting Strings

Strings seem easy, but are in truth very messy. This is largely because of character encodings and international languages. For the most part, we don’t need to worry about that, if we use what the programming languages give us!

In JavaScript and Python, we can actually use the `<` and `>` operators on strings!

```python
def compare(a, b):
  if a > b:
    return 1
  if a < b:
    return -1
  return 0
```

Unfortunately, this does not work in Java or C#.


## Sorting Objects

Sorting objects typically comes down to sorting based on properties in the object. This is similar to filtering, which often checks one property’s value. When this is necessary, your callback function will take an `a` and a `b` object, apply some logic to choose which properties, and compare them using either the number or string comparisons above. In some applications, this may need to be repeated. For instance, if you are sorting alphabetically for the phone book, you would sort first by last name, and if last names are equal, then by first name. If there are multiple people with the same first and last name, you may decide to then sort by phone number!


## Using Lambda and Sorted in Python

1. We have a list of dicts

```python
movies = [
    {
            'title': "Beetlejuice",
            'year': 1988,
            'genres': ["Comedy", "Fantasy"],
        },
        {
            'title': "The Cotton Club",
            'year': 1984,
            'genres': ["Crime", "Drama", "Music"],
        },
        {
            'title': "The Shawshank Redemption",
            'year': 1994,
            'genres': ["Crime", "Drama"],
        },
]
```

2. We define the sorting function using `lambda`: Use lambda to define a function that will be used to sort the list. The function should take an element from the list as an argument, and return the value that you want to sort by.

```python
    sorted_movies = lambda movie: movie['year']

```

3. Implement the 'sorted' function to sort the list. Pass the list as the first argument, and the sorting function as the `key` argument. The `key` argument tells `sorted` how to sort the list, by using the sorting function defined with `lambda`

```python
sorted_movies = sorted(movies_list, key=lambda movie: movie['year'])

```

>Resources
>
>[Code Challenge: Class 28](https://canvas.instructure.com/courses/6301520/assignments/35899978)
