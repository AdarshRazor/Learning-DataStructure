# Arrays

* Linear Data Structure
* Elements are stored in contiguous memory locations
* Can access elements randomly using index
* Stores homogeneous elements i.e, similar elements
* Syntax:
    * Array declarations:
        * Data type array_name[size];
            * new Data type[10];
    * Can also do declarations and initialisation in one line:
        * Array name = [element1, element2, element3, ...]
        * new Data type[10] = {1,2,3,4,5,6,7,8,9,10};


## Advantages and Disadvantages

* Advantages of arrays:
    * In array random access is fast.
    * In array, elements are stored in contiguous memory locations.
    * Arrays are easy to sort and interate over.
    Replacement of multiple elements is fast.
* Disadvantages of arrays:
    * Arrays are not as flexible as linked lists.
    * Arrays size is fixed.
    * Elements are difficult to insert and delete.
    * Arrays need contiguous memory locations.
* Applications:
    * Can be used as a **stack and queue.**
    * Can be used as a **linked list.**

## Implementation (Code)

```python
import array
my_array = array.array('i', [1, 2, 3, 4, 5])
```