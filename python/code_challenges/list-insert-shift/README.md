# List Insert Shift

Write a function called ```insertShiftArray``` which takes in an array and a value to be added. Without utilizing any of the built-in methods available to your language, return an array with the new value added at the middle index.

## Whiteboard Process

![Whiteboard Process](insertShiftList-wb.png)

## Approach & Efficiency

The approach that we took on this code challenge without utilizing too many built in functions was to create an empty list inside of the function. 

We then would need to find the middle of the list using len().

With that middle index we could insert the start to the middle of the argument list to the empty list, append the argument value after, then append the rest of the argument list to the empty list.

With that logic, we would return the argument list with the value inserted into the middle.

The time complexity of this function is O(n), where n is the length of the input list, and the space complexity is O(n), due to the creation of a new list with n/2 elements.

The temporary variables created in the function, 'middle' and 'newList' all take constant time so they can be ignored. 


## Solution
...in progress
<!-- Show how to run your code, and examples of it in action -->