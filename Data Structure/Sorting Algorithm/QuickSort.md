# Quick Sort

Quick sort is a divide-and-conquer sorting algorithm. It works by selecting a "pivot" element from the array and partitioning the other elements into two sub-arrays. 

It arranges the sub-arrays according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively using the same process. 

![image](https://user-images.githubusercontent.com/33658792/236675902-3e833b37-e93b-4596-8c18-98a35f8dfc3f.png)


## Implementation

1. It starts by choosing the first element as the pivot.
2. Partition the remaining elements into two sub-arrays. 
3. Elements in the left sub-arrays should be lesser and the right sub-arrays are greater than the pivot.
4. Repeat the same process you are done. :fire:

## Space and time complexity

* Worst complexity: O(n^2)
* Average complexity: O(n log n)
* Best complexity: O(n log n)
* Space complexity: O(log n)

<br>

* The worst-case time complexity of quick sort occurs when the partitioning always produces unbalanced sub-arrays, which can happen when the pivot is chosen poorly. In this case, the algorithm takes O(n^2) time to sort the array.
* The average and best-case time complexity of quick sort is O(n log n). The average case occurs when the partitioning produces roughly balanced sub-arrays, and the best case occurs when the pivot always partitions the array into two sub-arrays of equal size.
* The space complexity of quick sort is O(log n) because the algorithm uses a divide-and-conquer approach and sorts the sub-arrays in place. However, in the worst case where the recursion depth becomes too large, the space complexity can become O(n).

## When to use

- Quick sort is more efficient and works faster in case of **larger array** size or dataset.

- It can be also used when you have limited memory.  It sorts the array without using additional memory for creating new arrays or data structures.

Here is the [link](https://www.youtube.com/watch?v=PgBzjlCcFvc) of the video from GeeksforGeeks which might clear you idea.

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0] # choose the first element as pivot
    left = []
    right = []

    for num in arr[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)

    sorted_left = quick_sort(left) # sort the left sub-array
    sorted_right = quick_sort(right) # sort the right sub-array

    return sorted_left + [pivot] + sorted_right # combine the sorted sub-arrays

arr = [27,13,57,43,98,3,7,11,45,21,100]

print(quick_sort(arr))
```
