# Insertion Sort
 
It is an sorting algorithm. Where the element is compared to its predecessor and sort accordingly.

We can take the example of the playing card deck as the player set the card deck from higher to lower value. After picking up the card player compares it from the top and keep going down to its predecessor and placed when the position is coorect.

## Implementation

1. It starts by comapring adjecent element.
2. Then swaps the smaller no. to the left.
3. Keep repeating the process of comapring to its predecessor and shift to right.
4. After getting placed, increase the marker of unsorted element since the first element already in place after comparing.
5. Repeat this process and you are done. :fire:

## Space and time complexity

* Worst complexity: n^2
* Average complexity: n^2
* Best complexity: n
* Space complexity: 1

## When to use

- Insertion sort is used when number of **elements is small.**

- It can also be useful when input array is **almost sorted**, only few elements are misplaced in complete big array.

Here is the [link](https://www.youtube.com/watch?v=OGzPmgsI-pQ) of the video from GeeksforGeeks which might clear you idea.

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

arr = [27,13,57,43,98,3,7,11,45,21,100]

print(insertion_sort(arr))
```