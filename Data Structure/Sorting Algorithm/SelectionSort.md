# Merge Sort
 
Merge sort is an efficient general-purpose, and comparison-based sorting algoritm also know as divide and conquer.

It divides the input array into two halves, calls itself for the two halves repeatedly until it breaks down to smallest part. then merges the two sorted halves.

## Implementation

1. It starts by dividing the array into two halves.
2. Repeat the procedure until it breakdown into smallest parts.
3. Then comapre the bottom halfs and sort the array putting smalles first.
4. While sorting, merge the two halves.
5. Repeat this process and you are done. :fire:

## Space and time complexity

* Worst complexity: n*log(n)
* Average complexity: n*log(n)
* Best complexity: n*log(n)
* Space complexity: n

## When to use

- Merge sort is more efficient and works faster in case of **larger array** size or dataset.

- It is also useful to sort **linked lists.**

Here is the [link](https://www.youtube.com/watch?v=JSceec-wEyw) of the video from GeeksforGeeks which might clear you idea.

```python
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

arr = [27,13,57,43,98,3,7,11,45,21,100]

print(selection_sort(arr))
```