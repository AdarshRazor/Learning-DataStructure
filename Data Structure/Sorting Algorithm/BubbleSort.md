# Bubble Sort
 
It is an sorting algorithm. Where the larger elements sort down to last and the smaller ones comes first.

Sometimes its refer to as sinking sort, where the bubble which is lighter comes to the top and the heavier items sinks to the down bottom.

![image](https://user-images.githubusercontent.com/33658792/236674196-a50f56c1-6e1c-4b26-a18f-7c74318e2e93.png)

## Implementation

1. It starts by comapring adjecent element.
2. Then swaps the larger one to the right ( Towards the end of the array, one step at a time ).
3. Keep repeating the process until the largest element comes to the end of the array.
4. Then decrease the search length by 1 as the last element is the largest.
5. Repeat this process and you are done. :fire:

## Space and time complexity

* Worst complexity: n^2
* Average complexity: n^2
* Best complexity: n
* Space complexity: 1

## When to use

- Bubble sort is easy to implement.

- It is fast enough when you have small data sets.

Here is the [link](https://www.youtube.com/watch?v=nmhjrI-aW5o) of the video from GeeksforGeeks which might clear you idea.

```python
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [27,13,57,43,98,3,7,11,45,21,100]

print(bubble_sort(arr))
```
